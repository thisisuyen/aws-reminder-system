# KIỂM THỬ TÍCH HỢP HỆ THỐNG NHẮC VIỆC – TUẦN 2

**Đồ án:** Hệ thống đặt lịch nhắc việc qua Email với EventBridge Scheduler và Amazon SNS  
**Nhóm:** Serverless  
**Nguyễn Thanh Vân (24110379):** Backend, triển khai và tích hợp AWS  
**Trần Thu Uyên (24110378):** Frontend, Lambda Send và AWS Integration  
**Môi trường:** AWS Academy Learner Lab – Region `us-east-1`  
**Thời gian kiểm thử:** 18–19/10/2026 (GMT+7)

## 1. Kiến trúc hệ thống

```text
Frontend (HTML, CSS, JavaScript)
  → API Gateway: POST /reminders
  → AWS Lambda: reminder-create-api
      ├── DynamoDB: Reminders (lưu dữ liệu lời nhắc)
      └── EventBridge Scheduler: reminder-week2 (tạo lịch một lần)
          → AWS Lambda: reminder-send
          → Amazon SNS: reminder-email-topic
          → Email Subscription
```

Hệ thống tiếp nhận yêu cầu tạo lời nhắc từ giao diện web, lưu thông tin vào DynamoDB và tạo lịch với EventBridge Scheduler. Đến thời điểm hẹn, Lambda Send sử dụng Amazon SNS để gửi email đến subscription đã xác nhận.

## 2. Tài nguyên triển khai AWS

