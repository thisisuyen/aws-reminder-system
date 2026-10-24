# NHẬT KÝ KIỂM THỬ TUẦN 3

**ĐỒ ÁN ĐIỆN TOÁN ĐÁM MÂY**

**HỆ THỐNG ĐẶT LỊCH NHẮC VIỆC QUA EMAIL VỚI EVENTBRIDGE SCHEDULER VÀ AMAZON SNS**

**Giảng viên hướng dẫn:** Huỳnh Xuân Phụng  
**Nhóm:** Serverless  
**Môi trường:** AWS Academy Learner Lab — `us-east-1`  
**Giai đoạn:** Tuần 3 – Hoàn thiện GET/DELETE, đồng bộ SENT, triển khai S3 và kiểm thử toàn hệ thống

**Phạm vi kiểm thử:** API GET/DELETE, hủy lịch EventBridge Scheduler, cập nhật trạng thái `SENT` sau khi SNS Publish thành công, Frontend, S3 Static Website Hosting và kiểm thử tích hợp End-to-End.

**Môi trường triển khai:** AWS Learner Lab (`us-east-1`)  
**API Gateway:** `https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com`  
**S3 Website:** `http://aws-reminder-serverless-week3-demo.s3-website-us-east-1.amazonaws.com`

**Ngày kiểm thử tích hợp:** 24/10/2026.

---

## 1. KIỂM THỬ CÁC THÀNH PHẦN

### 1.1. Backend – Nguyễn Thanh Vân (24110379)

| Mã | Chức năng / thao tác | Kết quả mong đợi | Kết quả ghi nhận | Kết luận và minh chứng |
|---|---|---|---|---|
| **B01** | Lambda GET (`reminder-get-api`) | HTTP 200, body chứa `items`/`count` | Lambda GET trả HTTP 200, có dữ liệu từ bảng DynamoDB. | **PASS** — [03-Lambda-GET-test-200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/03-Lambda-GET-test-200.png) · [01-DynamoDB-week3-baseline](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/01-DynamoDB-week3-baseline.png) |
| **B02** | GET qua HTTP API Gateway | GET `/reminders` trả dữ liệu JSON | Route GET hoạt động và trả dữ liệu JSON qua HTTP API. | **PASS** — [04-GET-HTTPAPI-route](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/04-GET-HTTPAPI-route.png) · [05-GET-http-response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/05-GET-http-response.png) |
| **B03** | Lambda DELETE với ID đang `PENDING` | DELETE thành công, không còn item trong DB | Yêu cầu DELETE thành công; bản ghi được xóa khỏi DynamoDB. | **PASS** — [07-DELETE-pending-before](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/07-DELETE-pending-before.png) · [08-DELETE-api-200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/08-DELETE-api-200.png) · [09-DELETE-DynamoDB-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/09-DELETE-DynamoDB-after.png) |
| **B04** | Hủy Scheduler khi DELETE | Lịch tương ứng được hủy | Lịch Scheduler không còn sau khi thực hiện DELETE. | **PASS** — [07b-DELETE-Scheduler-before](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/07b-DELETE-Scheduler-before.png) · [10-DELETE-Scheduler-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/10-DELETE-Scheduler-after.png) |
| **B05** | DELETE qua HTTP API Gateway | `DELETE /reminders/{id}` trả 200 | HTTP API trả mã 200 cho yêu cầu DELETE. | **PASS** — [08b-DELETE-http-route-200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/08b-DELETE-http-route-200.png) |
| **B06** | Lambda Send + DynamoDB SENT | Publish SNS thành công, ghi `SENT`, `sentAt`, `snsMessageId` | SNS Publish thành công; DynamoDB cập nhật trạng thái `SENT`. | **PASS** — [12-SEND-before-PENDING](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/12-SEND-before-PENDING.png) · [13-SEND-Lambda-success](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/13-SEND-Lambda-success.png) · [14-SEND-after-SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/14-SEND-after-SENT.png) · [15-SEND-cloudwatch](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/15-SEND-cloudwatch.png) |
| **B07** | Cấu hình Routes/CORS và Tags | Các route hoạt động; Lambda mới có tags tuần 3 | Các route và CORS được cấu hình; Lambda GET/DELETE có tags. | **PASS** — [16-APIGateway-routes-CORS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/16-APIGateway-routes-CORS.png) · [02c-Lambda-GET-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/02c-Lambda-GET-tags.png) · [06c-Lambda-DELETE-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/06c-Lambda-DELETE-tags.png) |

