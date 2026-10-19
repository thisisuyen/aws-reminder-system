# NHẬT KÝ CÔNG VIỆC TUẦN 2 (WORKLOG)

<div align="center">

**ĐỒ ÁN ĐIỆN TOÁN ĐÁM MÂY**  
**HỆ THỐNG ĐẶT LỊCH NHẮC VIỆC QUA EMAIL VỚI EVENTBRIDGE SCHEDULER VÀ SNS**

**Giảng viên hướng dẫn:** Huỳnh Xuân Phụng  
**Nhóm:** Serverless  
**Môi trường:** AWS Learner Lab — Region `us-east-1`  
**Giai đoạn:** Tuần 2 – Triển khai và kiểm thử hệ thống

</div>

| Mã số sinh viên | Họ và tên | Vai trò |
|:---:|---|---|
| **24110379** | **Nguyễn Thanh Vân** | Backend & AWS |
| **24110378** | **Trần Thu Uyên** | Frontend & AWS Integration |

**Trạng thái tuần 2:** Đã hoàn thành các nhiệm vụ được phân công.

---

## 1. NHẬT KÝ CÔNG VIỆC — NGUYỄN THANH VÂN (24110379)

**Khối lượng:** 06 nhiệm vụ chuyên môn — **10 giờ**.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Chuẩn bị AWS, DynamoDB và tags | 1 giờ | Kiểm tra Learner Lab, Region us-east-1; thiết lập bảng Reminders và tag Project/Team/Week. | [Bảng DynamoDB và tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/02-DynamoDB-table-tags.png) | Hoàn thành |
| 2 | Triển khai Lambda API | 2 giờ | Viết Python/boto3 xử lý POST /reminders; kiểm tra title, email, reminderTime; ghi Item PENDING vào DynamoDB; xử lý lỗi tạo lịch. | [Lambda API](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/create_reminder.py) · [Kết quả 201](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/08-LambdaAPI-test-success.png) | Hoàn thành |
| 3 | Cấu hình và thử EventBridge Scheduler | 2 giờ | Tạo Group reminder-week2; chọn target Lambda, role hợp lệ và lịch One-time; dùng Lambda kiểm thử ghi log vào CloudWatch. | [Lambda target test](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/scheduler_target_test.py) · [CloudWatch Logs](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/06-Scheduler-test-logs.png) | Hoàn thành |
| 4 | Kiểm tra API và dữ liệu đã lưu | 1 giờ | Chạy kiểm thử Lambda API, so khớp reminderId giữa phản hồi 201 và DynamoDB; ghi nhận trạng thái PENDING. | [Bản ghi DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/09-DynamoDB-saved-item.png) | Hoàn thành |
| 5 | Tích hợp các thành phần trên AWS chính | 3 giờ | Tích hợp Lambda Send/SNS, API Gateway POST /reminders và Frontend; chuyển script.js sang API của AWS chính, kiểm tra luồng gửi email. | [Frontend thành công](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/06-Frontend-success.png) · [Email tương ứng](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/07-EndToEnd-email-success.png) | Hoàn thành |
| 6 | Tổng hợp minh chứng và tài liệu | 1 giờ | Đối chiếu kết quả AWS thực tế, bổ sung ảnh kiểm thử Backend/tích hợp, hoàn thiện integration-test.md và push GitHub. | [integration-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/integration-test.md) | Hoàn thành |
| | **Tổng** | **10 giờ** | **06/06 nhiệm vụ** | **02 file Python, 09 ảnh Backend, 07 ảnh tích hợp, 01 tài liệu tích hợp; kết nối Frontend vào AWS chính** | **100%** |

**Kết quả đóng góp:** Tạo lời nhắc qua Lambda API, lưu DynamoDB, thiết lập lịch Scheduler, xác nhận CloudWatch Logs và tích hợp luồng Frontend → API Gateway → Lambda → DynamoDB/Scheduler → Lambda Send → SNS → Email.

---

## 2. NHẬT KÝ CÔNG VIỆC — TRẦN THU UYÊN (24110378)

