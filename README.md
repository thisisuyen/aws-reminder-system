AWS REMINDER SYSTEM
1. Giới thiệu
Hệ thống đặt lịch nhắc việc qua Email sử dụng
kiến trúc AWS Serverless.
Hệ thống cho phép người dùng tạo lời nhắc,
xem danh sách và xóa lời nhắc.
Thông báo được gửi tự động qua Email
tại thời điểm đã thiết lập.
2. Công nghệ sử dụng
Amazon S3
Amazon API Gateway
AWS Lambda
Amazon DynamoDB
Amazon EventBridge Scheduler
Amazon SNS
Amazon CloudWatch
AWS IAM
3. Kiến trúc
```text
Website (S3)
    |
API Gateway
    |
Lambda API
    |
DynamoDB + EventBridge Scheduler
                 |
             Lambda Send
                 |
                SNS
                 |
               Email
```
4. Chức năng dự kiến
Tạo lời nhắc.
Xem danh sách lời nhắc.
Xóa lời nhắc.
Gửi Email nhắc việc tự động.
5. Thành viên
24110379 - Nguyễn Thanh Vân
Backend & AWS
Lambda API
DynamoDB
EventBridge Scheduler
Thiết kế database
Thiết kế API
Kiến trúc AWS
24110378 - Trần Thu Uyên
Frontend & AWS Integration
Giao diện HTML/CSS
API Gateway
Amazon SNS
Amazon S3
CloudWatch và IAM
GitHub và tài liệu AWS
6. Kế hoạch
Tuần 1:
Nghiên cứu và thiết kế hệ thống.
Tuần 2:
Triển khai từng dịch vụ AWS.
Tuần 3:
Tích hợp hệ thống và gửi Email tự động.
Tuần 4:
Kiểm thử và hoàn thiện báo cáo.
7. Cấu trúc dự án
docs/: Tài liệu thiết kế
frontend/: Giao diện website
worklogs/: Nhật ký công việc
minhchung/: Minh chứng thực hiện
8. Môi trường
AWS Learner Lab
AWS Region: us-east-1
9. Trạng thái
Tuần 1: Giai đoạn thiết kế.
Chức năng gửi Email tự động sẽ được
triển khai trong các tuần tiếp theo.