### 1.2. Frontend – Trần Thu Uyên (24110378)

| Mã | Chức năng / thao tác | Kết quả mong đợi | Kết quả ghi nhận | Kết luận và minh chứng |
|---|---|---|---|---|
| **F01** | Frontend gọi GET thật | Danh sách hiện dữ liệu từ DynamoDB | Frontend hiển thị danh sách được tải từ GET API. | **PASS** — [01-Frontend-GET-list](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/01-Frontend-GET-list.png) · [00-Frontend-API-GET-check](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/00-Frontend-API-GET-check.png) |
| **F02** | Tải lại trang / Làm mới | Sau F5 dữ liệu vẫn xuất hiện | Danh sách vẫn hiển thị sau khi tải lại trang. | **PASS** — [02-Frontend-refresh-persist](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/02-Frontend-refresh-persist.png) |
| **F03** | Hộp thoại xác nhận DELETE | Có bước xác nhận trước khi gửi DELETE | Hộp thoại xác nhận xuất hiện trước khi xóa. | **PASS** — [03-Frontend-cancel-confirm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/03-Frontend-cancel-confirm.png) |
| **F04** | DELETE từ website | Request DELETE trả thành công, danh sách cập nhật | DELETE thành công; danh sách được cập nhật sau thao tác. | **PASS** — [04-Frontend-delete-result](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/04-Frontend-delete-result.png) · [04b-Frontend-DELETE-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/04b-Frontend-DELETE-network.png) |
| **F05** | Frontend hiển thị SENT | GET phản ánh `status=SENT` | Giao diện hiển thị trạng thái Đã gửi SNS (`SENT`). | **PASS** — [05-Frontend-SENT-status](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/05-Frontend-SENT-status.png) |

### 1.3. Triển khai S3 – Nguyễn Thanh Vân (24110379), phối hợp Trần Thu Uyên (24110378)

| Mã | Chức năng / thao tác | Kết quả mong đợi | Kết quả ghi nhận | Kết luận và minh chứng |
|---|---|---|---|---|
| **S01** | S3 Bucket và triển khai file | Có Bucket Week=3, 3 file web, Hosting Enabled | Bucket chứa ba file website và đã bật Static Website Hosting. | **PASS** — [01-S3-bucket-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/01-S3-bucket-tags.png) · [02-S3-objects](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/02-S3-objects.png) · [03-S3-hosting-endpoint](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/03-S3-hosting-endpoint.png) |
| **S02** | Website S3 tải dữ liệu GET | Website mở và GET trả dữ liệu qua API | Website S3 hoạt động và GET API trả dữ liệu. | **PASS** — [04-S3-website-live](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04-S3-website-live.png) · [04b-S3-GET-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04b-S3-GET-network.png) |

---

## 2. KIỂM THỬ TÍCH HỢP END-TO-END (24/10/2026)

**Luồng A – Gửi email:** `ID-A = R-341298481ae543bb` (tiêu đề `IT1 - Kiem thu gui email tu S3`).

**Luồng B – Hủy trước giờ gửi:** `ID-B = R-1796c15305bd4563` (tiêu đề `IT5 - Test DELETE Scheduler`).

