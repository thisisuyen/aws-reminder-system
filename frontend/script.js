const API_BASE_URL = "https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com";
const CONFIRMED_SNS_EMAIL = "24110379@student.hcmute.edu.vn";

const form = document.querySelector("#reminder-form");
const submitButton = form.querySelector('button[type="submit"]');
const feedback = document.querySelector("#form-feedback");
const listFeedback = document.querySelector("#list-feedback");
const emailSelect = document.querySelector("#email");
const reminderTable = document.querySelector("#reminder-rows");
const createdCount = document.querySelector("#created-count");
const pendingCount = document.querySelector("#pending-count");
const sentCount = document.querySelector("#sent-count");
const refreshButton = document.querySelector("#refresh-reminders");

if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(CONFIRMED_SNS_EMAIL)) {
    const option = document.createElement("option");
    option.value = CONFIRMED_SNS_EMAIL;
    option.textContent = CONFIRMED_SNS_EMAIL + " (đã xác nhận SNS)";
    emailSelect.appendChild(option);
}

function showMessage(message, type = "error") {
    feedback.textContent = message;
    feedback.dataset.type = type;
}
function showListMessage(message, type = "info") {
    listFeedback.textContent = message;
    listFeedback.dataset.type = type;
}

async function requestJson(path, options = {}) {
    const response = await fetch(`${API_BASE_URL}${path}`, options);
    let result;
    try {
        result = await response.json();
    } catch {
        throw new Error(`API trả về nội dung không phải JSON (HTTP ${response.status})`);
    }
    if (!response.ok) {
        throw new Error(result.message || `HTTP ${response.status}`);
    }
    return result;
}

const statusLabels = {
    PENDING: "Đang chờ",
    SENDING: "Đang xử lý",
    SENT: "Đã gửi SNS",
    CANCELLED: "Đã hủy",
    SEND_FAILED: "Gửi lỗi",
    SCHEDULE_FAILED: "Lỗi tạo lịch",
};

function formatTime(timeText) {
    if (!timeText) return "—";
    const d = new Date(timeText);
    if (Number.isNaN(d.valueOf())) return String(timeText);
    return d.toLocaleString("vi-VN", {
        timeZone: "Asia/Ho_Chi_Minh", day: "2-digit", month: "2-digit",
        year: "numeric", hour: "2-digit", minute: "2-digit", hour12: false,
    });
}

function makeCell(value, className = "") {
    const td = document.createElement("td");
    td.textContent = value;
    if (className) td.className = className;
    return td;
}

function renderReminders(items) {
    reminderTable.replaceChildren();
    const sorted = [...items].sort((a, b) => String(b.createdAt || "").localeCompare(String(a.createdAt || "")));
    if (sorted.length === 0) {
        const tr = document.createElement("tr");
        const td = makeCell("Chưa có lời nhắc trong DynamoDB.");
        td.colSpan = 5;
        tr.appendChild(td);
        reminderTable.appendChild(tr);
    }
    for (const reminder of sorted) {
        const tr = document.createElement("tr");
        const tdTitle = document.createElement("td");
        const title = document.createElement("strong");
        title.className = "item-title";
        title.textContent = String(reminder.title || "(Không có tiêu đề)");
        const description = document.createElement("span");
        description.className = "item-note";
        description.textContent = String(reminder.description || "Không có nội dung");
        tdTitle.append(title, description);
        tr.appendChild(tdTitle);
        tr.appendChild(makeCell(formatTime(reminder.reminderTime), "date"));
        const tdStatus = document.createElement("td");
        const status = document.createElement("span");
        status.className = "status " + String(reminder.status || "").toLowerCase().replace(/_/g, "-");
        status.textContent = statusLabels[reminder.status] || reminder.status || "Không rõ";
        tdStatus.appendChild(status);
        tr.appendChild(tdStatus);
        tr.appendChild(makeCell(String(reminder.reminderId || ""), "item-id"));
        const tdAction = document.createElement("td");
        if (["PENDING", "SENT", "SEND_FAILED", "SCHEDULE_FAILED"].includes(reminder.status)) {
            const cancelButton = document.createElement("button");
            cancelButton.type = "button";
            cancelButton.className = "delete-button";
            cancelButton.textContent = reminder.status === "PENDING" ? "Hủy" : "Xóa";
            cancelButton.dataset.reminderId = reminder.reminderId;
            tdAction.appendChild(cancelButton);
        } else {
            tdAction.textContent = "—";
        }
        tr.appendChild(tdAction);
        reminderTable.appendChild(tr);
    }
    const to2 = (n) => String(n).padStart(2, "0");
    createdCount.textContent = to2(items.length);
    pendingCount.textContent = to2(items.filter(r => r.status === "PENDING").length);
    sentCount.textContent = to2(items.filter(r => r.status === "SENT").length);
    document.querySelector("#reminder-count").textContent = `${items.length} lời nhắc`;
}

