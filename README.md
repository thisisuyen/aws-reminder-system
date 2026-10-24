# AWS REMINDER SYSTEM

## 1. Giới thiệu

Hệ thống đặt lịch nhắc việc qua Email sử dụng kiến trúc **AWS Serverless**. Người dùng nhập nội dung và thời gian nhắc trên website; khi đến thời điểm đã đặt, hệ thống tự động gửi thông báo đến email đã xác nhận.

**Kết quả đến hết tuần 3:** Đã hoàn thành POST, GET, DELETE, cập nhật trạng thái `SENT`, triển khai Frontend lên S3 và kiểm thử tích hợp gửi email qua SNS.

## 2. Công nghệ sử dụng

- **Frontend:** HTML, CSS, JavaScript.
- **Backend:** AWS Lambda (Python, boto3).
- **Giao tiếp:** Amazon API Gateway HTTP API.
- **Lưu trữ dữ liệu:** Amazon DynamoDB.
- **Lập lịch:** Amazon EventBridge Scheduler.
- **Gửi email:** Amazon SNS.
- **Nhật ký và phân quyền:** Amazon CloudWatch, AWS IAM.
- **Triển khai website tĩnh:** Amazon S3.

## 3. Kiến trúc

```text
Frontend trên S3 (HTML/CSS/JavaScript)
              |
              v
         API Gateway
              |
              v
      Lambda Create API
          /         \
         v           v
     DynamoDB    EventBridge Scheduler
                       |
                       v
                  Lambda Send
                       |
                       v
                      SNS
                       |
                       v
                 Email đã xác nhận
```

Ngoài Lambda Create, tuần 3 bổ sung Lambda GET/DELETE để đọc, xóa dữ liệu DynamoDB và hủy lịch Scheduler khi cần; Lambda Send ghi trạng thái `SENT` sau khi SNS chấp nhận Publish.

## 4. Chức năng

| Chức năng | Kết quả đến tuần 3 |
|---|---|
| Tạo lời nhắc bằng `POST /reminders` | Đã triển khai và kiểm thử |
| Lưu dữ liệu vào DynamoDB | Đã kiểm thử |
| Tạo lịch EventBridge Scheduler | Đã kiểm thử |
| Tự động gửi email qua Lambda Send và SNS | Đã kiểm thử |
| Hiển thị danh sách và trạng thái trên Frontend | Đã kết nối GET từ DynamoDB |
| Xem danh sách qua `GET /reminders` | Đã triển khai và kiểm thử |
| Xóa lời nhắc qua `DELETE /reminders/{id}` | Đã triển khai và kiểm thử |
| Cập nhật trạng thái `SENT` và triển khai web lên S3 | Đã triển khai và kiểm thử tuần 3 |

SNS gửi thông báo đến **Email Subscription đã xác nhận**. Danh sách lời nhắc trên giao diện được tải từ DynamoDB qua API GET; `SENT` nghĩa là SNS đã chấp nhận Publish, không tự xác nhận email đã vào hộp thư.

## 5. Thành viên

### 24110379 – Nguyễn Thanh Vân

**Backend & AWS**

- Xây dựng `create_reminder.py` và `scheduler_target_test.py`.
- Triển khai DynamoDB, Scheduler và kiểm thử CloudWatch Logs.
- Tích hợp các dịch vụ vào AWS chính, kết nối Frontend và tổng hợp tài liệu kiểm thử.
- **Tuần 3:** Phát triển `get_reminders.py`, `delete_reminder.py`; cập nhật `send_reminder.py`, bổ sung unit test, kiểm thử Backend và S3.

### 24110378 – Trần Thu Uyên

**Frontend & AWS Integration**

- Xây dựng `send_reminder.py` và `api_gateway_mock.py`.
- Triển khai SNS, Lambda Send và thử nghiệm API Gateway Mock.
- Cập nhật `index.html`, `style.css` từ tuần 1; tạo mới `script.js` trong tuần 2.
- **Tuần 3:** Bổ sung xem danh sách, xóa và hiển thị `SENT` trên Frontend; phối hợp kiểm thử Integration và tổng hợp minh chứng.

## 6. Kế hoạch

| Tuần | Công việc |
|---|---|
| **Tuần 1** | Nghiên cứu AWS, thiết kế kiến trúc, DynamoDB, API và giao diện mẫu. |
| **Tuần 2** | Triển khai các dịch vụ, cập nhật Frontend và kiểm thử luồng email tự động. |
| **Tuần 3** | Hoàn thành GET/DELETE, trạng thái `SENT`, cập nhật Frontend, triển khai S3 và kiểm thử tích hợp. |
| **Tuần 4** | Kiểm thử mở rộng, hoàn thiện chức năng và báo cáo. |

## 7. Cấu trúc dự án

```text
aws-reminder-system/
├── README.md
├── backend/
│   ├── create_reminder.py
│   ├── get_reminders.py
│   ├── delete_reminder.py
│   ├── scheduler_target_test.py
│   ├── send_reminder.py
│   └── api_gateway_mock.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── docs/
│   ├── architecture.png
│   ├── api-design.md
│   ├── database-design.md
│   ├── aws-services.md
│   ├── integration-test.md
│   └── week3-test.md
├── tests/
│   └── test_week3_local.py
├── worklogs/
│   ├── week1.md
│   └── week2.md
└── minhchung/
    ├── tuan1/
    ├── tuan2/
    │   ├── backend/
    │   ├── frontend/
    │   └── integration/
    └── tuan3/
        ├── backend/
        ├── frontend/
        ├── s3/
        └── integration/
```

## 8. Môi trường

- **AWS:** Academy Learner Lab, Region `us-east-1`.
- **API Gateway chính:** `https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com/reminders`.
- **Website S3:** [Mở website](http://aws-reminder-serverless-week3-demo.s3-website-us-east-1.amazonaws.com).
- **Repository:** https://github.com/thisisuyen/aws-reminder-system.
- **Kiểm thử:** [tuần 2](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/integration-test.md) · [tuần 3](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md).
- **Nhật ký công việc:** [worklogs/week1.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week1.md) · [worklogs/week2.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week2.md).

## 9. Trạng thái

**Tuần 1:** Hoàn thành nghiên cứu và thiết kế.

**Tuần 2:** Đã kiểm thử luồng **Frontend → API Gateway → Lambda API → DynamoDB / Scheduler → Lambda Send → SNS → Email**. Kết quả được ghi nhận tại [giao diện tạo lời nhắc](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/06-Frontend-success.png) và [email nhận được](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/07-EndToEnd-email-success.png).

**Tuần 3:** Đã kiểm thử GET/DELETE, trạng thái `SENT`, Frontend trên S3 và luồng tích hợp. Minh chứng: [GET trên Frontend](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/01-Frontend-GET-list.png) · [email tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03-EndToEnd-SNS-email.png) · [website S3](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04-S3-website-live.png).
