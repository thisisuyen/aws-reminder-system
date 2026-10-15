
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

### Response thành công dự kiến

HTTP Status: 201

```json
{
  "message": "Reminder created",
  "reminderId": "R001",
  "status": "PENDING"
}
```

### Xử lý dự kiến

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

### Response thành công dự kiến

HTTP Status: 200

```json
{
  "reminders": [
    {
      "reminderId": "R001",
      "title": "Họp nhóm đồ án",
      "reminderTime": "2026-10-25T19:45:00+07:00",
      "status": "PENDING"
    }
  ]
}
```

## 4. DELETE /reminders/{id}

Chức năng:
Xóa lời nhắc theo ID.

Ví dụ:

DELETE /reminders/R001

### Xử lý dự kiến

1. Kiểm tra reminderId.
2. Tìm lời nhắc trong DynamoDB.
3. Xác định scheduleName.
4. Xóa lịch EventBridge nếu còn tồn tại.
5. Xóa dữ liệu DynamoDB.
6. Trả kết quả.

### Response thành công dự kiến

HTTP Status: 200

```json
{
  "message": "Reminder deleted",
  "reminderId": "R001"
}
```

## 5. Các mã HTTP

| Mã | Ý nghĩa |
|---|---|
| 200 | Thành công |
| 201 | Tạo thành công |
| 400 | Dữ liệu không hợp lệ |
| 404 | Không tìm thấy dữ liệu |
| 500 | Lỗi phía server |

## 6. Kế hoạch triển khai

Tuần 1:
Thiết kế các API.

Tuần 2:
Triển khai POST và GET.

Tuần 3:
Hoàn thiện DELETE và tích hợp Scheduler.
