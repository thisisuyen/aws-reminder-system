# AWS REMINDER SYSTEM

## 1. Giới thiệu

Hệ thống đặt lịch nhắc việc qua Email sử dụng kiến trúc **AWS Serverless**. Người dùng nhập nội dung và thời gian nhắc trên website; khi đến thời điểm đã đặt, hệ thống tự động gửi thông báo đến email đã xác nhận.

**Kết quả đến hết tuần 2:** Đã triển khai và kiểm thử thành công chức năng tạo lời nhắc từ giao diện web đến nhận email qua AWS.

## 2. Công nghệ sử dụng

- **Frontend:** HTML, CSS, JavaScript.
- **Backend:** AWS Lambda (Python, boto3).
- **Giao tiếp:** Amazon API Gateway HTTP API.
- **Lưu trữ dữ liệu:** Amazon DynamoDB.
- **Lập lịch:** Amazon EventBridge Scheduler.
- **Gửi email:** Amazon SNS.
- **Nhật ký và phân quyền:** Amazon CloudWatch, AWS IAM.
- **Dự kiến triển khai website:** Amazon S3.

## 3. Kiến trúc

```text
Frontend (HTML/CSS/JavaScript)
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

## 4. Chức năng

| Chức năng | Kết quả đến tuần 2 |
|---|---|
| Tạo lời nhắc bằng `POST /reminders` | Đã triển khai và kiểm thử |
| Lưu dữ liệu vào DynamoDB | Đã kiểm thử |
| Tạo lịch EventBridge Scheduler | Đã kiểm thử |
| Tự động gửi email qua Lambda Send và SNS | Đã kiểm thử |
| Hiển thị lời nhắc vừa tạo trên Frontend | Đã có trong phiên trình duyệt |
| Xem danh sách qua `GET /reminders` | Chưa triển khai hoàn chỉnh |
| Xóa lời nhắc qua `DELETE /reminders/{id}` | Chưa triển khai hoàn chỉnh |
| Cập nhật trạng thái `SENT` và triển khai web lên S3 | Giai đoạn sau |

SNS gửi thông báo đến **Email Subscription đã xác nhận**. Danh sách lời nhắc trên giao diện hiện chỉ gồm những lời nhắc vừa tạo trong phiên trình duyệt.

## 5. Thành viên

### 24110379 – Nguyễn Thanh Vân

**Backend & AWS**

- Xây dựng `create_reminder.py` và `scheduler_target_test.py`.
- Triển khai DynamoDB, Scheduler và kiểm thử CloudWatch Logs.
- Tích hợp các dịch vụ vào AWS chính, kết nối Frontend và tổng hợp tài liệu kiểm thử.

### 24110378 – Trần Thu Uyên

**Frontend & AWS Integration**

- Xây dựng `send_reminder.py` và `api_gateway_mock.py`.
- Triển khai SNS, Lambda Send và thử nghiệm API Gateway Mock.
- Cập nhật `index.html`, `style.css` từ tuần 1; tạo mới `script.js` trong tuần 2.

## 6. Kế hoạch

| Tuần | Công việc |
|---|---|
| **Tuần 1** | Nghiên cứu AWS, thiết kế kiến trúc, DynamoDB, API và giao diện mẫu. |
| **Tuần 2** | Triển khai các dịch vụ, cập nhật Frontend và kiểm thử luồng email tự động. |
| **Tuần 3** | Phát triển GET/DELETE, hoàn thiện danh sách, trạng thái và xem xét triển khai S3. |
| **Tuần 4** | Kiểm thử mở rộng, hoàn thiện chức năng và báo cáo. |

## 7. Cấu trúc dự án

```text
aws-reminder-system/
├── README.md
├── backend/
│   ├── create_reminder.py
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
│   └── integration-test.md
├── worklogs/
│   ├── week1.md
│   └── week2.md
└── minhchung/
    ├── tuan1/
    └── tuan2/
        ├── backend/
        ├── frontend/
        └── integration/
```

## 8. Môi trường

- **AWS:** Academy Learner Lab, Region `us-east-1`.
- **API Gateway chính:** `https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com/reminders`.
- **Repository:** https://github.com/thisisuyen/aws-reminder-system.
- **Kiểm thử:** [docs/integration-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/integration-test.md).
- **Nhật ký công việc:** [worklogs/week1.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week1.md) · [worklogs/week2.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week2.md).

## 9. Trạng thái

**Tuần 1:** Hoàn thành nghiên cứu và thiết kế.

**Tuần 2:** Đã kiểm thử luồng **Frontend → API Gateway → Lambda API → DynamoDB / Scheduler → Lambda Send → SNS → Email**. Kết quả được ghi nhận tại [giao diện tạo lời nhắc](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/06-Frontend-success.png) và [email nhận được](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/07-EndToEnd-email-success.png).
