# Kiểm thử Frontend — Tuần 4

## Môi trường

- Website: http://aws-reminder-serverless-week3-demo.s3-website-us-east-1.amazonaws.com
- Bucket: aws-reminder-serverless-week3-demo.
- Các object website: [index.html](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html), [script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) và [style.css](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css).

## Kết quả kiểm thử

| Mã | Trường hợp | Kết quả ghi nhận | Minh chứng |
|---|---|---|---|
| F01 | Mở website S3 | Website tải được giao diện tạo và danh sách lời nhắc. | [Website live](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/01-website-live.png), [Static website hosting](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/04-s3-hosting.png) |
| F02 | Tải danh sách qua GET | Trình duyệt gửi GET /reminders và nhận dữ liệu JSON. | [GET Network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/02-get-network.png), [GET response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/02b-get-response.png) |
| F03 | Kiểm tra object website | Bucket có đủ ba file HTML, JavaScript và CSS. | [S3 objects](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/03-s3-objects.png) |
| F04 | Để trống tiêu đề | Trình duyệt chặn submit và yêu cầu nhập tiêu đề bắt buộc. | [Empty title](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-01-empty-title.png) |
| F05 | Chọn thời gian không hợp lệ | Giao diện báo cần chọn thời gian cách hiện tại hơn 2 phút. | [Invalid time](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-02-invalid-time.png) |
| F06 | API không truy cập được | Giao diện hiển thị Failed to fetch khi danh sách không tải được. | [Offline](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-03-offline.png) |
| F07 | Kết nối hoạt động lại | Sau khi kết nối được khôi phục, danh sách tải lại từ API GET. | [Recovered](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/frontend/error-04-recovered.png) |

## Kết luận

Bộ ảnh ghi nhận website tĩnh đang được phục vụ từ S3, request GET/response, kiểm tra dữ liệu biểu mẫu và phản hồi giao diện khi mạng lỗi rồi hoạt động lại.
