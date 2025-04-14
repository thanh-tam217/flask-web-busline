

document.addEventListener("DOMContentLoaded", function () {
    const pages = document.querySelectorAll(".page");
    const menuItems = document.querySelectorAll("#menu .items li a");

    function showPageFromHash() {
        const hash = location.hash.replace("#", "") || "benxe"; // Mặc định là "benxe"

        // Ẩn tất cả trang
        pages.forEach(page => page.classList.remove("active"));
        
        // Hiển thị trang tương ứng với hash
        const activePage = document.getElementById(hash);
        if (activePage) {
            activePage.classList.add("active");
        }

        // Cập nhật trạng thái active trong menu
        menuItems.forEach(item => {
            item.parentElement.classList.remove("active");
            if (item.getAttribute("href") === `#${hash}`) {
                item.parentElement.classList.add("active");
            }
        });
    }

    // Lắng nghe sự kiện thay đổi URL (hashchange)
    window.addEventListener("hashchange", showPageFromHash);

    // Áp dụng trạng thái active khi click vào menu
    menuItems.forEach((item) => {
        item.addEventListener("click", function () {
            // Xóa class active khỏi tất cả mục
            menuItems.forEach(i => i.parentElement.classList.remove("active"));

            // Thêm class active vào mục được click
            this.parentElement.classList.add("active");
        });
    });

    // Xử lý tải trang lần đầu
    showPageFromHash();
});

document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.querySelector(".items li:last-child a"); // Chọn phần tử "Đăng xuất"

    logoutButton.addEventListener("click", function (event) {
        event.preventDefault(); // Ngăn chặn hành động mặc định
        window.location.href = "index.html"; // Chuyển hướng về trang index.html
    });
});
// form add
// function openModal(modalId) {
//     document.getElementById(modalId).style.display = "flex";
// }

function openModal(id) {
    document.getElementById(id).style.display = "flex";
    loadTinhThanhOptions(); // gọi khi mở modal
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}


// HIển thị danh sách bến xe và tìm kiếm bến xe theo tên tỉnh
const apiBase = "http://127.0.0.1:5000/benxe"; // API của Flask

// Render dữ liệu ra bảng
function renderBenXeList(data) {
    const tbody = document.getElementById("benxe-table-body");
    tbody.innerHTML = ""; // Xoá dữ liệu cũ

    if (!data || data.length === 0) {
        tbody.innerHTML = "<tr><td colspan='4' class='text-center py-4 text-gray-500'>Không tìm thấy bến xe</td></tr>";
        return;
    }

    data.forEach(ben => {
        const row = `
        <tr class="border-b hover:bg-gray-100 transition" id="row-${ben.IDBen}">
            <td class="px-4 py-2">${ben.IDBen}</td>
            <td class="px-4 py-2">${ben.TenBen}</td>
            <td class="px-4 py-2">${ben.DiaChi}</td>
            <td class="px-4 py-2">${ben.SDTBen}</td>
            <td class="px-4 py-2">
                <div class="icon-actions">
                    <i class="bx bxs-edit-alt icon edit-icon" onclick="editBenXe('${ben.IDBen}')"></i>
                    <i class="bx bxs-trash icon delete-icon" onclick="deleteBenXe('${ben.IDBen}')"></i>
                </div>
            </td>
        </tr>`;
        tbody.innerHTML += row;
    });
}

// Load toàn bộ bến xe
async function loadAllBenXe() {
    try {
        const res = await fetch(apiBase);
        const data = await res.json();
        renderBenXeList(data);
    } catch (err) {
        console.error("Lỗi khi tải bến xe:", err);
    }
}

// Tìm kiếm theo ID hoặc tên
async function searchByTenTinh() {
    const keyword = document.getElementById("search-tinh").value.trim().toLowerCase();
    if (!keyword) return;

    let url = "";

    if (!isNaN(keyword)) {
        url = `${apiBase}/${keyword}`;
    } else {
        url = `http://127.0.0.1:5000/benxe/tinh/name/${encodeURIComponent(keyword)}`;
    }

    try {
        const res = await fetch(url);
        if (!res.ok) {
            renderBenXeList([]);
            return;
        }

        const data = await res.json();
        if (!Array.isArray(data)) {
            renderBenXeList([data]);
        } else {
            renderBenXeList(data);
        }
    } catch (err) {
        console.error("Lỗi khi tìm kiếm:", err);
    }
}

