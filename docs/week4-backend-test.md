# Kiểm thử Backend — Tuần 4

## Môi trường

- Region: us-east-1.
- HTTP API: reminder-http-api, API ID c3vvd6ghug.
- Bảng dữ liệu: Reminders, partition key reminderId.
- Các Lambda: reminder-create-api, reminder-get-api, reminder-delete-api và reminder-send.
- Execution role quan sát trong cấu hình Lambda: LabRole.

## Kết quả kiểm thử

| Mã | Hạng mục | Kết quả ghi nhận | Minh chứng |
|---|---|---|---|
| B01 | Cấu hình route API Gateway | Có POST /reminders, GET /reminders và DELETE /reminders/{id}; từng route được nối tới integration tương ứng. | [Routes](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-api-gateway-routes.png), [POST integration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/02-post-integration.png), [GET integration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/03-get-integration.png), [DELETE integration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/04-delete-integration.png) |
| B02 | Cấu hình DynamoDB | Bảng Reminders ở trạng thái Active, chế độ On-demand, partition key reminderId kiểu String. | [Bảng Reminders](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-dynamodb-table.png) |
| B03 | POST tạo lời nhắc | API trả thông báo tạo thành công, trạng thái PENDING và scheduleName cho lời nhắc kiểm thử. | [Items trước lượt tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/02-dynamodb-items-before.png), [POST response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/A01-post-response.png) |
| B04 | GET danh sách | Lambda GET dùng TABLE_NAME=Reminders và MAX_ITEMS=500; trình duyệt nhận response JSON của GET /reminders. | [Biến môi trường GET](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/get-01-environment-variables.png), [GET integration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/03-get-integration.png), [GET response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/02b-get-response.png) |
| B05 | DELETE lời nhắc đang chờ | Route DELETE được cấu hình; ảnh tích hợp ghi nhận xác nhận xóa và trạng thái sau xóa. | [Biến môi trường DELETE](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/delete-01-environment-variables.png), [DELETE integration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/04-delete-integration.png), [Xác nhận xóa](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/integration/B05-delete-confirm.png) |
| B06 | POST thiếu tiêu đề | API trả HTTP 400 với thông báo tiêu đề là bắt buộc và tối đa 200 ký tự. | [HTTP 400](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-01-400.png) |
| B07 | DELETE mã không tồn tại | API trả HTTP 404, thông báo không tìm thấy lời nhắc. | [HTTP 404](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-02-404.png) |
| B08 | DELETE khi lời nhắc đang gửi | API trả HTTP 409 và từ chối xóa trạng thái đang gửi. | [HTTP 409](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-03-409.png) |
| B09 | Quyền và biến môi trường Lambda | Ảnh ghi nhận cấu hình biến môi trường và execution role LabRole cho các Lambda. | [Create env](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/create-01-environment-variables.png), [Create permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/create-02-permissions-labrole.png), [GET permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/get-02-permissions-labrole.png), [DELETE permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/delete-02-permissions-labrole.png), [Send permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/send-02-permissions-labrole.png) |

## Kết luận

Các ảnh xác nhận cấu hình route, DynamoDB, biến môi trường, quyền Lambda và ba nhánh lỗi HTTP 400, 404, 409. Luồng POST/GET/DELETE được kiểm tra thêm trong [nhật ký tích hợp](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-integration-test.md).
