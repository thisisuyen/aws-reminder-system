
# THIẾT KẾ CƠ SỞ DỮ LIỆU DYNAMODB

## 1. Mục đích

Sử dụng Amazon DynamoDB để lưu trữ
thông tin lời nhắc do người dùng tạo.

## 2. Thông tin bảng

- Table Name: Reminders
- Database: Amazon DynamoDB
- Region: us-east-1
- Partition Key: reminderId
- Partition Key Type: String
- Sort Key: Không sử dụng

## 3. Các thuộc tính

| Tên thuộc tính | Kiểu dữ liệu | Ý nghĩa |
|---|---|---|
| reminderId | String | Mã lời nhắc duy nhất |
| title | String | Tiêu đề lời nhắc |
| description | String | Nội dung lời nhắc |
| reminderTime | String | Thời gian nhắc |
| email | String | Email nhận thông báo |
| status | String | Trạng thái lời nhắc |
| scheduleName | String | Tên lịch EventBridge |
| createdAt | String | Thời gian tạo |

## 4. Ví dụ dữ liệu

```json
{
  "reminderId": "R001",
  "title": "Họp nhóm đồ án",
  "description": "Họp nhóm lúc 20 giờ",
  "reminderTime": "2026-10-25T19:45:00+07:00",
  "email": "nhom@example.com",
  "status": "PENDING",
  "scheduleName": "reminder-R001",
  "createdAt": "2026-10-14T09:00:00+07:00"
}
```

## 5. Quy tắc dữ liệu

- reminderId phải duy nhất.
- title không được để trống.
- reminderTime phải là thời gian hợp lệ.
- Thời gian nhắc phải ở tương lai.
- Thời gian sử dụng định dạng ISO 8601.
- email thuộc danh sách được phép nhận.
- scheduleName lưu tên lịch tương ứng.

## 6. Trạng thái lời nhắc

PENDING:
Thông báo đang chờ gửi.

SENT:
Thông báo đã được SNS chấp nhận.

## 7. Các thao tác dự kiến

- Thêm lời nhắc mới.
- Xem danh sách lời nhắc.
- Tìm lời nhắc bằng reminderId.
- Xóa lời nhắc.
- Cập nhật trạng thái.

## 8. Kế hoạch

Tuần 1:
Thiết kế cấu trúc dữ liệu.

Tuần 2:
Tạo bảng DynamoDB và lưu dữ liệu thử.

Tuần 3:
Tích hợp Lambda và EventBridge Scheduler.