| Mã | Nhóm thực hiện | Dữ liệu và kết quả kiểm thử | Minh chứng | Kết quả |
|---|---|---|---|---|
| **IT1** | Vân và Uyên – POST từ website S3 | Website tạo `ID-A`; phản hồi API chứa `reminderId=R-341298481ae543bb`, `status=PENDING` và `scheduleName`. | [01-EndToEnd-POST](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/01-EndToEnd-POST.png) · [01b-EndToEnd-POST-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/01b-EndToEnd-POST-network.png) | **PASS** |
| **IT2** | Vân và Uyên – GET/PENDING | Danh sách sau GET hiện `ID-A` với trạng thái Đang chờ (`PENDING`). | [02-EndToEnd-PENDING](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/02-EndToEnd-PENDING.png) | **PASS** |
| **IT3** | Vân và Uyên – SNS / CloudWatch | Email SNS thực nhận có dòng `Ma loi nhac: R-341298481ae543bb`; có ảnh CloudWatch Lambda Send. | [03-EndToEnd-SNS-email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03-EndToEnd-SNS-email.png) · [03b-EndToEnd-SEND-cloudwatch](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03b-EndToEnd-SEND-cloudwatch.png) | **PASS** |
| **IT4** | Vân và Uyên – cập nhật SENT | Website hiện `ID-A` đã gửi; DynamoDB cùng ID chuyển `SENT`, có cột `sentAt` và `snsMessageId`. | [04-EndToEnd-SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/04-EndToEnd-SENT.png) · [04b-EndToEnd-SENT-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/04b-EndToEnd-SENT-DynamoDB.png) | **PASS** |
| **IT5** | Vân và Uyên – chuẩn bị DELETE | `ID-B` ở trạng thái `PENDING` trước thao tác DELETE. | [05-EndToEnd-DELETE-before](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/05-EndToEnd-DELETE-before.png) · [05a-EndToEnd-DELETE-website-before](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/05a-EndToEnd-DELETE-website-before.png) | **PASS** |
| **IT6** | Vân và Uyên – hủy lời nhắc | Xác nhận xóa trên website; lời nhắc không còn hiển thị và DynamoDB trả về 0 bản ghi cho `ID-B`. | [06a-EndToEnd-DELETE-confirm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06a-EndToEnd-DELETE-confirm.png) · [06-EndToEnd-DELETE-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06-EndToEnd-DELETE-after.png) · [06b-DELETE-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06b-DELETE-DynamoDB.png) | **PASS** |

### 2.1. Bảng đối chiếu mã kiểm thử

| Trường hợp | Lúc tạo | Trạng thái cuối được ghi nhận | Nguồn bằng chứng |
|---|---|---|---|
| `R-341298481ae543bb` | POST từ S3, PENDING | `SENT`, SNS email cùng ID | IT1–IT4 |
| `R-1796c15305bd4563` | PENDING, chuẩn bị DELETE | DynamoDB không còn item sau thao tác xóa | IT5–IT6 |

---

## 3. KIỂM THỬ TỰ ĐỘNG (UNIT TEST)

**Lệnh chạy:** `python -m pytest -q tests/test_week3_local.py`

**Kết quả:** `3 passed` — cả ba bài kiểm thử đạt yêu cầu.

| Test | Nội dung kiểm tra | Kết quả |
|---|---|---|
| `test_get_and_delete_pending` | GET trả item; DELETE xóa item, hủy lịch; gọi DELETE lần hai trả 404 | PASS |
| `test_send_once_and_skip_duplicate` | PENDING chuyển SENT; lặp lại event không Publish SNS lần hai | PASS |
| `test_cancelled_reminder_cannot_send` | Lời nhắc đã CANCELLED không được Publish SNS | PASS |

**Mã nguồn kiểm thử:** [tests/test_week3_local.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/tests/test_week3_local.py). Bộ kiểm thử sử dụng FakeTable, FakeScheduler và FakeSns để mô phỏng các dịch vụ AWS.

---

## 4. LỖI GẶP TRONG QUÁ TRÌNH VÀ TRẠNG THÁI XỬ LÝ

| Sự cố | Biện pháp xử lý | Kết quả |
|---|---|---|
| Website S3 từng trả `403 AccessDenied` | Kiểm tra `index.html`, cấu hình Static Website Hosting, Block Public Access và Bucket Policy. | Website truy cập được qua S3 Website Endpoint. |
| Website S3 từng báo `Không tải được danh sách: Failed to fetch` | Đối chiếu API Gateway GET và CORS Origin `http://aws-reminder-serverless-week3-demo.s3-website-us-east-1.amazonaws.com`; kiểm tra Network. | Yêu cầu GET hoạt động từ website S3. |

**Giới hạn hệ thống:** Phiên bản thử nghiệm chưa tích hợp xác thực người dùng cho API GET/DELETE. Trạng thái `SENT` được ghi nhận sau khi SNS chấp nhận Publish; email thực nhận được đối chiếu riêng ở ca IT3.

---

## 5. MÃ NGUỒN VÀ TÀI LIỆU LIÊN QUAN

| Nội dung | Liên kết GitHub |
|---|---|
| Backend GET | [backend/get_reminders.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/get_reminders.py) |
| Backend DELETE | [backend/delete_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/delete_reminder.py) |
| Backend Send | [backend/send_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/send_reminder.py) |
| Frontend index | [frontend/index.html](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) |
| Frontend style | [frontend/style.css](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css) |
| Frontend script | [frontend/script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) |
| Unit test | [tests/test_week3_local.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/tests/test_week3_local.py) |
| Bản ghi kiểm thử tuần 3 | [docs/week3-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md) |