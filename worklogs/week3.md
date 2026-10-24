# NHẬT KÝ CÔNG VIỆC TUẦN 3

<div align="center">

**ĐỒ ÁN ĐIỆN TOÁN ĐÁM MÂY**  
**HỆ THỐNG ĐẶT LỊCH NHẮC VIỆC QUA EMAIL VỚI EVENTBRIDGE SCHEDULER VÀ AMAZON SNS**

**Giảng viên hướng dẫn:** Huỳnh Xuân Phụng  
**Nhóm:** Serverless  
**Môi trường:** AWS Academy Learner Lab — `us-east-1`  
**Giai đoạn:** Tuần 3 – Hoàn thiện GET/DELETE, đồng bộ SENT, triển khai S3 và kiểm thử toàn hệ thống

</div>

| Mã số sinh viên | Họ và tên | Vai trò | Thời lượng |
|:---:|---|---|:---:|
| **24110379** | **Nguyễn Thanh Vân** | Backend & AWS / kiểm thử tích hợp | **10 giờ** |
| **24110378** | **Trần Thu Uyên** | Frontend & AWS Integration / S3 | **9 giờ** |

---

## 1. NHẬT KÝ CÔNG VIỆC — NGUYỄN THANH VÂN (24110379)

**Phạm vi thực hiện:** 05 nhiệm vụ, tổng thời lượng **10 giờ**. Triển khai Backend và các dịch vụ AWS tại `us-east-1`.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm trên GitHub | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Triển khai GET lấy danh sách lời nhắc | 2 giờ | Tạo Lambda `reminder-get-api`, đọc bảng `Reminders`, trả JSON `items`, `count`; gắn `GET /reminders` trong HTTP API Gateway và thử qua endpoint. | [get_reminders.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/get_reminders.py) · [03-Lambda-GET-test-200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/03-Lambda-GET-test-200.png) · [05-GET-http-response](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/05-GET-http-response.png) | Hoàn thành |
| 2 | Triển khai DELETE và hủy lịch | 2 giờ | Tạo Lambda `reminder-delete-api`; xử lý lời nhắc `PENDING`, hủy Schedule thuộc group `reminder-week2`, xóa item trong DynamoDB; cấu hình `DELETE /reminders/{id}` và kiểm thử. | [delete_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/delete_reminder.py) · [08b-DELETE-http-route-200](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/08b-DELETE-http-route-200.png) · [09-DELETE-DynamoDB-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/09-DELETE-DynamoDB-after.png) · [10-DELETE-Scheduler-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/10-DELETE-Scheduler-after.png) | Hoàn thành |
| 3 | Nâng cấp Lambda Send, đồng bộ SENT | 2 giờ | Nâng cấp `reminder-send`: nhận lịch từ Scheduler, xử lý `PENDING → SENDING → SENT`, Publish SNS, lưu `sentAt` và `snsMessageId`; kiểm tra CloudWatch và tránh gửi lặp. | [send_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/send_reminder.py) · [13-SEND-Lambda-success](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/13-SEND-Lambda-success.png) · [14-SEND-after-SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/14-SEND-after-SENT.png) · [15-SEND-cloudwatch](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/15-SEND-cloudwatch.png) | Hoàn thành |
| 4 | Hoàn thiện AWS Gateway, quyền và cấu hình | 2 giờ | Rà soát GET/POST/DELETE routes, Integration, CORS, Lambda Environment Variables, tags của hai Lambda mới; dùng AWS chính để phối hợp hosting S3 và Origin tương ứng. | [16-APIGateway-routes-CORS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/16-APIGateway-routes-CORS.png) · [02c-Lambda-GET-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/02c-Lambda-GET-tags.png) · [06c-Lambda-DELETE-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/06c-Lambda-DELETE-tags.png) | Hoàn thành |
| 5 | Kiểm thử tích hợp và tổng hợp minh chứng | 2 giờ | Đối chiếu lời nhắc gửi email ID-A giữa API, SNS và DynamoDB SENT; phối hợp kiểm thử hủy ID-B và ghi nhận DynamoDB không còn bản ghi; tổng hợp ảnh/backend, integration và nhật ký test. | [03b-EndToEnd-SEND-cloudwatch](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03b-EndToEnd-SEND-cloudwatch.png) · [04b-EndToEnd-SENT-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/04b-EndToEnd-SENT-DynamoDB.png) · [06b-DELETE-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06b-DELETE-DynamoDB.png) · [week3-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md) | Hoàn thành |
| | **Tổng** | **10 giờ** | **05/05 nhiệm vụ hoàn thành** | **03 file Python, cấu hình AWS và minh chứng Backend/tích hợp** | **Hoàn thành** |

