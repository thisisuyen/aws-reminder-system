# Rà soát bảo mật — Tuần 4

## API Gateway và CORS

API reminder-http-api có các route POST /reminders, GET /reminders và DELETE /reminders/{id}. Ảnh cấu hình route cho thấy chưa gắn authorizer; các route này không yêu cầu xác thực người dùng trong cấu hình được chụp.

CORS được cấu hình cho website S3 cùng hai origin localhost phục vụ phát triển. Các method được cho phép là GET, POST, DELETE và OPTIONS; header được cho phép là content-type; credentials tắt.

- [Routes và authorization](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/01-api-gateway-routes.png)
- [CORS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/security/03-api-cors.png)

CORS kiểm soát request từ trình duyệt, không thay thế xác thực hoặc phân quyền API.

## Quyền Lambda

Ảnh cấu hình ghi nhận các Lambda dùng LabRole trong môi trường AWS Learner Lab. Bảng cấu hình của Lambda Create trỏ tới DynamoDB Reminders, Scheduler group reminder-week2 và Lambda Send. Các biến môi trường và quyền được đối chiếu trực tiếp qua ảnh cấu hình bên dưới.

- [Create permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/create-02-permissions-labrole.png)
- [GET permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/get-02-permissions-labrole.png)
- [DELETE permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/delete-02-permissions-labrole.png)
- [Send permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/send-02-permissions-labrole.png)

## Website S3

Bucket aws-reminder-serverless-week3-demo bật Static Website Hosting. Bucket policy cho phép s3:GetObject với Principal * trên các object của bucket để trình duyệt tải file website.

- [Static website hosting](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/04-s3-hosting.png)
- [S3 bucket permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03-s3-permissions.png)
- [Bucket policy](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03b-s3-bucket-policy.png)

Bucket này chỉ nên chứa nội dung tĩnh công khai; không đặt khóa, thông tin đăng nhập hoặc dữ liệu riêng tư trong các file được phục vụ công khai.

## Kiểm tra xử lý lỗi

Các phản hồi HTTP đã ghi nhận:

- 400 khi thiếu title.
- 404 khi reminderId không tồn tại.
- 409 khi lời nhắc đang ở trạng thái sending và không thể xóa.

Minh chứng: [400](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-01-400.png) · [404](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-02-404.png) · [409](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/backend/error-03-409.png).