async function loadReminders() {
    refreshButton.disabled = true;
    showListMessage("Đang tải danh sách từ DynamoDB...", "info");
    try {
        const data = await requestJson("/reminders", { method: "GET" });
        if (!Array.isArray(data.items)) throw new Error("API GET không trả về mảng items");
        renderReminders(data.items);
        showListMessage(data.truncated
            ? "Danh sách bị giới hạn theo MAX_ITEMS, chưa hiện hết dữ liệu."
            : `Đã tải ${data.items.length} lời nhắc từ API GET.`, "success");
    } catch (error) {
        showListMessage("Không tải được danh sách: " + error.message, "error");
    } finally {
        refreshButton.disabled = false;
    }
}

refreshButton.addEventListener("click", loadReminders);
reminderTable.addEventListener("click", async (event) => {
    const button = event.target.closest("button[data-reminder-id]");
    if (!button) return;
    const id = button.dataset.reminderId;
    if (!confirm(`Xóa lời nhắc ${id}? Nếu còn chờ, lịch Scheduler cũng sẽ được hủy.`)) return;
    button.disabled = true;
    showListMessage("Đang yêu cầu xóa lời nhắc...", "info");
    try {
        const result = await requestJson(`/reminders/${encodeURIComponent(id)}`, { method: "DELETE" });
        showMessage(`Đã xóa ${result.reminderId}.`, "success");
        await loadReminders();
    } catch (error) {
        showListMessage("Xóa không thành công: " + error.message, "error");
        button.disabled = false;
    }
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const title = document.querySelector("#title").value.trim();
    const description = document.querySelector("#description").value.trim();
    const date = document.querySelector("#reminder-date").value;
    const time = document.querySelector("#reminder-time").value;
    const email = emailSelect.value;
    if (!email || !date || !time || !title) {
        showMessage("Hãy nhập đủ thông tin và chọn email đã xác nhận SNS.");
        return;
    }
    // Demo project assumes the input is Vietnam local time (UTC+07:00).
    const reminderTime = `${date}T${time}:00+07:00`;
    if (new Date(reminderTime).getTime() <= Date.now() + 2 * 60_000) {
        showMessage("Hãy chọn thời gian cách hiện tại hơn 2 phút.");
        return;
    }
    submitButton.disabled = true;
    showMessage("Đang gửi yêu cầu tạo lịch...", "info");
    try {
        const result = await requestJson("/reminders", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, description, reminderTime, email }),
        });
        if (result.status === "MOCK_ONLY") {
            showMessage("Đang nối vào API Mock; chưa lưu DynamoDB hay tạo lịch.", "info");
            return;
        }
        if (result.status !== "PENDING" || !result.reminderId) {
            throw new Error("API chưa trả về kết quả tạo lịch hợp lệ");
        }
        showMessage(`Đã tạo ${result.reminderId}. Chờ đến giờ để kiểm tra SNS và trạng thái SENT.`, "success");
        form.reset();
        await loadReminders();
    } catch (error) {
        showMessage("Không tạo được lời nhắc: " + error.message, "error");
    } finally {
        submitButton.disabled = false;
    }
});

loadReminders();
