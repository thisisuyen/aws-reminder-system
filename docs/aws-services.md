# TỔNG HỢP CÁC DỊCH VỤ AWS

## 1\. Tổng quan

Dự án sử dụng kiến trúc AWS Serverless
để xây dựng hệ thống đặt lịch nhắc việc
và gửi thông báo qua Email.

Môi trường: AWS Learner Lab
Region: us-east-1

## 2\. Amazon S3

### Chức năng

Lưu trữ và cung cấp website tĩnh.

### Ứng dụng

Lưu các file HTML, CSS và JavaScript
của giao diện hệ thống.

Các file dự kiến:

* index.html
* style.css
* script.js

### Vai trò

Cung cấp giao diện cho người dùng.
Website gửi HTTP request đến API Gateway.

## 3\. Amazon API Gateway

### Chức năng

Tiếp nhận HTTP request từ frontend
và chuyển yêu cầu đến AWS Lambda.

### Các Route dự kiến

|Method|Endpoint|Chức năng|
|-|-|-|
|POST|/reminders|Tạo lời nhắc|
|GET|/reminders|Xem danh sách|
|DELETE|/reminders/{id}|Xóa lời nhắc|

### Vai trò

Kết nối website với Lambda API.

Loại API dự kiến: HTTP API.

## 4\. AWS Lambda

### Chức năng

Chạy mã xử lý khi có sự kiện.

### Lambda API

Tên: reminder-api-lambda

Nhiệm vụ:

* Nhận request từ API Gateway.
* Kiểm tra dữ liệu đầu vào.
* Lưu dữ liệu vào DynamoDB.
* Tạo lịch EventBridge Scheduler.

### Lambda Send

Tên: reminder-send-lambda

Nhiệm vụ:

* Nhận sự kiện từ Scheduler.
* Gửi thông báo đến Amazon SNS.
* Phối hợp cập nhật trạng thái lời nhắc.

## 5\. Amazon DynamoDB

### Chức năng

Lưu trữ dữ liệu lời nhắc dưới dạng NoSQL.

### Bảng dự kiến

Table: Reminders

Partition Key: reminderId

Các thuộc tính:

* reminderId
* title
* description
* reminderTime
* email
* status
* scheduleName
* createdAt

### Vai trò

Lưu và cung cấp dữ liệu cho
chức năng tạo, xem và xóa lời nhắc.

## 6\. EventBridge Scheduler

### Chức năng

Kích hoạt một tác vụ vào thời gian
được xác định trước.

### Cấu hình dự kiến

Schedule Type: One-time

Timezone: Asia/Ho\_Chi\_Minh

Flexible Time Window: OFF

Target: reminder-send-lambda

### Vai trò

Kích hoạt Lambda Send khi đến giờ nhắc.

Scheduler cần execution role hợp lệ
để gọi Lambda Send.

## 7\. Amazon SNS

### Chức năng

Phân phối thông báo qua mô hình
Publish/Subscribe.

### Các thành phần

Topic: Kênh tiếp nhận thông báo.

Subscription: Đối tượng đăng ký nhận.

Publish: Thao tác gửi thông báo.

### Cấu hình dự kiến

Topic: reminder-notification-topic

Protocol: Email

Email nhận phải xác nhận Subscription.

### Vai trò

Phân phối thông báo từ Lambda Send
đến Email đã xác nhận.

## 8\. Amazon CloudWatch

### Chức năng

Theo dõi hoạt động và hỗ trợ phát hiện lỗi.

### Nội dung theo dõi

* Log thực thi Lambda.
* Lỗi xử lý request.
* Kết quả gọi các dịch vụ AWS.

### Vai trò

Hỗ trợ kiểm tra và giám sát backend.

## 9\. AWS IAM

### Chức năng

Quản lý quyền truy cập dịch vụ AWS.

### Role dự kiến

LabRole trong AWS Learner Lab.

### Nhu cầu phân quyền

Lambda API:

* Đọc/ghi DynamoDB.
* Thao tác EventBridge Scheduler.
* Ghi CloudWatch Logs.

Lambda Send:

* Publish thông báo lên SNS.
* Ghi CloudWatch Logs.

EventBridge Scheduler:

* Sử dụng execution role hợp lệ.
* Kích hoạt Lambda Send.

Khả năng sử dụng LabRole cho Scheduler
cần được xác nhận bằng kiểm thử thực tế.

## 10\. Kiến trúc tích hợp

Người dùng
|
Website - S3
|
API Gateway
|
Lambda API
|
+----> DynamoDB
|
+----> EventBridge Scheduler
|
Lambda Send
|
SNS
|
Email

CloudWatch: Theo dõi log.

IAM: Quản lý quyền truy cập.

## 11\. Kết quả thiết kế tuần 1

* Xác định vai trò của 8 dịch vụ AWS.
* Xác định luồng kết nối các thành phần.
* Thống nhất định dạng dữ liệu API.
* Xác định phương án gửi Email qua SNS.
* Chuẩn bị cơ sở triển khai từ tuần 2.

