
# THIẾT KẾ REST API

## 1. Tổng quan

API được sử dụng để giao tiếp giữa
website và backend AWS Lambda.

Công nghệ:
- Amazon API Gateway
- AWS Lambda
- JSON
- HTTP

## 2. POST /reminders

Chức năng:
Tạo lời nhắc mới.

### Request

```json
{
  "title": "Họp nhóm đồ án",
  "description": "Họp nhóm lúc 20 giờ",
  "reminderTime": "2026-10-25T19:45:00+07:00",
  "email": "nhom@example.com"
}
```

### Response thành công đã triển khai

HTTP Status: 201

```json
{
  "message": "Reminder created",
  "reminderId": "R-a1b2c3d4e5f60708",
  "status": "PENDING",
  "scheduleName": "reminder-R-a1b2c3d4e5f60708",
  "scheduleArn": "<ARN do Scheduler trả về>"
}
```

### Xử lý đã triển khai

1. Nhận thông tin từ website.
2. Kiểm tra dữ liệu đầu vào.
3. Kiểm tra thời gian nhắc.
4. Sinh reminderId duy nhất.
5. Lưu thông tin vào DynamoDB.
6. Tạo EventBridge Schedule.
7. Trả kết quả về website.

Chỉ trả thành công khi quá trình tạo
lời nhắc và lịch tương ứng thành công.

## 3. GET /reminders

Chức năng:
Lấy danh sách lời nhắc.

### Response thành công đã triển khai

HTTP Status: 200

```json
{
  "items": [
    {
      "reminderId": "R-a1b2c3d4e5f60708",
      "title": "Họp nhóm đồ án",
      "description": "Họp nhóm lúc 20 giờ",
      "reminderTime": "2026-10-25T19:45:00+07:00",
      "email": "nhom@example.com",
      "status": "PENDING",
      "scheduleName": "reminder-R-a1b2c3d4e5f60708",
      "createdAt": "2026-10-24T18:00:00+07:00"
    }
  ],
  "count": 1,
  "truncated": false
}
```

`GET` đọc dữ liệu DynamoDB bằng Scan, sắp xếp theo `createdAt` và trả danh sách trong `items` (mặc định tối đa 500 mục).

## 4. DELETE /reminders/{id}

Chức năng:
Xóa lời nhắc theo ID.

Ví dụ:

DELETE /reminders/R-a1b2c3d4e5f60708

### Xử lý đã triển khai

1. Kiểm tra reminderId.
2. Tìm lời nhắc trong DynamoDB.
3. Xác định scheduleName.
4. Nếu `PENDING`, chuyển có điều kiện sang `CANCELLED` rồi hủy lịch EventBridge.
5. Nếu `SENDING`, trả `409` để tránh xung đột khi đang gửi.
6. Xóa item DynamoDB có điều kiện và trả kết quả.

### Response thành công đã triển khai

HTTP Status: 200

```json
{
  "message": "Reminder deleted",
  "reminderId": "R-a1b2c3d4e5f60708",
  "status": "DELETED"
}
```

## 5. Các mã HTTP

| Mã | Ý nghĩa |
|---|---|
| 200 | Thành công |
| 201 | Tạo thành công |
| 400 | Dữ liệu không hợp lệ |
| 404 | Không tìm thấy dữ liệu |
| 405 | Method không được hỗ trợ |
| 409 | Trạng thái xung đột khi xóa |
| 500 | Lỗi phía server |

## 6. Kế hoạch triển khai

Tuần 1:
Thiết kế các API.

Tuần 2:
Triển khai POST và các dịch vụ tạo/gửi lời nhắc.

Tuần 3:
Triển khai GET/DELETE, cập nhật `SENT` và tích hợp Frontend với API thật.

## 7. Minh chứng tuần 3

- [GET HTTP 200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/05-GET-http-response.png)
- [DELETE HTTP 200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/08b-DELETE-http-route-200.png)
- [Nhật ký kiểm thử tuần 3](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md)