// Tải danh sách khi trang load
document.addEventListener("DOMContentLoaded", loadAllBenXe);

// --------------------------------------------------------------------------------
// Form add bến xe
async function loadTinhThanhOptions() {
    const select = document.getElementById("tinhThanhSelect");
    select.innerHTML = `<option value="">Chọn tỉnh/thành phố</option>`;
    try {
        const res = await fetch("http://127.0.0.1:5000/tinhthanh");
        const data = await res.json();

        data.forEach(tinh => {
            const option = document.createElement("option");
            option.value = tinh.IDTinh;
            option.textContent = tinh.TenTinh;
            select.appendChild(option);
        });
    } catch (err) {
        console.error("Lỗi khi tải tỉnh thành:", err);
    }
}
// Gán IDTinh vào input hidden khi chọn tỉnh
document.getElementById("tinhThanhSelect").addEventListener("change", function () {
    document.getElementById("idTinhHidden").value = this.value;
});



// // Lấy ID tỉnh khi người dùng chọn tỉnh
// document.getElementById("tinhThanhSelect").addEventListener("change", async function () {
//     const tenTinh = this.value;
//     const hiddenInput = document.getElementById("idTinhHidden");

//     if (!tenTinh) {
//         hiddenInput.value = "";
//         return;
//     }

//     try {
//         const res = await fetch(`http://127.0.0.1:5000/tinhthanh/name/${encodeURIComponent(tenTinh)}`);
//         const data = await res.json();
//         hiddenInput.value = data.IDTinh || ""; // lưu IDTinh vào input hidden
//     } catch (err) {
//         console.error("Lỗi lấy ID tỉnh:", err);
//     }
// });


// sự kiện bấm nút lưu
document.getElementById('formBenXe').addEventListener('submit', async function (e) {
    e.preventDefault();

    const benXe = {
        IDBen: document.getElementById('idBen').value.trim(),
        TenBen: document.getElementById('tenBen').value.trim(),
        DiaChi: document.getElementById('diaChi').value.trim(),
        SDTBen: document.getElementById('soDienThoai').value.trim(),
        IDTinh: document.getElementById('idTinhHidden').value.trim()
    };

    console.log("Dữ liệu gửi:", benXe);

    try {
        const res = await fetch("http://127.0.0.1:5000/benxe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(benXe)
        });

        const result = await res.json();
        if (res.ok) {
            alert("Thêm thành công!");
            closeModal('modalBenXe');
            this.reset();
        } else {
            alert("Lỗi: " + result.error);
        }
    } catch (err) {
        console.error("Lỗi khi gửi dữ liệu:", err);
    }
});