**Kết quả đóng góp:** Hoàn thiện API GET/DELETE, trạng thái SNS `SENT` trong DynamoDB và cơ sở kiểm thử trên AWS chính. Những tài nguyên được tạo từ tuần 2 (`Reminders`, `reminder-create-api`, `reminder-send`, `reminder-http-api`, SNS Topic, Scheduler Group) được tiếp tục sử dụng, không tạo hệ thống độc lập mới.

---

## 2. NHẬT KÝ CÔNG VIỆC — TRẦN THU UYÊN (24110378)

**Phạm vi thực hiện:** 05 nhiệm vụ, tổng thời lượng **9 giờ**. Phát triển Frontend, kết nối API Gateway và phối hợp triển khai website trên Amazon S3.

| STT | Công việc | Thời lượng | Nội dung đã thực hiện | Kết quả / sản phẩm trên GitHub | Trạng thái |
|:---:|---|:---:|---|---|:---:|
| 1 | Kết nối GET và tải lại dữ liệu | 2 giờ | Cập nhật `index.html`, `script.js` để gọi API GET thật, hiển thị danh sách từ DynamoDB và tải lại sau khi F5/Làm mới. | [index.html](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) · [script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) · [01-Frontend-GET-list](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/01-Frontend-GET-list.png) · [02-Frontend-refresh-persist](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/02-Frontend-refresh-persist.png) | Hoàn thành |
| 2 | Giao diện Hủy/Xóa lời nhắc | 2 giờ | Bổ sung xác nhận thao tác và gọi `DELETE /reminders/{id}`; nhận kết quả API, sau đó gọi GET để kiểm tra lời nhắc đã biến mất. | [03-Frontend-cancel-confirm](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/03-Frontend-cancel-confirm.png) · [04-Frontend-delete-result](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/04-Frontend-delete-result.png) · [04b-Frontend-DELETE-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/04b-Frontend-DELETE-network.png) | Hoàn thành |
| 3 | Hiển thị trạng thái và xử lý thông báo | 1 giờ | Hiển thị `PENDING`, `SENDING`, `SENT`, `SEND_FAILED` và các trạng thái khác từ API; hiển thị lỗi khi request thất bại, không giả lập kết quả SEND. | [script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) · [style.css](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css) · [05-Frontend-SENT-status](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/frontend/05-Frontend-SENT-status.png) | Hoàn thành |
| 4 | Triển khai website tĩnh trên S3 | 2 giờ | Chuẩn bị và bàn giao 3 file Frontend; phối hợp tạo Bucket, tags tuần 3, upload đối tượng, bật Static Website Hosting và kiểm tra gọi GET từ S3 Website Endpoint trên AWS chính. | [01-S3-bucket-tags](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/01-S3-bucket-tags.png) · [02-S3-objects](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/02-S3-objects.png) · [03-S3-hosting-endpoint](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/03-S3-hosting-endpoint.png) · [04-S3-website-live](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04-S3-website-live.png) · [04b-S3-GET-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04b-S3-GET-network.png) | Hoàn thành |
| 5 | Kiểm thử và tổng hợp minh chứng Frontend | 2 giờ | Kiểm thử POST/GET/SENT/DELETE qua website S3; so mã lời nhắc thật với email SNS và phản hồi API, lưu ảnh theo cấu trúc GitHub, đóng góp nhật ký tích hợp. | [01-EndToEnd-POST](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/01-EndToEnd-POST.png) · [03-EndToEnd-SNS-email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03-EndToEnd-SNS-email.png) · [04-EndToEnd-SENT](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/04-EndToEnd-SENT.png) · [06-EndToEnd-DELETE-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06-EndToEnd-DELETE-after.png) · [week3-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md) | Hoàn thành |
| | **Tổng** | **9 giờ** | **05/05 nhiệm vụ hoàn thành** | **03 file Frontend, website S3 và minh chứng Frontend/tích hợp** | **Hoàn thành** |

**Kết quả đóng góp:** Frontend tuần 3 sử dụng API Gateway để tạo, xem, hủy và theo dõi trạng thái lời nhắc. Giao diện đã được triển khai trên Amazon S3; hai thành viên phối hợp kiểm thử tích hợp và tổng hợp minh chứng.

---

## 3. PHỐI HỢP NHÓM VÀ KIỂM THỬ TÍCH HỢP

**Phân công phối hợp:** Vân phụ trách Backend và cấu hình AWS chính; Uyên phụ trách Frontend và kiểm thử giao diện. Hai thành viên phối hợp triển khai website S3 và kiểm thử tích hợp trên cùng hệ thống tại `us-east-1`.

