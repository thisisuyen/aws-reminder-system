
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
| email | String | Email nhập khi tạo; việc gửi phụ thuộc SNS Subscription đã xác nhận |
| status | String | Trạng thái lời nhắc |
| scheduleName | String | Tên lịch EventBridge |
| createdAt | String | Thời gian tạo |
| sentAt | String | Thời điểm SNS chấp nhận Publish và Lambda ghi `SENT` |
| snsMessageId | String | Mã MessageId do SNS trả về |
| cancelledAt | String | Thời điểm đánh dấu hủy trước khi xóa lịch |

## 4. Ví dụ dữ liệu

```json
{
  "reminderId": "R-a1b2c3d4e5f60708",
  "title": "Họp nhóm đồ án",
  "description": "Họp nhóm lúc 20 giờ",
  "reminderTime": "2026-10-25T19:45:00+07:00",
  "email": "nhom@example.com",
  "status": "PENDING",
  "scheduleName": "reminder-R-a1b2c3d4e5f60708",
  "createdAt": "2026-10-14T09:00:00+07:00"
}
```

## 5. Quy tắc dữ liệu

- reminderId phải duy nhất.
- title không được để trống.
- reminderTime phải là thời gian hợp lệ.
- Thời gian nhắc phải ở tương lai.
- Thời gian sử dụng định dạng ISO 8601.
- email có định dạng hợp lệ; SNS gửi tới Subscription đã xác nhận.
- scheduleName lưu tên lịch tương ứng.

## 6. Trạng thái lời nhắc

PENDING:
Thông báo đang chờ gửi.

SENDING:
Lambda Send đang xử lý gửi; không cho xóa để tránh xung đột.

SENT:
Thông báo đã được SNS chấp nhận (chưa khẳng định email đã vào Inbox).

CANCELLED:
Trạng thái tạm khi hủy lời nhắc `PENDING` trước khi xóa lịch và item.

SEND_FAILED:
Gửi lên SNS thất bại.

SCHEDULE_FAILED:
Lưu DynamoDB thành công nhưng tạo lịch Scheduler thất bại.

## 7. Các thao tác đã triển khai

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
Triển khai GET/DELETE, cập nhật `SENT` qua Lambda Send và bổ sung `sentAt`, `snsMessageId`, `cancelledAt`.

Minh chứng: [Trạng thái SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/14-SEND-after-SENT.png) · [DynamoDB sau DELETE](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/09-DELETE-DynamoDB-after.png).
