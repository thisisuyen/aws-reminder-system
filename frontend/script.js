
// Cau hinh de demo. Chua can cap nhat khi chua co URL/API va email that.
const API_POST_URL = "https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com/reminders";
const CONFIRMED_SNS_EMAIL = "24110379@student.hcmute.edu.vn";

const form = document.querySelector("#reminder-form");
const submitButton = form.querySelector('button[type="submit"]');
const feedback = document.querySelector("#form-feedback");
const emailSelect = document.querySelector("#email");
const reminderTable = document.querySelector("#reminder-rows");
const createdCount = document.querySelector("#created-count");
const pendingCount = document.querySelector("#pending-count");
const created = [];

if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(CONFIRMED_SNS_EMAIL)) {
    const option = document.createElement("option");
    option.value = CONFIRMED_SNS_EMAIL;
    option.textContent = CONFIRMED_SNS_EMAIL + " (da xac nhan SNS)";
    emailSelect.appendChild(option);
}

function showMessage(message, type = "error") {
    feedback.textContent = message;
    feedback.dataset.type = type;
}

function addResultRow(reminder) {
    if (created.length === 1) reminderTable.replaceChildren();
    const row = document.createElement("tr");
    const titleCell = document.createElement("td");
    const name = document.createElement("strong");
    name.className = "item-title";
    name.textContent = reminder.title;
    const note = document.createElement("span");
    note.className = "item-note";
    note.textContent = reminder.description || "Khong co noi dung";
    titleCell.append(name, note);
    const timeCell = document.createElement("td");
    const date = document.createElement("span");
    date.className = "date";
    date.textContent = reminder.date.split("-").reverse().join("/");
    const clock = document.createElement("span");
    clock.className = "clock";
    clock.textContent = reminder.time;
    timeCell.append(date, clock);
    const statusCell = document.createElement("td");
    const status = document.createElement("span");
    status.className = "status pending";
    status.textContent = "PENDING";
    statusCell.append(status);
    const idCell = document.createElement("td");
    idCell.textContent = reminder.reminderId;
    row.append(titleCell, timeCell, statusCell, idCell);
    reminderTable.prepend(row);
    createdCount.textContent = String(created.length).padStart(2, "0");
    pendingCount.textContent = String(created.length).padStart(2, "0");
    document.querySelector("#reminder-count").textContent = created.length + " loi nhac";
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!/^https:\/\//.test(API_POST_URL)) {
        showMessage("Chua cau hinh URL API POST /reminders trong script.js");
        return;
    }
    const title = document.querySelector("#title").value.trim();
    const description = document.querySelector("#description").value.trim();
    const date = document.querySelector("#reminder-date").value;
    const time = document.querySelector("#reminder-time").value;
    const email = emailSelect.value;
    if (!email || !date || !time || !title) {
        showMessage("Hay nhap du thong tin va chon email da xac nhan SNS.");
        return;
    }
    // Ban demo nay gia dinh nguoi dung chon gio Viet Nam (UTC+07:00).
    const reminderTime = `${date}T${time}:00+07:00`;
    if (new Date(reminderTime).getTime() < Date.now() + 2 * 60_000) {
        showMessage("Hay chon thoi gian nhac cach hien tai hon 2 phut.");
        return;
    }

    submitButton.disabled = true;
    showMessage("Dang gui yeu cau...", "info");
    try {
        const response = await fetch(API_POST_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, description, email, reminderTime })
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.message || `Loi HTTP ${response.status}`);
        if (result.status === "MOCK_ONLY") {
            showMessage("Da ket noi API Gateway MOCK. Chua luu DynamoDB hay tao Scheduler.", "info");
            return;
        }
        if (result.status !== "PENDING" || !result.reminderId) {
            throw new Error("API chua tra ve ket qua tao lich hop le");
        }
        created.push(result.reminderId);
        addResultRow({ title, description, date, time, reminderId: result.reminderId });
        showMessage(`Da tao loi nhac ${result.reminderId}. Cho den gio hen de kiem tra email.`, "success");
        form.reset();
    } catch (error) {
        showMessage("Khong tao duoc loi nhac: " + error.message);
    } finally {
        submitButton.disabled = false;
    }
});
