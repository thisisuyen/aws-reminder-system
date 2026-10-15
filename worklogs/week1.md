# NHẬT KÝ CÔNG VIỆC TUẦN 1 (WORKLOG)

<div align="center">

**ĐỒ ÁN ĐIỆN TOÁN ĐÁM MÂY**  
**HỆ THỐNG ĐẶT LỊCH NHẮC VIỆC QUA EMAIL VỚI EVENTBRIDGE SCHEDULER VÀ SNS**

**Giảng viên hướng dẫn:** Huỳnh Xuân Phụng  
**Nhóm:** Serverless  
**Môi trường:** AWS Learner Lab — Region `us-east-1`  
**Giai đoạn:** Tuần 1 – Tìm hiểu, phân tích và thiết kế hệ thống

</div>

| Mã số sinh viên | Họ và tên | Vai trò |
|:---:|---|---|
| **24110379** | **Nguyễn Thanh Vân** | Backend & AWS |
| **24110378** | **Trần Thu Uyên** | Frontend & AWS Integration |

**Trạng thái tuần 1:** Đã hoàn thành các nhiệm vụ được phân công.

---

## 1. NHẬT KÝ CÔNG VIỆC — NGUYỄN THANH VÂN (24110379)

**Khối lượng:** 06 nhiệm vụ chuyên môn — **08 giờ**.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Tìm hiểu AWS Lambda | 1 giờ | Nghiên cứu Function, Runtime Python, Handler, Event và execution role; phân tích luồng API Gateway gọi Lambda xử lý lời nhắc. | Xác định chức năng `reminder-api-lambda`, đầu vào/đầu ra và vai trò trong kiến trúc. ([Thiết kế API dùng Lambda](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/api-design.md) · [Sơ đồ tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/architecture.png)) | Hoàn thành |
| 2 | Tìm hiểu DynamoDB | 1 giờ | Nghiên cứu Table, Item, Attribute, Partition Key; phân tích thao tác thêm, đọc, liệt kê, xóa và cập nhật lời nhắc. | Xác định bảng `Reminders` và khóa chính `reminderId` kiểu String. ([Thiết kế database](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/database-design.md)) | Hoàn thành |
| 3 | Tìm hiểu EventBridge Scheduler | 2 giờ | Nghiên cứu One-time schedule, Target Lambda, timezone `Asia/Ho_Chi_Minh`, Flexible Time Window OFF và vai trò execution role. | Xây dựng phương án kích hoạt `reminder-send-lambda` đúng lịch và xử lý hủy lịch khi xóa lời nhắc. ([Sơ đồ Scheduler](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/architecture.png) · [Thiết kế scheduleName](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/database-design.md)) | Hoàn thành |
| 4 | Thiết kế bảng DynamoDB | 1 giờ | Thiết kế tám thuộc tính, bản ghi JSON mẫu, quy tắc dữ liệu và liên kết với Scheduler qua `scheduleName`. | `docs/database-design.md` ([File thiết kế](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/database-design.md)) | Hoàn thành |
| 5 | Thiết kế API | 1 giờ | Đặc tả ba endpoint POST/GET/DELETE, request/response JSON và mã trạng thái HTTP. | `docs/api-design.md` ([File API](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/api-design.md)) | Hoàn thành |
| 6 | Vẽ sơ đồ kiến trúc AWS | 2 giờ | Biểu diễn luồng S3 → API Gateway → Lambda API → DynamoDB/EventBridge Scheduler → Lambda Send → SNS → Email; bổ sung CloudWatch và IAM. | `docs/architecture.png` ([Sơ đồ](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/architecture.png)) | Hoàn thành |
| | **Tổng** | **8 giờ** | **Hoàn thành 6/6 nhiệm vụ chuyên môn** | **03 file thiết kế và kết quả nghiên cứu** | **100%** |

**Kết quả đóng góp:** Hoàn thiện thiết kế backend, cấu trúc lưu trữ, hợp đồng API và sơ đồ kiến trúc làm cơ sở triển khai trong tuần 2.

---

## 2. NHẬT KÝ CÔNG VIỆC — TRẦN THU UYÊN (24110378)

