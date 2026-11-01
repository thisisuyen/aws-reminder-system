# Kiểm thử tích hợp End-to-End — Tuần 4

## Môi trường

- Region: us-east-1.
- Website S3 gọi HTTP API reminder-http-api.
- Các thành phần trong luồng: Frontend, API Gateway, Lambda, DynamoDB Reminders, EventBridge Scheduler, Lambda Send và SNS.

## Luồng A — Tạo lời nhắc và nhận email

Lời nhắc R-174123c996704e9d được tạo từ website. API trả trạng thái PENDING; DynamoDB lưu bản ghi; Scheduler tạo lịch một lần trỏ tới Lambda reminder-send. Sau thời điểm hẹn, CloudWatch ghi nhận Lambda Send chạy, email SNS xuất hiện trong hộp thư và DynamoDB/Frontend hiển thị trạng thái SENT.

| Bước | Kết quả | Minh chứng |
|---|---|---|
| Gửi POST từ website | Response chứa reminderId R-174123c996704e9d, trạng thái PENDING và scheduleName. | [POST response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A01-post-response.png), [POST headers](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A01b-post-headers.png) |
| Xác nhận PENDING | Frontend hiển thị lời nhắc mới; DynamoDB có item tương ứng. | [Frontend pending](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A02-frontend-pending.png), [DynamoDB pending](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A03-dynamodb-pending.png) |
| Xác nhận Scheduler | Schedule tồn tại trong group reminder-week2 và target là Lambda Send. | [Schedule created](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A04-scheduler-created.png), [Schedule target](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A04b-scheduler-target.png) |
| Xác nhận gửi | CloudWatch ghi nhận thực thi; email có cùng reminderId; DynamoDB và Frontend hiển thị SENT. | [Send CloudWatch](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A05-send-cloudwatch.png), [Send CloudWatch continued](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A05b-send-cloudwatch.png), [Email received](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A06-email-received.png), [DynamoDB sent](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A07-dynamodb-sent.png), [Frontend sent](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A08-frontend-sent.png) |

## Luồng B — Hủy lời nhắc đang chờ

Lời nhắc R-2a5437efc5fc4b2d được tạo ở trạng thái PENDING. Trước khi đến giờ gửi, thao tác Xóa được xác nhận trên website. Sau đó, ảnh DynamoDB không còn item và trang Scheduler không còn lịch trong danh sách.

| Bước | Kết quả | Minh chứng |
|---|---|---|
| Tạo lời nhắc | API trả reminderId R-2a5437efc5fc4b2d và PENDING. | [POST response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B01-post-response.png) |
| Xác nhận trạng thái trước xóa | Frontend, DynamoDB và Scheduler ghi nhận lời nhắc/lịch đang chờ. | [Frontend pending](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B02-frontend-pending.png), [DynamoDB before delete](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B03-dynamodb-before-delete.png), [Scheduler before delete](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B04-scheduler-before-delete.png) |
| Xác nhận xóa | Website hiển thị hộp thoại xác nhận xóa lời nhắc và hủy Scheduler nếu còn chờ. | [Delete confirmation](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B05-delete-confirm.png) |
| Xác nhận sau xóa | Lời nhắc không còn trên website; DynamoDB trả 0 items; danh sách Scheduler trả 0 schedules. | [Frontend after delete](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B07-frontend-after-delete.png), [DynamoDB after delete](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B08-dynamodb-after-delete.png), [Scheduler after delete](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B09-scheduler-after-delete.png) |

## Kết luận

Bộ minh chứng ghi nhận hai luồng độc lập: tạo và gửi email thành công; tạo rồi hủy lời nhắc trước thời điểm gửi, đồng thời kiểm tra trạng thái trên website, DynamoDB và Scheduler.
