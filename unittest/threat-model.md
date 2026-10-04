# Threat Model cho json_search()

* **(a) Actor/Role:** Người dùng gọi hàm có thể mang các vai trò: `admin`, `operator`, và `viewer`.
* **(b) Asset:** Dữ liệu trả về có thể chứa các tài sản nhạy cảm như `apiKey` (chuỗi xác thực) hoặc `managementIpAddress`.
* **(c) Trust Boundary:** Trust boundary đang bị bỏ qua nếu hàm nhận yêu cầu truy xuất dữ liệu từ client nhưng không kiểm tra vai trò (role) của người gọi có hợp lệ với dữ liệu đó hay không trước khi trả về kết quả.
* **(d) Threat:** Thuộc nhóm rủi ro Information Disclosure (Tiết lộ thông tin). Kẻ tấn công mang role `viewer` có thể chủ động gọi hàm tìm kiếm key `apiKey` để đánh cắp khoá, từ đó dẫn đến rủi ro Elevation of Privilege (Leo thang đặc quyền).