**Khối lượng:** 07 nhiệm vụ chuyên môn — **08 giờ**.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm | Trạng thái |
|:---:|---|:---|---|---|:---:|
| 1 | Tìm hiểu API Gateway | 1 giờ | Nghiên cứu HTTP API, Route, Integration, Invoke URL và CORS; xác định cách website gọi Lambda thông qua API Gateway. | Xác định phương án kết nối ba endpoint `/reminders` với `reminder-api-lambda`. ([Tài liệu API Gateway](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/aws-services.md)) | Hoàn thành |
| 2 | Tìm hiểu Amazon SNS | 1 giờ | Nghiên cứu Topic, Subscription, Publish và xác nhận đăng ký email. | Xác định Topic dự kiến `reminder-notification-topic` và phương án gửi tới email đã xác nhận. ([Tài liệu SNS](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/aws-services.md)) | Hoàn thành |
| 3 | Tìm hiểu S3 Static Website Hosting | 1 giờ | Nghiên cứu Bucket, cách lưu HTML/CSS/JS, index document và cơ chế cung cấp website tĩnh. | Xác định cách triển khai frontend trên Amazon S3 trong tuần tiếp theo. ([Tài liệu S3](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/aws-services.md)) | Hoàn thành |
| 4 | Tìm hiểu CloudWatch và IAM LabRole | 1 giờ | Nghiên cứu CloudWatch Logs, Log Group, Log Stream, IAM Role và quyền truy cập giữa các dịch vụ. | Xác định vai trò giám sát và phân quyền cho các thành phần AWS; phần tài liệu do Uyên tổng hợp. ([Tài liệu CloudWatch/IAM](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/aws-services.md)) | Hoàn thành |
| 5 | Thiết kế giao diện website | 2 giờ | Xây dựng giao diện HTML/CSS hai cột: form tạo lời nhắc bên trái, danh sách lời nhắc bên phải; sử dụng dữ liệu mẫu và bố cục responsive. | `frontend/index.html`, `frontend/style.css` ([HTML](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) · [CSS](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css)) | Hoàn thành |
| 6 | Tạo GitHub Repository và README | 1 giờ | Tổ chức Repository chung, mô tả mục tiêu, kiến trúc, phân công, cấu trúc thư mục và kế hoạch phát triển. | Repository `aws-reminder-system`, `README.md` ([README](https://github.com/thisisuyen/aws-reminder-system/blob/main/README.md)) | Hoàn thành |
| 7 | Tổng hợp tài liệu dịch vụ AWS | 1 giờ | Tổng hợp chức năng và vai trò tích hợp của S3, API Gateway, Lambda, DynamoDB, Scheduler, SNS, CloudWatch và IAM. | `docs/aws-services.md` ([Tài liệu AWS](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/aws-services.md)) | Hoàn thành |
| | **Tổng** | **8 giờ** | **Hoàn thành 7/7 nhiệm vụ chuyên môn** | **02 file giao diện, README, tài liệu AWS** | **100%** |

**Kết quả đóng góp:** Hoàn thiện giao diện website mẫu, chuẩn bị Repository dùng chung và tài liệu mô tả các dịch vụ AWS phục vụ tích hợp trong tuần 2.

---

## 3. HỌP NHÓM VÀ THỐNG NHẤT THIẾT KẾ

**Thành viên tham gia:** Nguyễn Thanh Vân (24110379), Trần Thu Uyên (24110378).  
**Thời lượng họp:** **02 giờ/người** — tổng **04 giờ công**.  
**Trạng thái:** Hoàn thành.

### 3.1. Nội dung thảo luận

| Nội dung | Kết quả thống nhất |
|---|---|
| Mục tiêu hệ thống | Cho phép tạo, xem, xóa lời nhắc và gửi email tự động đến thời gian đã chọn. |
| Phạm vi tuần 1 | Hoàn thành nghiên cứu, kiến trúc, thiết kế cơ sở dữ liệu/API và giao diện mẫu; chưa yêu cầu các dịch vụ chạy tích hợp thật. |
| Kiến trúc hệ thống | `S3 → API Gateway → Lambda API → DynamoDB / EventBridge Scheduler → Lambda Send → SNS → Email`; CloudWatch phục vụ log, IAM quản lý quyền. |
| Cơ sở dữ liệu | Bảng DynamoDB `Reminders`, khóa `reminderId` kiểu String; tám thuộc tính theo thiết kế. |
| Giao tiếp frontend–backend | Sử dụng JSON; ba API: `POST /reminders`, `GET /reminders`, `DELETE /reminders/{id}`. |
| Thời gian nhắc việc | Dữ liệu theo ISO 8601 có múi giờ; Scheduler sử dụng `Asia/Ho_Chi_Minh`, One-time và Flexible Time Window OFF. |
| Gửi thông báo | Sử dụng Amazon SNS và email đã xác nhận subscription trong phạm vi demo. |
| Giao diện | Form tạo lời nhắc ở cột trái; danh sách lời nhắc ở cột phải; giao diện HTML/CSS mẫu, chưa kết nối API trong tuần 1. |
| Phân công | Vân phụ trách backend/thiết kế; Uyên phụ trách frontend, tích hợp AWS, GitHub và tài liệu dịch vụ. |
| Lưu trữ và minh chứng | Sản phẩm và minh chứng lưu trong GitHub; báo cáo không nhúng ảnh minh chứng. |

### 3.2. Kết quả buổi họp

Nhóm thống nhất kiến trúc Serverless, cấu trúc bảng `Reminders`, định dạng dữ liệu giao tiếp và phạm vi chức năng của website. Nhiệm vụ được phân chia rõ giữa backend và frontend để tránh trùng lặp. Các sản phẩm tuần 1 được tập hợp trong một Repository chung làm nền tảng triển khai các dịch vụ AWS ở tuần 2.

---

## 4. TỔNG HỢP KẾT QUẢ TUẦN 1

| Sinh viên | Nhiệm vụ chuyên môn | Giờ chuyên môn | Họp nhóm | Tổng giờ | Mức hoàn thành tuần 1 |
|---|:---:|:---:|:---:|:---:|:---:|
| **Nguyễn Thanh Vân – 24110379** | **6/6** | 8 giờ | 2 giờ | **10 giờ** | **100%** |
| **Trần Thu Uyên – 24110378** | **7/7** | 8 giờ | 2 giờ | **10 giờ** | **100%** |
| **Toàn nhóm** | **13/13** | **16 giờ** | **4 giờ công** | **20 giờ công** | **100%** |

**Kết quả tuần 1:** Đã hoàn thành toàn bộ **13/13 nhiệm vụ chuyên môn** và nội dung họp nhóm được phân công. Mức **100%** chỉ phản ánh mức hoàn thành công việc **trong tuần 1**, không phải tỷ lệ hoàn thành toàn bộ đồ án 4 tuần.
