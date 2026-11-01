# NHẬT KÝ CÔNG VIỆC TUẦN 4

<div align="center">

**ĐỒ ÁN ĐIỆN TOÁN ĐÁM MÂY**  
**HỆ THỐNG ĐẶT LỊCH NHẮC VIỆC QUA EMAIL VỚI EVENTBRIDGE SCHEDULER VÀ AMAZON SNS**

**Giảng viên hướng dẫn:** Huỳnh Xuân Phụng  
**Nhóm:** Serverless  
**Môi trường:** AWS Academy Learner Lab — `us-east-1`  
**Giai đoạn:** Tuần 4 – Kiểm thử Backend/Frontend, tích hợp, giám sát và rà soát cấu hình

</div>

| Mã số sinh viên | Họ và tên | Vai trò | Thời lượng |
|:---:|---|---|:---:|
| **24110379** | **Nguyễn Thanh Vân** | Backend & AWS / kiểm thử tích hợp | **12 giờ** |
| **24110378** | **Trần Thu Uyên** | Frontend & AWS Integration / S3 | **12 giờ** |

---

## 1. NHẬT KÝ CÔNG VIỆC — NGUYỄN THANH VÂN (24110379)

**Phạm vi thực hiện:** 05 nhiệm vụ, tổng thời lượng **12 giờ**. Kiểm thử Backend, cấu hình AWS, CloudWatch và quyền truy cập tại `us-east-1`.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm trên GitHub | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Kiểm tra API và nhánh lỗi | 2 giờ | Đối chiếu POST/GET/DELETE trên API Gateway; thử POST thiếu title, DELETE mã không tồn tại và DELETE khi lời nhắc đang gửi. API lần lượt trả 400, 404, 409. | [Kiểm thử Backend](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-backend-test.md) · [Routes](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-api-gateway-routes.png) · [400](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-01-400.png) · [404](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-02-404.png) · [409](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-03-409.png) | Hoàn thành |
| 2 | Rà soát DynamoDB, Lambda và Scheduler | 2 giờ | Kiểm tra bảng Reminders, các biến môi trường Create/GET/DELETE/Send, execution role LabRole và schedule nhắm tới Lambda Send. | [Bảng Reminders](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-dynamodb-table.png) · [Create env](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/create-01-environment-variables.png) · [LabRole](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/create-02-permissions-labrole.png) · [Scheduler target](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A04b-scheduler-target.png) | Hoàn thành |
| 3 | Theo dõi CloudWatch | 2 giờ | Ghi nhận metric Invocations, Errors, Duration, Throttles; dashboard reminder-week4-dashboard và alarm reminder-send-errors-week4. Ảnh alarm cho thấy trạng thái OK với Errors bằng 1, dưới ngưỡng lớn hơn 1. | [Monitoring](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-monitoring.md) · [Dashboard](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/02-dashboard.png) · [Trạng thái alarm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/05-alarm-triggered.png) | Hoàn thành |
| 4 | Rà soát CORS và quyền truy cập | 3 giờ | Đối chiếu origin/method CORS, role Lambda, route không gắn authorizer và bucket policy đọc object website công khai. | [Rà soát bảo mật](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-security.md) · [CORS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/security/03-api-cors.png) · [Bucket policy](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03b-s3-bucket-policy.png) | Hoàn thành |
| 5 | Đối chiếu tích hợp và tổng hợp tài liệu Backend | 3 giờ | Kiểm tra cùng reminderId trong hai luồng gửi/hủy, đối chiếu DynamoDB, Scheduler, CloudWatch, email và ghi kết quả vào tài liệu. | [Kiểm thử tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-integration-test.md) · [Email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A06-email-received.png) · [DynamoDB sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B08-dynamodb-after-delete.png) | Hoàn thành |
| | **Tổng** | **12 giờ** | **05/05 nhiệm vụ hoàn thành** | **Tài liệu và minh chứng Backend/AWS, CloudWatch, tích hợp** | **Hoàn thành** |

**Kết quả đóng góp:** Hoàn thành 5/5 nhiệm vụ với 12 giờ công phân bổ. Các route, trạng thái dữ liệu, Scheduler, CloudWatch và cấu hình quyền được đối chiếu với ảnh AWS tuần 4. Các bài thử tích hợp chung được ghi tại mục 3.

---

## 2. NHẬT KÝ CÔNG VIỆC — TRẦN THU UYÊN (24110378)

**Phạm vi thực hiện:** 05 nhiệm vụ, tổng thời lượng **12 giờ**. Kiểm thử Frontend, website S3 và hai luồng tích hợp từ giao diện.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm trên GitHub | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Kiểm tra website và GET | 2 giờ | Mở website S3, đối chiếu ba object giao diện; trình duyệt gửi GET /reminders và nhận JSON. | [Kiểm thử Frontend](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-frontend-test.md) · [Website](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/01-website-live.png) · [GET response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/02b-get-response.png) | Hoàn thành |
| 2 | Kiểm tra biểu mẫu | 2 giờ | Thử tiêu đề trống và thời gian chưa hợp lệ; đối chiếu thông báo trên giao diện. | [Tiêu đề trống](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-01-empty-title.png) · [Thời gian](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-02-invalid-time.png) | Hoàn thành |
| 3 | Kiểm tra lỗi kết nối và khôi phục | 2 giờ | Quan sát Failed to fetch khi API không truy cập được và danh sách tải lại sau khi kết nối hoạt động. | [Mất kết nối](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-03-offline.png) · [Khôi phục](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-04-recovered.png) | Hoàn thành |
| 4 | Kiểm thử luồng tạo và nhận email | 3 giờ | Đối chiếu cùng reminderId từ POST, trạng thái PENDING trên website/DynamoDB, schedule, CloudWatch, email và trạng thái SENT sau gửi. | [Kiểm thử tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-integration-test.md) · [POST](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A01-post-response.png) · [Email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A06-email-received.png) · [Frontend SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A08-frontend-sent.png) | Hoàn thành |
| 5 | Kiểm thử hủy lời nhắc đang chờ | 3 giờ | Xác nhận xóa trên website; kiểm tra lời nhắc biến mất, DynamoDB trả 0 items và Scheduler trả 0 schedules. | [Xác nhận xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B05-delete-confirm.png) · [Frontend sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B07-frontend-after-delete.png) · [DynamoDB sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B08-dynamodb-after-delete.png) · [Scheduler sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B09-scheduler-after-delete.png) | Hoàn thành |
| | **Tổng** | **12 giờ** | **05/05 nhiệm vụ hoàn thành** | **Tài liệu và minh chứng Frontend/S3, tích hợp** | **Hoàn thành** |