| Dịch vụ | Tên tài nguyên | Liên kết AWS Console |
|---|---|---|
| Amazon DynamoDB | `Reminders` | [Xem DynamoDB](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#table?name=Reminders) |
| AWS Lambda – tạo lời nhắc | `reminder-create-api` | [Xem Lambda API](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/reminder-create-api?tab=code) |
| Amazon EventBridge Scheduler | Schedule Group `reminder-week2` | [Xem Schedule Group](https://us-east-1.console.aws.amazon.com/scheduler/home?region=us-east-1#schedule-groups/reminder-week2) |
| AWS IAM | `LabRole` | [Xem IAM Role](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/roles/details/LabRole) |
| AWS Lambda – gửi email | `reminder-send` | [Xem Lambda Send](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/reminder-send?tab=code) |
| Amazon SNS | Topic `reminder-email-topic` | [Xem SNS Topic](https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/topic/arn:aws:sns:us-east-1:904706796409:reminder-email-topic) |
| Amazon SNS | Email Subscription đã xác nhận | [Xem Subscription](https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/subscription/arn:aws:sns:us-east-1:904706796409:reminder-email-topic:0e11f9e4-ba2e-4b8f-a299-2f8c0e522c6d) |
| Amazon API Gateway | `reminder-http-api` – `POST /reminders` | [Xem API Gateway](https://us-east-1.console.aws.amazon.com/apigateway/main/develop/routes?api=c3vvd6ghug&region=us-east-1) |

**HTTP API Endpoint:** `https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com/reminders`  
**Bộ tag của dự án:** `Project=AWSReminderSystem`, `Team=Serverless`, `Week=2`.

## 3. Kết quả kiểm thử và minh chứng

### 3.1. Backend và Scheduler – Nguyễn Thanh Vân

| Hạng mục | Kết quả ghi nhận | Ảnh minh chứng |
|---|---|---|
| Môi trường AWS | Truy cập Learner Lab ở Region `us-east-1`. | [01-AWS-LearnerLab.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/01-AWS-LearnerLab.png) |
| DynamoDB | Bảng `Reminders` được gắn ba tag của dự án. | [02-DynamoDB-table-tags.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/02-DynamoDB-table-tags.png) |
| Lambda đích kiểm thử | Lambda `reminder-target-test` trả `ok=true` khi chạy thử. | [03-Lambda-target-test.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/03-Lambda-target-test.png) |
| Schedule Group | Group `reminder-week2` ở trạng thái Active, có ba tag dự án. | [04-ScheduleGroup-tags.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/04-ScheduleGroup-tags.png) |
| Lịch thử nghiệm | Lịch `test-reminder-manual` thuộc Group `reminder-week2`, đặt chạy một lần với `Action after completion: DELETE`. | [05-Scheduler-test-config.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/05-Scheduler-test-config.png) |
| CloudWatch | Ghi nhận sự kiện `SCHEDULER_TRIGGERED` đối với `R-TEST-002`. | [06-Scheduler-test-logs.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/06-Scheduler-test-logs.png) |
| Cấu hình Lambda API | Ghi nhận màn hình biến môi trường của Lambda API trong giai đoạn kiểm thử Backend. | [07-LambdaAPI-config.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/07-LambdaAPI-config.png) |
| Tạo lời nhắc qua Lambda API | Lambda API trả `statusCode=201`, `status=PENDING`, mã `R-f431cf991562446c` và thông tin lịch. | [08-LambdaAPI-test-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/08-LambdaAPI-test-success.png) |
| Lưu DynamoDB | Bảng `Reminders` có mục `R-f431cf991562446c` với trạng thái `PENDING` tại thời điểm chụp. | [09-DynamoDB-saved-item.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/backend/09-DynamoDB-saved-item.png) |

### 3.2. SNS, Lambda Send, API Gateway Mock và Frontend – Trần Thu Uyên

| Hạng mục | Kết quả ghi nhận | Ảnh minh chứng |
|---|---|---|
| SNS Topic | Tạo Topic `reminder-email-topic`. | [01-SNS-topic-tags.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/01-SNS-topic-tags.png) |
| SNS Subscription | Email Subscription ở trạng thái Confirmed. | [02-SNS-subscription-confirmed.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/02-SNS-subscription-confirmed.png) |
| SNS Publish | Kiểm thử gửi thông báo trực tiếp từ SNS thành công. | [03-SNS-publish-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/03-SNS-publish-success.png) |
| Nhận email SNS | Hộp thư nhận được thông báo từ SNS. | [04-SNS-email-received.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/04-SNS-email-received.png) |
| Cấu hình Lambda Send | Triển khai Lambda `reminder-send` trong tài khoản thử nghiệm của Uyên. | [05-Lambda-send-config.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/05-Lambda-send-config.png) |
| Kiểm thử Lambda Send | Lambda Send trả kết quả chạy thành công. | [06-Lambda-send-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/06-Lambda-send-success.png) |
| Email từ Lambda Send | Hộp thư nhận thông báo do Lambda Send gửi qua SNS. | [07-Lambda-send-email.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/07-Lambda-send-email.png) |
| HTTP API Gateway | Có HTTP API và stage `$default` để kiểm thử kết nối. | [08-APIGateway-route.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/08-APIGateway-route.png) |
| Kiểm thử API Mock | API trả phản hồi `status=MOCK_ONLY` khi gọi thử. | [09-APIGateway-test.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/09-APIGateway-test.png) |
| Frontend thử nghiệm | Form tạo lời nhắc hoạt động với API Gateway Mock. | [10-Frontend-form.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/frontend/10-Frontend-form.png) |

### 3.3. Kiểm thử tích hợp trên tài khoản AWS chính

| Hạng mục | Kết quả ghi nhận | Ảnh minh chứng |
|---|---|---|
| Kiểm thử SNS trên tài khoản chính | Hộp thư nhận email thử với tiêu đề `Kiem tra SNS tai khoan Van`. | [01-SNS-main.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/01-SNS-main.png) |
| Lambda Send sau tích hợp | Lambda `reminder-send` trả `ok=true` và `snsMessageId` cho `R-INTEGRATION-001`. | [02-LambdaSend-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/02-LambdaSend-success.png) |
| Email nhắc việc sau tích hợp | Gmail nhận email `Hop bao cao tuan 2` mang mã `R-518a68eca67e4643`. | [03-Scheduler-SNS-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/03-Scheduler-SNS-success.png) |
| API Gateway chính | API `reminder-http-api` (`c3vvd6ghug`) có route `POST /reminders`. | [04-APIGateway-main.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/04-APIGateway-main.png) |
| Email từ lượt kiểm thử API | Hộp thư nhận email `Kiem tra API Gateway` mang mã `R-09adc72eed1042b7`. | [05-API-POST-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/05-API-POST-success.png) |
| Lời nhắc trên Frontend | Web tạo lời nhắc `R-7d3d899dcdda4ed7`, hẹn 02:28 ngày 19/10/2026, hiển thị `PENDING`. | [06-Frontend-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/06-Frontend-success.png) |
| Email tương ứng với Frontend | Gmail nhận email mang cùng mã `R-7d3d899dcdda4ed7` lúc 02:28 ngày 19/10/2026. | [07-EndToEnd-email-success.png](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan2/integration/07-EndToEnd-email-success.png) |

**Đối chiếu toàn luồng:** Lời nhắc `R-7d3d899dcdda4ed7` xuất hiện trên giao diện với thời gian hẹn **02:28 ngày 19/10/2026**; Gmail nhận email chứa cùng mã lời nhắc vào **02:28**. Hai ảnh tương ứng thể hiện kết quả từ bước tạo lời nhắc trên web đến bước nhận thông báo qua email.

## 4. Mã nguồn tuần 2

| Người phụ trách | Thành phần | File GitHub |
|---|---|---|
| Nguyễn Thanh Vân | Lambda API | [backend/create_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/create_reminder.py) |
| Nguyễn Thanh Vân | Lambda kiểm thử Scheduler | [backend/scheduler_target_test.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/scheduler_target_test.py) |
| Trần Thu Uyên | Lambda Send / SNS | [backend/send_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/send_reminder.py) |
| Trần Thu Uyên | API Gateway Mock | [backend/api_gateway_mock.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/api_gateway_mock.py) |
| Trần Thu Uyên | Giao diện HTML | [frontend/index.html](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) |
| Trần Thu Uyên | CSS giao diện | [frontend/style.css](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css) |
| Trần Thu Uyên | JavaScript kết nối API | [frontend/script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) |

**Repository:** https://github.com/thisisuyen/aws-reminder-system  
**Tài liệu kiểm thử:** [docs/integration-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/integration-test.md)

## 5. Kết luận

Các kết quả kiểm thử tuần 2 cho thấy nhóm đã triển khai được các thành phần tạo lời nhắc, lưu dữ liệu vào DynamoDB, tạo lịch bằng EventBridge Scheduler, xử lý thông báo qua Lambda Send và SNS, đồng thời thử nghiệm thành công quá trình tạo lời nhắc trên web và nhận email có cùng mã lời nhắc. Giao diện hiển thị những lời nhắc vừa tạo trong phiên trình duyệt và trạng thái `PENDING` sau khi tạo lịch.