**Khối lượng:** 05 nhiệm vụ chuyên môn — **09 giờ**.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Tạo SNS Topic và xác nhận Email Subscription | 2 giờ | Tạo topic, đăng ký email, xác nhận subscription và thử SNS Publish. | [Subscription Confirmed](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/02-SNS-subscription-confirmed.png) · [Email SNS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/04-SNS-email-received.png) | Hoàn thành |
| 2 | Triển khai Lambda Send | 2 giờ | Viết Lambda Python dùng sns.publish(); định dạng tiêu đề, nội dung, reminderId và kiểm thử kết quả gửi email. | [Lambda Send](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/send_reminder.py) · [Email Lambda](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/07-Lambda-send-email.png) | Hoàn thành |
| 3 | Thử API Gateway bằng Lambda Mock | 2 giờ | Tạo HTTP API POST /reminders; viết API Mock trả MOCK_ONLY, xử lý dữ liệu sai và kiểm thử CORS với giao diện. | [API Mock](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/api_gateway_mock.py) · [Mock response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/09-APIGateway-test.png) | Hoàn thành |
| 4 | Cập nhật HTML/CSS và tạo JavaScript | 2 giờ | Điều chỉnh index.html, style.css đã có từ tuần 1; tạo mới script.js xử lý form, gửi fetch POST và hiển thị PENDING/lỗi. | [HTML](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) · [CSS](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css) · [JavaScript](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) | Hoàn thành |
| 5 | Kiểm thử giao diện và cập nhật GitHub | 1 giờ | Chạy giao diện thử với API Gateway Mock, đối chiếu kết quả, lưu 10 ảnh SNS/Lambda/API/Frontend và lưu phần việc lên GitHub. | [Giao diện thử nghiệm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/10-Frontend-form.png) | Hoàn thành |
| | **Tổng** | **9 giờ** | **05/05 nhiệm vụ** | **02 file Python, 03 file Frontend (02 cập nhật, 01 tạo mới), 10 ảnh thử nghiệm** | **100%** |

**Kết quả đóng góp:** Hoàn thiện các thành phần gửi email bằng SNS, Lambda Send; triển khai API Gateway Mock; cập nhật giao diện và tạo JavaScript phục vụ tích hợp với Backend.

---

## 3. HỌP NHÓM VÀ THỐNG NHẤT TÍCH HỢP

**Thành viên tham gia:** Nguyễn Thanh Vân (24110379), Trần Thu Uyên (24110378).  
**Nội dung phối hợp:** Tích hợp các thành phần độc lập vào tài khoản AWS chính và đối chiếu kết quả kiểm thử. Thời gian phối hợp đã được tính trong các nhiệm vụ chuyên môn của mỗi người.

### 3.1. Nội dung thảo luận

| Nội dung | Kết quả thống nhất |
|---|---|
| Phân công triển khai | Vân thực hiện Backend/Scheduler; Uyên thực hiện SNS, Lambda Send, API Mock và Frontend. |
| API giao tiếp | Frontend sử dụng `POST /reminders`, truyền JSON theo cấu trúc đã thống nhất từ tuần 1. |
| Môi trường thử nghiệm | Uyên kiểm thử Mock riêng; Vân thực hiện tích hợp với API Gateway và AWS chính. |
| Xử lý lịch | EventBridge Scheduler tạo lịch One-time theo `Asia/Ho_Chi_Minh`. |
| Nhận thông báo | Lambda Send publish tới SNS Topic; email phải xác nhận Subscription. |
| Kiểm thử tích hợp | Đối chiếu mã `R-7d3d899dcdda4ed7` trên Frontend và trong email nhận lúc 02:28 ngày 19/10/2026. |
| Minh chứng | Tách ảnh Backend, Frontend và Integration; tổng hợp tại `docs/integration-test.md`. |

### 3.2. Kết quả buổi họp

Hai thành viên thống nhất giao tiếp API, tài nguyên AWS chính và phương pháp kiểm thử. Nhóm đã kiểm tra được luồng tạo lời nhắc và nhận email tương ứng.

**Minh chứng GitHub:** [Tài liệu kiểm thử](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/integration-test.md) · [Frontend](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/06-Frontend-success.png) · [Email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/07-EndToEnd-email-success.png).

---

## 4. TỔNG HỢP KẾT QUẢ TUẦN 2

| Sinh viên | Nhiệm vụ chuyên môn | Giờ công tuần 2 | Mức hoàn thành tuần 2 |
|---|:---:|:---:|:---:|
| **Nguyễn Thanh Vân – 24110379** | **6/6** | **10 giờ** | **100%** |
| **Trần Thu Uyên – 24110378** | **5/5** | **9 giờ** | **100%** |
| **Toàn nhóm** | **11/11** | **19 giờ** | **100%** |

**Kết quả tuần 2:** Hoàn thành toàn bộ **11/11 nhiệm vụ chuyên môn**, kiểm thử thành công chức năng tạo lời nhắc và gửi email tự động. Thời gian phối hợp nhóm đã tính trong các nhiệm vụ, không cộng thêm. Mức 100% là mức hoàn thành công việc tuần 2, không phải toàn bộ đồ án.