**Kết quả đóng góp:** Hoàn thành 5/5 nhiệm vụ với 12 giờ công phân bổ. Website S3, dữ liệu GET, phản hồi biểu mẫu và hai luồng tích hợp được ghi nhận bằng ảnh trình duyệt và AWS.

---

## 3. PHỐI HỢP NHÓM VÀ KIỂM THỬ TÍCH HỢP

**Phân công phối hợp:** Vân phụ trách Backend và cấu hình AWS; Uyên phụ trách Frontend và kiểm thử giao diện. Hai thành viên đối chiếu kết quả trên cùng hệ thống tại `us-east-1`.

| Nội dung phối hợp | Kết quả thực hiện và đối chiếu |
|---|---|
| Cấu hình API chính | Website S3 gọi cùng API Gateway `reminder-http-api` với POST, GET và DELETE. [Routes](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-api-gateway-routes.png) · [GET từ trình duyệt](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/02-get-network.png) |
| Website S3 | Ba file giao diện có trong bucket, Static Website Hosting được bật và website truy cập được. [S3 objects](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/03-s3-objects.png) · [S3 hosting](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/04-s3-hosting.png) · [Website](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/01-website-live.png) |
| Luồng ID-A (gửi email) | `R-174123c996704e9d`: POST tạo `PENDING`, schedule nhắm tới Lambda Send, email có cùng mã và DynamoDB chuyển `SENT`. [POST](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A01-post-response.png) · [Email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A06-email-received.png) · [DynamoDB SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A07-dynamodb-sent.png) |
| Luồng ID-B (hủy) | `R-2a5437efc5fc4b2d`: kiểm tra `PENDING` trước khi xóa; sau xác nhận, DynamoDB trả 0 items và Scheduler trả 0 schedules. [Trước xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B03-dynamodb-before-delete.png) · [DynamoDB sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B08-dynamodb-after-delete.png) · [Scheduler sau xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B09-scheduler-after-delete.png) |
| Khác biệt giữa trạng thái SENT và nhận email | `SENT` là trạng thái ghi trong DynamoDB sau luồng SNS Publish; email thực nhận được đối chiếu bằng ảnh hộp thư riêng. [DynamoDB SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A07-dynamodb-sent.png) · [Email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A06-email-received.png) |
| Nhật ký kiểm thử | Các bước và ảnh được ghi tại [docs/week4-backend-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-backend-test.md), [docs/week4-frontend-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-frontend-test.md) và [docs/week4-integration-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-integration-test.md). |

---

## 4. TỔNG HỢP KẾT QUẢ TUẦN 4

| Thành viên | Nhiệm vụ hoàn thành | Thời lượng | Sản phẩm |
|---|:---:|:---:|---|
| **Nguyễn Thanh Vân (24110379)** | **5/5** | **12 giờ** | Kiểm tra Backend, cấu hình AWS, CloudWatch và bảo mật |
| **Trần Thu Uyên (24110378)** | **5/5** | **12 giờ** | Kiểm tra Frontend, biểu mẫu và hai luồng tích hợp |
| **Toàn nhóm** | **10/10** | **24 giờ** | Tài liệu tuần 4 và 60 ảnh minh chứng |

### 4.1. Các file và thư mục sản phẩm

| Nội dung | Liên kết GitHub |
|---|---|
| Nhật ký công việc tuần 4 | [worklogs/week4.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week4.md) |
| Kiểm thử Backend | [docs/week4-backend-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-backend-test.md) |
| Kiểm thử Frontend | [docs/week4-frontend-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-frontend-test.md) |
| Kiểm thử tích hợp | [docs/week4-integration-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-integration-test.md) |
| Giám sát | [docs/week4-monitoring.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-monitoring.md) |
| Rà soát bảo mật | [docs/week4-security.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-security.md) |
| Ảnh tuần 4 | [minhchung/tuan4](https://github.com/thisisuyen/aws-reminder-system/tree/main/minhchung/tuan4/) |

---

## 5. KẾT LUẬN

Trong tuần 4, nhóm hoàn thành 10/10 nhiệm vụ được ghi trong hai bảng công việc với tổng thời lượng phân bổ 24 giờ. Vân kiểm tra API, cấu hình AWS, CloudWatch và quyền truy cập; Uyên kiểm tra website S3, phản hồi giao diện và hai luồng tích hợp. Ảnh minh chứng ghi nhận việc tạo lời nhắc và nhận email cùng mã, cũng như hủy lời nhắc rồi kiểm tra lại DynamoDB và Scheduler. Tài liệu kiểm thử và ảnh của từng nhiệm vụ được dẫn bằng link GitHub trong nhật ký này.
