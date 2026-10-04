# Security Requirements

* Hàm `json_search` phải áp dụng kiểm soát truy cập dựa trên vai trò (RBAC). 
* Hệ thống chỉ trả về giá trị của khóa tìm kiếm nếu `role` truyền vào nằm trong danh sách được phép truy cập theo quy định (chẳng hạn `apiKey` chỉ dành cho `admin`).
* Nếu role không đủ quyền, hàm phải từ chối truy cập bằng cách trả về một danh sách rỗng.