| Nội dung phối hợp | Kết quả thực hiện và đối chiếu |
|---|---|
| Cấu hình API chính | Frontend trỏ tới `https://c3vvd6ghug.execute-api.us-east-1.amazonaws.com`. API gồm POST/GET/DELETE. [16-APIGateway-routes-CORS](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/16-APIGateway-routes-CORS.png) |
| Chia sẻ AWS chính và S3 | Website S3 thuộc hệ thống AWS chính; Endpoint `http://aws-reminder-serverless-week3-demo.s3-website-us-east-1.amazonaws.com`. [04-S3-website-live](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/s3/04-S3-website-live.png) |
| Luồng ID-A (gửi email) | `R-341298481ae543bb`: POST tạo `PENDING`, email SNS có cùng mã; DynamoDB cập nhật `SENT`. [01b-EndToEnd-POST-network](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/01b-EndToEnd-POST-network.png) · [03-EndToEnd-SNS-email](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/03-EndToEnd-SNS-email.png) · [04b-EndToEnd-SENT-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/04b-EndToEnd-SENT-DynamoDB.png) |
| Luồng ID-B (hủy) | `R-1796c15305bd4563`: DynamoDB có `PENDING` trước khi hủy và không còn item sau kiểm thử DELETE. Minh chứng xóa Scheduler ở bài thử Backend độc lập. [05-EndToEnd-DELETE-before](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/05-EndToEnd-DELETE-before.png) · [06b-DELETE-DynamoDB](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/integration/06b-DELETE-DynamoDB.png) · [10-DELETE-Scheduler-after](https://github.com/thisisuyen/aws-reminder-system/blob/main/minhchung/tuan3/backend/10-DELETE-Scheduler-after.png) |
| Khác biệt giữa trạng thái SENT và nhận email | `SENT` ghi nhận SNS đã chấp nhận Publish và DynamoDB được cập nhật; email thực nhận được chứng minh bằng ảnh hộp thư riêng. |
| Nhật ký kiểm thử | Thông tin từng bài thử, minh chứng và các giới hạn được lập tại [docs/week3-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md). |

---

## 4. TỔNG HỢP KẾT QUẢ TUẦN 3

| Thành viên | Nhiệm vụ hoàn thành | Thời lượng | Sản phẩm |
|---|:---:|:---:|---|
| **Nguyễn Thanh Vân (24110379)** | **5/5** | **10 giờ** | 03 file Python Backend, cấu hình GET/DELETE/SENT và các ảnh AWS |
| **Trần Thu Uyên (24110378)** | **5/5** | **9 giờ** | 03 file Frontend, website S3 và ảnh kiểm thử |
| **Toàn nhóm** | **10/10** | **19 giờ** | Backend, Frontend, S3, kiểm thử tích hợp và tài liệu tuần 3 |

### 4.1. Các file và thư mục sản phẩm

| Nội dung | Liên kết GitHub |
|---|---|
| Lambda GET | [backend/get_reminders.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/get_reminders.py) |
| Lambda DELETE | [backend/delete_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/delete_reminder.py) |
| Lambda Send | [backend/send_reminder.py](https://github.com/thisisuyen/aws-reminder-system/blob/main/backend/send_reminder.py) |
| Frontend HTML | [frontend/index.html](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/index.html) |
| Frontend CSS | [frontend/style.css](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/style.css) |
| Frontend JavaScript | [frontend/script.js](https://github.com/thisisuyen/aws-reminder-system/blob/main/frontend/script.js) |
| Nhật ký kiểm thử | [docs/week3-test.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/docs/week3-test.md) |
| Worklog tuần 3 | [worklogs/week3.md](https://github.com/thisisuyen/aws-reminder-system/blob/main/worklogs/week3.md) |

---

## 5. KẾT LUẬN

Trong tuần 3, nhóm hoàn thành 10/10 nhiệm vụ với tổng thời lượng 19 giờ. Hệ thống đã triển khai API GET/DELETE, cập nhật trạng thái `SENT` sau khi SNS chấp nhận Publish, hoàn thiện giao diện Frontend và triển khai website tĩnh trên Amazon S3. Kết quả kiểm thử tích hợp xác nhận luồng tạo và gửi lời nhắc qua email, đồng thời kiểm tra chức năng hủy lời nhắc và xóa bản ghi trên DynamoDB. Mã nguồn, nhật ký kiểm thử và các ảnh minh chứng được lưu trong repository của nhóm.