// ---------------------------------------
// Hàm load tỉnh thành
// form chỉnh sửa bến xe
document.getElementById("formBenXeEdit").addEventListener("submit", function (e) {
    e.preventDefault();
    const idBen = document.getElementById("idBenEdit").value;
    const benXeData = {
        TenBen: document.getElementById("tenBenEdit").value,
        DiaChi: document.getElementById("diaChiEdit").value,
        SDTBen: document.getElementById("soDienThoaiEdit").value,
        IDTinh: document.getElementById("tinhThanhSelectEdit").value,
    };

    fetch(`/benxe/${idBen}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(benXeData),
    })
    .then(res => res.json())
    .then(data => {
        alert("Cập nhật bến xe thành công");
        closeModal("modalBenXeEdit");
        loadAllBenXe();  // Tải lại danh sách bến xe
    })
    .catch(err => {
        console.error("Lỗi khi cập nhật bến xe:", err);
        alert("Cập nhật không thành công");
    });
});

// ---------------------------------------
// Hàm load tỉnh thành cho form chỉnh sửa
async function loadTinhThanhOptionsEdit(selectedID = "") {
    const select = document.getElementById("tinhThanhSelectEdit");
    select.innerHTML = `<option value="">Chọn tỉnh/thành phố</option>`;  // Reset lại list options
    try {
        const res = await fetch("http://127.0.0.1:5000/tinhthanh");
        const data = await res.json();

        data.forEach(tinh => {
            const option = document.createElement("option");
            option.value = tinh.IDTinh;
            option.textContent = tinh.TenTinh;
            if (tinh.IDTinh === selectedID) {
                option.selected = true;  // Chọn tỉnh thành hiện tại
            }
            select.appendChild(option);
        });
    } catch (err) {
        console.error("Lỗi khi tải tỉnh thành (Edit):", err);
    }
}

// Chức năng chỉnh sửa bến xe
function editBenXe(idBen) {
    fetch(`/benxe/${idBen}`)
        .then(res => res.json())
        .then(data => {
            // Điền dữ liệu vào form chỉnh sửa
            document.getElementById("idBenEdit").value = data.IDBen;
            document.getElementById("tenBenEdit").value = data.TenBen;
            document.getElementById("diaChiEdit").value = data.DiaChi;
            document.getElementById("soDienThoaiEdit").value = data.SDTBen;

            // Gọi hàm load tỉnh thành và chọn đúng tỉnh
            loadTinhThanhOptionsEdit(data.IDTinh);

            // Mở modal chỉnh sửa
            openModal("modalBenXeEdit");
        })
        .catch(err => {
            console.error("Lỗi khi lấy thông tin bến xe:", err);
        });
}



// Chức năng xóa bến xe
function deleteBenXe(id_ben) {
    const url = `/benxe/${id_ben}`;

    fetch(url, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        alert("Xóa bến xe thành công");
        const row = document.getElementById(`row-${id_ben}`);
        if (row) row.remove(); // Xoá hàng khỏi bảng
    })
    .catch((error) => {
        alert("Lỗi khi xóa bến xe");
        console.error(error);
    });
}

// -------------------------------------------------------
// ------------- Quản lý tỉnh thành

// Gọi API để lấy danh sách tỉnh thành và hiển thị vào bảng
function loadAllTinhThanh() {
    fetch('http://127.0.0.1:5000/tinhthanh')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('tinhthanh-table-body');
            tableBody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.IDTinh}</td>
                    <td>${item.TenTinh}</td>
                    <td class="px-4 py-2">
                        <div class="icon-actions">
                            <i class="bx bxs-edit-alt icon edit-icon" onclick="editTinhThanh('${item.IDTinh}')"></i>
                            <i class="bx bxs-trash icon delete-icon" onclick="deleteBenXe('${item.TenTinh}')"></i>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Lỗi khi tải tỉnh thành:', error));
}

// Hàm hiển thị dữ liệu lên form sửa
function showEditTinhThanh(id, name) {
    document.getElementById('idTinhEdit').value = id;
    document.getElementById('tenTinhEdit').value = name;
    openModal('modalTinhThanhEdit');
}

// Hàm xóa tỉnh thành
function deleteTinhThanh(id) {
    if (confirm("Bạn có chắc muốn xóa tỉnh thành này?")) {
        fetch(`http://127.0.0.1:5000/tinhthanh/${id}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            loadAllTinhThanh();
        })
        .catch(error => console.error('Lỗi khi xóa:', error));
    }
}

// Gọi khi load trang
document.addEventListener('DOMContentLoaded', loadAllTinhThanh);

function searchTinhThanh() {
    const keyword = document.getElementById('search-tinhthanh').value.trim().toLowerCase();

    fetch('http://127.0.0.1:5000/tinhthanh')
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(item => 
                item.TenTinh.toLowerCase().includes(keyword)
            );

            const tableBody = document.getElementById('tinhthanh-table-body');
            tableBody.innerHTML = '';

            filtered.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.IDTinh}</td>
                    <td>${item.TenTinh}</td>
                    <td class="px-4 py-2">
                        <div class="icon-actions">
                            <i class="bx bxs-edit-alt icon edit-icon" onclick="editTinhThanh('${item.IDTinh}')"></i>
                            <i class="bx bxs-trash icon delete-icon" onclick="deleteBenXe('${item.TenTinh}')"></i>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Lỗi khi tìm kiếm:', error));
}

