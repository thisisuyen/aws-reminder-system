# Giám sát hệ thống — Tuần 4

## CloudWatch metrics

Các ảnh ghi nhận metric của Lambda gồm Invocations, Errors, Duration và Throttles. Các metric này được đưa vào dashboard reminder-week4-dashboard để xem cùng một trang.

- [Invocations](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/01-lambda-metrics.png)
- [Errors](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/01b-lambda-errors.png)
- [Duration](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/01c-lambda-duration.png)
- [Throttles](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/01d-lambda-throttles.png)
- [Dashboard reminder-week4-dashboard](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/02-dashboard.png)

## Alarm cho lỗi Lambda Send

Alarm reminder-send-errors-week4 theo dõi metric Errors của Lambda reminder-send. Điều kiện hiển thị là Errors > 1 trong 1 datapoint của khoảng thời gian 1 phút; missing data được để là missing.

Ảnh alarm hiển thị trạng thái OK với một điểm Errors bằng 1, thấp hơn điều kiện > 1. Tài liệu này ghi nhận alarm đã cấu hình và trạng thái quan sát được; ảnh không thể hiện trạng thái ALARM.

- [Cấu hình alarm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03-alarm.png)
- [Lượt Lambda lỗi có kiểm soát](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/04-controlled-error.png)
- [Metric và trạng thái alarm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/05-alarm-triggered.png)

## Dữ liệu website S3

Các ảnh giám sát cũng ghi nhận cấu hình quyền public read trên bucket website tĩnh. Cấu hình này được mô tả thêm trong [rà soát bảo mật](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week4-security.md).

- [S3 permissions](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03-s3-permissions.png)
- [S3 bucket policy](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan4/monitoring/03b-s3-bucket-policy.png)
