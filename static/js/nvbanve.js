

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


// // HIển thị danh sách bến xe và tìm kiếm bến xe theo tên tỉnh
// const apiBase = "http://127.0.0.1:5000/benxe"; // API của Flask

// // Render dữ liệu ra bảng
// function renderBenXeList(data) {
//     const tbody = document.getElementById("benxe-table-body");
//     tbody.innerHTML = ""; // Xoá dữ liệu cũ

//     if (!data || data.length === 0) {
//         tbody.innerHTML = "<tr><td colspan='4' class='text-center py-4 text-gray-500'>Không tìm thấy bến xe</td></tr>";
//         return;
//     }

//     data.forEach(ben => {
//         const row = `
//         <tr class="border-b hover:bg-gray-100 transition" id="row-${ben.IDBen}">
//             <td class="px-4 py-2">${ben.IDBen}</td>
//             <td class="px-4 py-2">${ben.TenBen}</td>
//             <td class="px-4 py-2">${ben.DiaChi}</td>
//             <td class="px-4 py-2">${ben.SDTBen}</td>
//             <td class="px-4 py-2">
//                 <div class="icon-actions">
//                     <i class="bx bxs-edit-alt icon edit-icon" onclick="editBenXe('${ben.IDBen}')"></i>
//                     <i class="bx bxs-trash icon delete-icon" onclick="deleteBenXe('${ben.IDBen}')"></i>
//                 </div>
//             </td>
//         </tr>`;
//         tbody.innerHTML += row;
//     });
// }

// // Load toàn bộ bến xe
// async function loadAllBenXe() {
//     try {
//         const res = await fetch(apiBase);
//         const data = await res.json();
//         renderBenXeList(data);
//     } catch (err) {
//         console.error("Lỗi khi tải bến xe:", err);
//     }
// }

// // Tìm kiếm theo tên
// async function searchByTenTinh() {
//     const keyword = document.getElementById("search-tinh").value.trim().toLowerCase();
//     if (!keyword) return;

//     let url = "";

//     if (!isNaN(keyword)) {
//         url = `${apiBase}/${keyword}`;
//     } else {
//         url = `http://127.0.0.1:5000/benxe/tinh/name/${encodeURIComponent(keyword)}`;
//     }

//     try {
//         const res = await fetch(url);
//         if (!res.ok) {
//             renderBenXeList([]);
//             return;
//         }

//         const data = await res.json();
//         if (!Array.isArray(data)) {
//             renderBenXeList([data]);
//         } else {
//             renderBenXeList(data);
//         }
//     } catch (err) {
//         console.error("Lỗi khi tìm kiếm:", err);
//     }
// }

// // Tải danh sách khi trang load
// document.addEventListener("DOMContentLoaded", loadAllBenXe);

// // --------------------------------------------------------------------------------
// // Form add bến xe
// async function loadTinhThanhOptions() {
//     const select = document.getElementById("tinhThanhSelect");
//     select.innerHTML = `<option value="">Chọn tỉnh/thành phố</option>`;
//     try {
//         const res = await fetch("http://127.0.0.1:5000/tinhthanh");
//         const data = await res.json();

//         data.forEach(tinh => {
//             const option = document.createElement("option");
//             option.value = tinh.IDTinh;
//             option.textContent = tinh.TenTinh;
//             select.appendChild(option);
//         });
//     } catch (err) {
//         console.error("Lỗi khi tải tỉnh thành:", err);
//     }
// }
// // Gán IDTinh vào input hidden khi chọn tỉnh
// document.getElementById("tinhThanhSelect").addEventListener("change", function () {
//     document.getElementById("idTinhHidden").value = this.value;
// });

// // sự kiện bấm nút lưu
// document.getElementById('formBenXe').addEventListener('submit', async function (e) {
//     e.preventDefault();

//     const benXe = {
//         IDBen: document.getElementById('idBen').value.trim(),
//         TenBen: document.getElementById('tenBen').value.trim(),
//         DiaChi: document.getElementById('diaChi').value.trim(),
//         SDTBen: document.getElementById('soDienThoai').value.trim(),
//         IDTinh: document.getElementById('idTinhHidden').value.trim()
//     };

//     console.log("Dữ liệu gửi:", benXe);

//     try {
//         const res = await fetch("http://127.0.0.1:5000/benxe", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify(benXe)
//         });

//         const result = await res.json();
//         if (res.ok) {
//             alert("Thêm thành công!");
//             closeModal('modalBenXe');
//             this.reset();
//         } else {
//             alert("Lỗi: " + result.error);
//         }
//     } catch (err) {
//         console.error("Lỗi khi gửi dữ liệu:", err);
//     }
// });

// ---------------------------------------
// Hàm load tỉnh thành
// form chỉnh sửa bến xe
// document.getElementById("formBenXeEdit").addEventListener("submit", function (e) {
//     e.preventDefault();
//     const idBen = document.getElementById("idBenEdit").value;
//     const benXeData = {
//         TenBen: document.getElementById("tenBenEdit").value,
//         DiaChi: document.getElementById("diaChiEdit").value,
//         SDTBen: document.getElementById("soDienThoaiEdit").value,
//         IDTinh: document.getElementById("tinhThanhSelectEdit").value,
//     };

//     fetch(`/benxe/${idBen}`, {
//         method: "PUT",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(benXeData),
//     })
//     .then(res => res.json())
//     .then(data => {
//         alert("Cập nhật bến xe thành công");
//         closeModal("modalBenXeEdit");
//         loadAllBenXe();  // Tải lại danh sách bến xe
//     })
//     .catch(err => {
//         console.error("Lỗi khi cập nhật bến xe:", err);
//         alert("Cập nhật không thành công");
//     });
// });

// // ---------------------------------------
// // Hàm load tỉnh thành cho form chỉnh sửa
// async function loadTinhThanhOptionsEdit(selectedID = "") {
//     const select = document.getElementById("tinhThanhSelectEdit");
//     select.innerHTML = `<option value="">Chọn tỉnh/thành phố</option>`;  // Reset lại list options
//     try {
//         const res = await fetch("http://127.0.0.1:5000/tinhthanh");
//         const data = await res.json();

//         data.forEach(tinh => {
//             const option = document.createElement("option");
//             option.value = tinh.IDTinh;
//             option.textContent = tinh.TenTinh;
//             if (tinh.IDTinh === selectedID) {
//                 option.selected = true;  // Chọn tỉnh thành hiện tại
//             }
//             select.appendChild(option);
//         });
//     } catch (err) {
//         console.error("Lỗi khi tải tỉnh thành (Edit):", err);
//     }
// }

// // Chức năng chỉnh sửa bến xe
// function editBenXe(idBen) {
//     fetch(`/benxe/${idBen}`)
//         .then(res => res.json())
//         .then(data => {
//             // Điền dữ liệu vào form chỉnh sửa
//             document.getElementById("idBenEdit").value = data.IDBen;
//             document.getElementById("tenBenEdit").value = data.TenBen;
//             document.getElementById("diaChiEdit").value = data.DiaChi;
//             document.getElementById("soDienThoaiEdit").value = data.SDTBen;

//             // Gọi hàm load tỉnh thành và chọn đúng tỉnh
//             loadTinhThanhOptionsEdit(data.IDTinh);

//             // Mở modal chỉnh sửa
//             openModal("modalBenXeEdit");
//         })
//         .catch(err => {
//             console.error("Lỗi khi lấy thông tin bến xe:", err);
//         });
// }



// // Chức năng xóa bến xe
// function deleteBenXe(id_ben) {
//     const url = `/benxe/${id_ben}`;

//     fetch(url, {
//         method: 'DELETE',
//     })
//     .then(response => response.json())
//     .then(data => {
//         alert("Xóa bến xe thành công");
//         const row = document.getElementById(`row-${id_ben}`);
//         if (row) row.remove(); // Xoá hàng khỏi bảng
//     })
//     .catch((error) => {
//         alert("Lỗi khi xóa bến xe");
//         console.error(error);
//     });
// }

// // -------------------------------------------------------
// // ------------- Quản lý tỉnh thành
// // hoàn thành

// // Gọi API để lấy danh sách tỉnh thành và hiển thị vào bảng
// function loadAllTinhThanh() {
//     fetch('http://127.0.0.1:5000/tinhthanh')
//         .then(response => response.json())
//         .then(data => {
//             const tableBody = document.getElementById('tinhthanh-table-body');
//             tableBody.innerHTML = '';

//             data.forEach(item => {
//                 const row = document.createElement('tr');
//                 row.innerHTML = `
//                     <td>${item.IDTinh}</td>
//                     <td>${item.TenTinh}</td>
//                     <td class="px-4 py-2">
//                         <div class="icon-actions">
//                             <i class="bx bxs-edit-alt icon edit-icon" onclick="editTinhThanh('${item.IDTinh}')"></i>
//                             <i class="bx bxs-trash icon delete-icon" onclick="deleteTinhThanh('${item.IDTinh}')"></i>
//                         </div>
//                     </td>
//                 `;
//                 tableBody.appendChild(row);
//             });
//         })
//         .catch(error => console.error('Lỗi khi tải tỉnh thành:', error));
// }

// // Gọi khi load trang
// document.addEventListener('DOMContentLoaded', loadAllTinhThanh);
// // Hàm tìm kiếm tỉnh thành theo tên
// function searchTinhThanh() {
//     const keyword = document.getElementById('search-tinhthanh').value.trim().toLowerCase();

//     fetch('http://127.0.0.1:5000/tinhthanh')
//         .then(response => response.json())
//         .then(data => {
//             const filtered = data.filter(item => 
//                 item.TenTinh.toLowerCase().includes(keyword)
//             );

//             const tableBody = document.getElementById('tinhthanh-table-body');
//             tableBody.innerHTML = '';

//             filtered.forEach(item => {
//                 const row = document.createElement('tr');
//                 row.innerHTML = `
//                     <td>${item.IDTinh}</td>
//                     <td>${item.TenTinh}</td>
//                     <td class="px-4 py-2">
//                         <div class="icon-actions">
//                             <i class="bx bxs-edit-alt icon edit-icon" onclick="openEditTinhThanh('${item.IDTinh}')"></i>
//                             <i class="bx bxs-trash icon delete-icon" onclick="deleteTinhThanh('${item.IDTinh}')"></i>
//                         </div>
//                     </td>
//                 `;
//                 tableBody.appendChild(row);
//             });
//         })
//         .catch(error => console.error('Lỗi khi tìm kiếm:', error));
// }

// //thêm tỉnh thành mới // đã xong
// document.getElementById("formTinhThanh").addEventListener("submit", async function(e) {
//     e.preventDefault();
//     // const id = document.getElementById("idTinh").value.trim();
//     const name = document.getElementById("tenTinh").value.trim();

//     try {
//         const res = await fetch("http://127.0.0.1:5000/tinhthanh", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ TenTinh: name })
//         });

//         const result = await res.json();
//         if (res.ok) {
//             alert("Thêm thành công");
//             closeModal("modalTinhThanh");
//             this.reset();
//             loadAllTinhThanh();
//         } else {
//             alert("Lỗi: " + result.error);
//         }
//     } catch (err) {
//         console.error("Lỗi thêm tỉnh thành:", err);
//     }
// });

// // 
// function editTinhThanh(id, ten) {
//     document.getElementById("idTinhEdit").value = id;
//     document.getElementById("tenTinhEdit").value = ten;
//     openModal("modalTinhThanhEdit");
// }

// document.getElementById("formTinhThanhEdit").addEventListener("submit", async function(e) {
//     e.preventDefault();
//     const id = document.getElementById("idTinhEdit").value.trim();
//     const name = document.getElementById("tenTinhEdit").value.trim();

//     try {
//         const res = await fetch(`http://127.0.0.1:5000/tinhthanh/${id}`, {
//             method: "PUT",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ TenTinh: name })
//         });

//         if (res.ok) {
//             alert("Cập nhật thành công");
//             closeModal("modalTinhThanhEdit");
//             loadAllTinhThanh();
//         } else {
//             alert("Cập nhật thất bại");
//         }
//     } catch (err) {
//         console.error("Lỗi cập nhật:", err);
//     }
// });

// // xóa tỉnh // đã xong
// async function deleteTinhThanh(id) {
//     if (!confirm("Bạn có chắc muốn xóa tỉnh thành này?")) return;

//     try {
//         const res = await fetch(`http://127.0.0.1:5000/tinhthanh/${id}`, {
//             method: "DELETE"
//         });

//         if (res.ok) {
//             alert("Đã xóa thành công");
//             loadAllTinhThanh();
//         } else {
//             alert("Xóa thất bại");
//         }
//     } catch (err) {
//         console.error("Lỗi khi xóa:", err);
//     }
// }


// -----------------------------------------------------------
// ---------------- Quản lý tuyến xe



const tinhThanh = [
    { id: "TT01", name: "An Giang" },
    { id: "TT02", name: "Cần Thơ" },
    { id: "TT03", name: "Đồng Tháp" },
    { id: "TT04", name: "Hậu Giang" },
    { id: "TT05", name: "Sóc Trăng" },
    { id: "TT06", name: "Thành phố Hồ Chí Minh" },
    { id: "TT07", name: "Vĩnh Long" },
];

document.addEventListener('DOMContentLoaded', () => {
    const tenDiemDi = document.getElementById('diemDiSelect');
    const tenDiemDen = document.getElementById('diemDenSelect');

    // Tạo option cho cả hai select
    tinhThanh.forEach(tt => {
        const option1 = document.createElement('option');
        option1.value = tt.id;
        option1.textContent = tt.name;
        tenDiemDi.appendChild(option1);

        const option2 = document.createElement('option');
        option2.value = tt.id;
        option2.textContent = tt.name;
        tenDiemDen.appendChild(option2);
    });

    // Gán ID tương ứng khi chọn tỉnh
    tenDiemDi.addEventListener('change', () => {
        const id = tenDiemDi.value;
        document.getElementById('idDiemDi').value = id;
        document.getElementById('showIdDiemDi').value = id;
    });

    tenDiemDen.addEventListener('change', () => {
        const id = tenDiemDen.value;
        document.getElementById('idDiemDen').value = id;
        document.getElementById('showIdDiemDen').value = id;
    });

    loadAllTuyenXe();
});

// load xong
// function loadTinhThanh() {
//     fetch("http://127.0.0.1:5000/api/tentinhthanh")
//     // fetch('http://127.0.0.1:5000/tinhthanh')
//         .then(res => res.json())
//         .then(data => {
//             tinhThanhList = data;
//             tenDiemDi = document.getElementById('diemDiSelect');
//             tenDiemDen = document.getElementById('diemDenSelect');

//             tenDiemDi.innerHTML = '<option value="">-- Chọn điểm đi --</option>';
//             tenDiemDen.innerHTML = '<option value="">-- Chọn điểm đến --</option>';

//             data.forEach(tinh => {
//                 const option = `<option value="${tinh.IDTinh}">${tinh.TenTinh}</option>`;
//                 tenDiemDi.innerHTML += option;
//                 tenDiemDen.innerHTML += option;
//             });

//             // Sự kiện chọn điểm đi
//             tenDiemDi.addEventListener('change', () => {
//                 const id = tenDiemDi.value;
//                 document.getElementById('idDiemDi').value = id;
//                 document.getElementById('showIdDiemDi').value = id;
//             });

//             // Sự kiện chọn điểm đến
//             tenDiemDen.addEventListener('change', () => {
//                 const id = tenDiemDen.value;
//                 document.getElementById('idDiemDen').value = id;
//                 document.getElementById('showIdDiemDen').value = id;
//             });
//         });
// }

// Load tất cả tuyến xe // xong
function loadAllTuyenXe() {
    fetch('http://127.0.0.1:5000/tuyenxe')
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById('tuyenxe-table-body');
            table.innerHTML = '';
            data.forEach(tx => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${tx.IDTuyenXe}</td>
                    <td>${tx.TenDiemDi}</td>
                    <td>${tx.TenDiemDen}</td>
                    <td>${tx.QuangDuong} km</td>
                    <td>${tx.TG_DiChuyen} giờ</td>
                    
                `;
                table.appendChild(row);
            });
        });
}

async function deleteTuyenXe(id) {
    if (!confirm("Bạn có chắc muốn xóa tuyến xe này?")) return;

    try {
        const res = await fetch(`http://127.0.0.1:5000/tuyenxe/${id}`, {
            method: "DELETE"
        });

        if (res.ok) {
            alert("Đã xóa tuyến xe thành công");
            loadAllTuyenXe();
        } else {
            alert("Xóa thất bại");
        }
    } catch (err) {
        console.error("Lỗi khi xóa:", err);
    }
}

// Tìm kiếm theo điểm đi / đến //xong
function searchTuyenXe() {
    const keywordDi = document.getElementById('search-diemdi').value.trim().toLowerCase();
    const keywordDen = document.getElementById('search-diemden').value.trim().toLowerCase();

    fetch('http://127.0.0.1:5000/tuyenxe')
        .then(res => res.json())
        .then(data => {
            const filtered = data.filter(tx =>
                tx.TenDiemDi.toLowerCase().includes(keywordDi) &&
                tx.TenDiemDen.toLowerCase().includes(keywordDen)
            );

            const table = document.getElementById('tuyenxe-table-body');
            table.innerHTML = '';
            filtered.forEach(tx => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${tx.IDTuyenXe}</td>
                    <td>${tx.TenDiemDi}</td>
                    <td>${tx.TenDiemDen}</td>
                    <td>${tx.QuangDuong} km</td>
                    <td>${tx.TG_DiChuyen} giờ</td>
                    
                `;
                table.appendChild(row);
            });
        });
}


document.getElementById("formTuyenXe").addEventListener("submit", async function (event) {
    event.preventDefault();

    const IDDiemDi = document.getElementById("idDiemDi").value;
    const TenDiemDi = document.getElementById("diemDiSelect").selectedOptions[0].text;

    const IDDiemDen = document.getElementById("idDiemDen").value;
    const TenDiemDen = document.getElementById("diemDenSelect").selectedOptions[0].text;

    const QuangDuong = document.getElementById("quangDuong").value;
    const TG_DiChuyen = document.getElementById("thoiGianDiChuyen").value;

    const tuyenXe = {
        IDDiemDi,
        TenDiemDi,
        IDDiemDen,
        TenDiemDen,
        QuangDuong,
        TG_DiChuyen
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/tuyenxe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(tuyenXe),
        });
    
        const result = await response.json();
    
        if (response.ok) {
            alert("Thêm tuyến xe thành công!");
            // Reload lại danh sách tuyến xe nếu cần
        } else {
            console.error("Lỗi khi thêm tuyến xe:", result);
            alert("Không thể thêm tuyến xe. Chi tiết: " + result.error);
        }
    } catch (error) {
        console.error("Lỗi fetch:", error);
        alert("Lỗi mạng hoặc server.");
    }
    
});

function editTuyenXe(id) {
    console.log("Đang chỉnh sửa tuyến xe có ID:", id);
    // Gọi API để lấy dữ liệu chi tiết tuyến xe
    fetch(`http://127.0.0.1:5000/tuyenxe/${id}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById('edit-id-tuyenxe').value = data.IDTuyenXe;
            document.getElementById('edit-ten-diemdi').value = data.TenDiemDi;
            document.getElementById('edit-id-diemdi').value = data.IDDiemDi;
            document.getElementById('edit-ten-diemden').value = data.TenDiemDen;
            document.getElementById('edit-id-diemden').value = data.IDDiemDen;
            document.getElementById('edit-tg-dichuyen').value = data.TG_DiChuyen;
            document.getElementById('edit-quangduong').value = data.QuangDuong;
            document.getElementById('edit-form-container').style.display = 'block';
        });
}

function hideEditForm() {
    document.getElementById('edit-form-container').style.display = 'none';
}

document.getElementById('edit-tuyenxe-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const id = document.getElementById('edit-id-tuyenxe').value;

    const data = {
        IDDiemDi: document.getElementById('edit-id-diemdi').value,
        TenDiemDi: document.getElementById('edit-ten-diemdi').value,
        IDDiemDen: document.getElementById('edit-id-diemden').value,
        TenDiemDen: document.getElementById('edit-ten-diemden').value,
        TG_DiChuyen: document.getElementById('edit-tg-dichuyen').value,
        QuangDuong: document.getElementById('edit-quangduong').value,
    };

    fetch(`http://127.0.0.1:5000/tuyenxe/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(response => {
            alert(response.message);
            hideEditForm();
            loadAllTuyenXe(); // reload lại bảng
        })
        .catch(err => {
            alert("Lỗi khi cập nhật tuyến xe.");
            console.error(err);
        });
});


// --------------------------------------------------------------
// ------------------ Quản lý chuyến xe

// Gọi API để lấy danh sách chuyến xe và hiển thị vào bảng
function loadAllChuyenXe() {
    fetch('http://127.0.0.1:5000/chuyenxe')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('chuyenxe-table-body');
            tableBody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.IDChuyen}</td>
                    <td>${item.IDTaiXe}</td>
                    <td>${item.IDXe}</td>
                    <td>${item.IDTuyenXe}</td>
                    <td>${item.BenKhoiHanh}</td>
                    <td>${item.BenDen}</td>
                    <td>${item.TG_XuatPhat}</td>
                    <td>${item.TG_DuDen}</td>
                    <td>${item.GiaVe}</td>
                    
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Lỗi khi tải chuyến xe:', error));
}

// Gọi khi load trang
document.addEventListener('DOMContentLoaded', loadAllChuyenXe);


// Tìm kiếm chuyến xe theo tên tỉnh
function searchChuyenXe() {
    const diemDiInput = document.getElementById('cx-search-diemdi');
    const diemDenInput = document.getElementById('cx-search-diemden');

    if (!diemDiInput || !diemDenInput) {
        alert("Không tìm thấy ô nhập điểm đi / điểm đến trên trang.");
        return;
    }

    const diemDi = diemDiInput.value.trim();
    const diemDen = diemDenInput.value.trim();

    console.log("Điểm đi:", diemDi, "Điểm đến:", diemDen);  // Gỡ lỗi

    if (diemDi === "" || diemDen === "") {
        alert('Vui lòng nhập đầy đủ điểm đi và điểm đến');
        return;
    }

    fetch(`/api/chuyenxe/search?diem_di=${encodeURIComponent(diemDi)}&diem_den=${encodeURIComponent(diemDen)}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('chuyenxe-table-body');
            tableBody.innerHTML = '';

            if (data.length === 0) {
                tableBody.innerHTML = `<tr><td colspan="9">Không tìm thấy chuyến xe phù hợp.</td></tr>`;
                return;
            }

            data.forEach(cx => {
                const row = `
                    <tr>
                        <td>${cx.IDChuyen}</td>
                        <td>${cx.IDTaiXe}</td>
                        <td>${cx.IDXe}</td>
                        <td>${cx.IDTuyenXe}</td>
                        <td>${cx.BenKhoiHanh}</td>
                        <td>${cx.BenDen}</td>
                        <td>${cx.TG_XuatPhat}</td>
                        <td>${cx.TG_DuDen}</td>
                        <td>${cx.GiaVe}</td>
                        
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => {
            console.error("Lỗi khi tìm kiếm chuyến xe:", error);
        });
}

// thêm chuyến xe mới

document.addEventListener("DOMContentLoaded", function () {
    const data = {
        taiXe: [
            { id: "NV0009", ten: "Cao Văn Khánh" },
            { id: "NV0010", ten: "Tạ Minh Thông" },
            { id: "NV0011", ten: "Mai Thanh Sơn" },
            { id: "NV0012", ten: "Vũ Phương Linh" },
            { id: "NV0013", ten: "Tô Gia Bảo" },
            { id: "NV0014", ten: "Chu Kiến Thành" },
            { id: "NV0015", ten: "Hứa Quang Minh" }
        ],
        xe: [
            { id: "XE0008", bienSo: "95B3619069" },
            { id: "XE0009", bienSo: "53B2981701" },
            { id: "XE0010", bienSo: "64Z0162198" },
            { id: "XE0011", bienSo: "31S1784609" },
            { id: "XE0012", bienSo: "76B8155844" },
            { id: "XE0013", bienSo: "94U5160256" },
            { id: "XE0014", bienSo: "52W6574338" },
            { id: "XE0015", bienSo: "19M5372260" },
            { id: "XE0016", bienSo: "70T0823248" }

            
        ],
        tuyenXe: [
            { id: "TX0001" },
            { id: "TX0002" },
            { id: "TX0003" },
            { id: "TX0004" },
            { id: "TX0005" },
            { id: "TX0006" },
            { id: "TX0007" },
            { id: "TX0008" },
            { id: "TX0009" },
            { id: "TX0010" },
            { id: "TX0011" },
            { id: "TX0012" },
            { id: "TX0013" },
            { id: "TX0014" },
            { id: "TX0015" },
            { id: "TX0016" },
            { id: "TX0017" },
            { id: "TX0018" },
            { id: "TX0019" },
            { id: "TX0020" },
            { id: "TX0021" },
            { id: "TX0022" },
            { id: "TX0023" },
            { id: "TX0024" },
            { id: "TX0025" }
        
        ],
        benXe: [
            { id: "BX0001", ten: "Bến xe An Sương" },
            { id: "BX0002", ten: "Bến xe Cao Lãnh" },
            { id: "BX0003", ten: "Bến xe Cần Thơ" },
            { id: "BX0004", ten: "Bến xe Châu Đốc" },
            { id: "BX0005", ten: "Bến xe Long Xuyên" },
            { id: "BX0006", ten: "Bến xe Miền Đông" },
            { id: "BX0007", ten: "Bến xe Miền Tây" },
            { id: "BX0008", ten: "Bến xe Sa Đéc" },
            { id: "BX0009", ten: "Bến xe Sóc Trăng" },
            { id: "BX0010", ten: "Bến xe Vị Thanh" },
            { id: "BX0011", ten: "Bến xe Vĩnh Long" }
            
        ]
    };

    // Gán dữ liệu vào select
    function populateSelect(selectId, items, labelField = "ten", valueField = "id") {
        const select = document.getElementById(selectId);
        items.forEach(item => {
            const option = document.createElement("option");
            option.value = item[valueField];
            option.textContent = item[labelField];
            select.appendChild(option);
        });
    }

    populateSelect("selectTaiXe", data.taiXe, "ten", "id");
    populateSelect("selectXe", data.xe, "bienSo", "id");
    populateSelect("selectTuyen", data.tuyenXe, "id", "id");
    populateSelect("selectBenKhoiHanh", data.benXe, "ten", "id");
    populateSelect("selectBenDen", data.benXe, "ten", "id");

    // Gán ID bến vào input ẩn khi chọn bến
    document.getElementById("selectBenKhoiHanh").addEventListener("change", function () {
        document.getElementById("idBenKhoiHanh").value = this.value;
    });

    document.getElementById("selectBenDen").addEventListener("change", function () {
        document.getElementById("idBenDen").value = this.value;
    });

    // Submit form
    document.getElementById("formChuyenXe").addEventListener("submit", function (e) {
        e.preventDefault();

        const payload = {
            IDTaiXe: document.getElementById("selectTaiXe").value,
            IDXe: document.getElementById("selectXe").value,
            IDTuyenXe: document.getElementById("selectTuyen").value,
            IDBenKhoiHanh: document.getElementById("idBenKhoiHanh").value,
            BenKhoiHanh: document.getElementById("selectBenKhoiHanh").selectedOptions[0].text,
            IDBenDen: document.getElementById("idBenDen").value,
            BenDen: document.getElementById("selectBenDen").selectedOptions[0].text,
            TG_XuatPhat: document.getElementById("tgXuatPhat").value,
            TG_DuDen: document.getElementById("tgDuDen").value,
            GiaVe: document.getElementById("giaVe").value
        };

        fetch("http://127.0.0.1:5000/chuyenxe", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(result => {
            if (result.message) {
                alert(result.message + " | Mã chuyến: " + result.IDChuyen);
                // Reset form hoặc đóng modal tùy ý
            } else {
                alert("Lỗi: " + result.error);
            }
        })
        .catch(err => console.error("Lỗi gửi dữ liệu:", err));
    });
});



// Hàm sửa chuyến xe

// Dữ liệu giả
const data = {
    taiXe: [
        { id: "NV0009", ten: "Cao Văn Khánh" },
        { id: "NV0010", ten: "Tạ Minh Thông" },
        { id: "NV0011", ten: "Mai Thanh Sơn" },
        { id: "NV0012", ten: "Vũ Phương Linh" },
        { id: "NV0013", ten: "Tô Gia Bảo" },
        { id: "NV0014", ten: "Chu Kiến Thành" },
        { id: "NV0015", ten: "Hứa Quang Minh" }
    ],
    xe: [
        { id: "XE0008", bienSo: "95B3619069" },
        { id: "XE0009", bienSo: "53B2981701" },
        { id: "XE0010", bienSo: "64Z0162198" },
        { id: "XE0011", bienSo: "31S1784609" },
        { id: "XE0012", bienSo: "76B8155844" },
        { id: "XE0013", bienSo: "94U5160256" },
        { id: "XE0014", bienSo: "52W6574338" },
        { id: "XE0015", bienSo: "19M5372260" },
        { id: "XE0016", bienSo: "70T0823248" }
    ],
    tuyenXe: [
        { id: "TX0001" }, { id: "TX0002" }, { id: "TX0003" }, { id: "TX0004" }, { id: "TX0005" },
        { id: "TX0006" }, { id: "TX0007" }, { id: "TX0008" }, { id: "TX0009" }, { id: "TX0010" },
        { id: "TX0011" }, { id: "TX0012" }, { id: "TX0013" }, { id: "TX0014" }, { id: "TX0015" },
        { id: "TX0016" }, { id: "TX0017" }, { id: "TX0018" }, { id: "TX0019" }, { id: "TX0020" },
        { id: "TX0021" }, { id: "TX0022" }, { id: "TX0023" }, { id: "TX0024" }, { id: "TX0025" }
    ],
    benXe: [
        { id: "BX0001", ten: "Bến xe An Sương" },
        { id: "BX0002", ten: "Bến xe Cao Lãnh" },
        { id: "BX0003", ten: "Bến xe Cần Thơ" },
        { id: "BX0004", ten: "Bến xe Châu Đốc" },
        { id: "BX0005", ten: "Bến xe Long Xuyên" },
        { id: "BX0006", ten: "Bến xe Miền Đông" },
        { id: "BX0007", ten: "Bến xe Miền Tây" },
        { id: "BX0008", ten: "Bến xe Sa Đéc" },
        { id: "BX0009", ten: "Bến xe Sóc Trăng" },
        { id: "BX0010", ten: "Bến xe Vị Thanh" },
        { id: "BX0011", ten: "Bến xe Vĩnh Long" }
    ]
};

// Hàm điền dữ liệu vào các select
function populateSelectOptions(selectId, options) {
    const selectElement = document.getElementById(selectId);
    selectElement.innerHTML = '';  // Xóa tất cả các option hiện có
    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option.id;
        optionElement.textContent = option.ten || option.bienSo || option.id;
        selectElement.appendChild(optionElement);
    });
}

// Hàm sửa chuyến xe
async function editChuyenXe(idChuyen) {
    try {
        const response = await fetch(`/chuyenxe/${idChuyen}`);
        const dataChuyenXe = await response.json();

        // Điền dữ liệu vào form
        document.getElementById("editIDChuyen").value = dataChuyenXe.IDChuyen;
        document.getElementById("editSelectTaiXe").value = dataChuyenXe.IDTaiXe;
        document.getElementById("editSelectXe").value = dataChuyenXe.IDXe;
        document.getElementById("editSelectTuyen").value = dataChuyenXe.IDTuyenXe;
        document.getElementById("editSelectBenKhoiHanh").value = dataChuyenXe.IDBenKhoiHanh;
        document.getElementById("editSelectBenDen").value = dataChuyenXe.IDBenDen;
        document.getElementById("editIDBenKhoiHanh").value = dataChuyenXe.IDBenKhoiHanh;
        document.getElementById("editIDBenDen").value = dataChuyenXe.IDBenDen;
        document.getElementById("editTGXuatPhat").value = dataChuyenXe.TG_XuatPhat;
        document.getElementById("editTGDuDen").value = dataChuyenXe.TG_DuDen;
        document.getElementById("editGiaVe").value = dataChuyenXe.GiaVe;

        // Hiển thị dữ liệu giả cho các select
        populateSelectOptions('editSelectTaiXe', data.taiXe);
        populateSelectOptions('editSelectXe', data.xe);
        populateSelectOptions('editSelectTuyen', data.tuyenXe);
        populateSelectOptions('editSelectBenKhoiHanh', data.benXe);
        populateSelectOptions('editSelectBenDen', data.benXe);

        openModal("modalEditChuyenXe");
    } catch (error) {
        console.error("Lỗi khi lấy dữ liệu chuyến xe:", error);
    }
}

// Submit form sửa chuyến xe
document.getElementById("formEditChuyenXe").addEventListener("submit", async function (e) {
    e.preventDefault();

    const idChuyen = document.getElementById("editIDChuyen").value;

    const payload = {
        IDTaiXe: document.getElementById("editSelectTaiXe").value,
        IDXe: document.getElementById("editSelectXe").value,
        IDTuyenXe: document.getElementById("editSelectTuyen").value,
        IDBenKhoiHanh: document.getElementById("editIDBenKhoiHanh").value,
        BenKhoiHanh: document.getElementById("editSelectBenKhoiHanh").selectedOptions[0].text,
        IDBenDen: document.getElementById("editIDBenDen").value,
        BenDen: document.getElementById("editSelectBenDen").selectedOptions[0].text,
        TG_XuatPhat: document.getElementById("editTGXuatPhat").value,
        TG_DuDen: document.getElementById("editTGDuDen").value,
        GiaVe: parseInt(document.getElementById("editGiaVe").value),
        // Nếu không có giá trị cho NgayXuatPhat, nó sẽ được tự động là null khi gửi lên
        NgayXuatPhat: document.getElementById("editTGXuatPhat").value || null
    };
    

    try {
        const response = await fetch(`http://127.0.0.1:5000/chuyenxe/${idChuyen}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const result = await response.json();
        if (response.ok) {
            alert("Cập nhật thành công");
            closeModal("modalEditChuyenXe");
            loadAllChuyenXe?.();
        } else {
            alert("Lỗi: " + result.error);
        }
    } catch (err) {
        console.error("Lỗi:", err);
    }
});



// async function editChuyenXe(idChuyen) {
//     try {
//         const response = await fetch(`/chuyenxe/${idChuyen}`);
//         const data = await response.json();

//         document.getElementById("editIDChuyen").value = data.IDChuyen;
//         document.getElementById("editSelectTaiXe").value = data.IDTaiXe;
//         document.getElementById("editSelectXe").value = data.IDXe;
//         document.getElementById("editSelectTuyen").value = data.IDTuyenXe;
//         document.getElementById("editSelectBenKhoiHanh").value = data.IDBenKhoiHanh;
//         document.getElementById("editSelectBenDen").value = data.IDBenDen;
//         document.getElementById("editIDBenKhoiHanh").value = data.IDBenKhoiHanh;
//         document.getElementById("editIDBenDen").value = data.IDBenDen;
//         document.getElementById("editTGXuatPhat").value = data.TG_XuatPhat;
//         document.getElementById("editTGDuDen").value = data.TG_DuDen;
//         document.getElementById("editGiaVe").value = data.GiaVe;

//         openModal("modalEditChuyenXe");
//     } catch (error) {
//         console.error("Lỗi khi lấy dữ liệu chuyến xe:", error);
//     }
// }

// // Submit form sửa chuyến xe
// document.getElementById("formEditChuyenXe").addEventListener("submit", async function (e) {
//     e.preventDefault();

//     const idChuyen = document.getElementById("editIDChuyen").value;

//     const payload = {
//         IDTaiXe: document.getElementById("editSelectTaiXe").value,
//         IDXe: document.getElementById("editSelectXe").value,
//         IDTuyenXe: document.getElementById("editSelectTuyen").value,
//         IDBenKhoiHanh: document.getElementById("editIDBenKhoiHanh").value,
//         BenKhoiHanh: document.getElementById("editSelectBenKhoiHanh").selectedOptions[0].text,
//         IDBenDen: document.getElementById("editIDBenDen").value,
//         BenDen: document.getElementById("editSelectBenDen").selectedOptions[0].text,
//         TG_XuatPhat: document.getElementById("editTGXuatPhat").value,
//         TG_DuDen: document.getElementById("editTGDuDen").value,
//         GiaVe: parseInt(document.getElementById("editGiaVe").value)
//     };

//     try {
//         const response = await fetch(`http://127.0.0.1:5000/chuyenxe/${idChuyen}`, {
//             method: "PUT",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify(payload)
//         });
//         const result = await response.json();
//         if (response.ok) {
//             alert("Cập nhật thành công");
//             closeModal("modalEditChuyenXe");
//             loadAllChuyenXe?.();
//         } else {
//             alert("Lỗi: " + result.error);
//         }
//     } catch (err) {
//         console.error("Lỗi:", err);
//     }
// });


async function deleteChuyenXe(id) {
    const confirmed = confirm("Bạn có chắc muốn xóa chuyến xe này?");
    if (!confirmed) return;

    try {
        const response = await fetch(`http://127.0.0.1:5000/chuyenxe/${id}`, {
            method: "DELETE"
        });

        const result = await response.json();
        if (response.ok) {
            alert("Xóa thành công");
            loadAllChuyenXe(); // reload danh sách nếu có
        } else {
            alert("Lỗi: " + result.error);
        }
    } catch (err) {
        console.error("Lỗi khi xóa:", err);
        alert("Đã xảy ra lỗi khi xóa chuyến xe");
    }
}


// --------------------------------------------------------------
// ------------------ Quản lý xe

// Lấy danh sách xe
// function loadAllXe() {
//     fetch('http://127.0.0.1:5000/xe')
//         .then(response => response.json())
//         .then(data => {
//             renderXeTable(data);
//             // Reset input và dropdown
//             document.getElementById("search-xe").value = "";
//             document.getElementById("filter-loai-xe").value = "";
//             document.getElementById("filter-trang-thai").value = "";
//         })
//         .catch(error => console.error('Lỗi khi tải xe:', error));
// }

// // Hiển thị danh sách xe
// function renderXeTable(data) {
//     const tbody = document.getElementById("xe-table-body");
//     tbody.innerHTML = ""; // Clear table

//     data.forEach(item => {
//         let statusClass = '';
//         let statusIcon = '';
//         let statusText = item.TrangThai;

//         if (statusText === "Đang hoạt động") {
//             statusClass = 'status-active';
//             statusIcon = '<i class="bx bx-check-circle"></i>';
//         } else if (statusText === "Chưa hoạt động") {
//             statusClass = 'status-inactive';
//             statusIcon = '<i class="bx bx-minus-circle"></i>';
//         } else if (statusText === "Đang bảo trì") {
//             statusClass = 'status-maintenance';
//             statusIcon = '<i class="bx bx-error-circle"></i>';
//         }

//         const row = document.createElement('tr');
//         row.innerHTML = `
//             <td>${item.IDXe}</td>
//             <td>${item.BienSo}</td>
//             <td>${item.LoaiXe}</td>
//             <td>${item.SoGhe}</td>
//             <td><span class="badge ${statusClass}">${statusIcon} ${statusText}</span></td>
//             <td class="px-4 py-2">
//                 <div class="icon-actions">
//                     <i class="bx bxs-edit-alt icon edit-icon" onclick="editXe('${item.IDXe}')"></i>
//                     <i class="bx bxs-trash icon delete-icon" onclick="deleteXe('${item.IDXe}')"></i>
//                 </div>
//             </td>
//         `;
//         tbody.appendChild(row);
//     });
// }

// // Tìm kiếm xe theo biển số
// function searchXe() {
//     const keyword = document.getElementById("search-xe").value.trim();
//     if (!keyword) return;

//     fetch(`http://127.0.0.1:5000/xe/search?bien_so=${encodeURIComponent(keyword)}`)
//         .then(res => res.json())
//         .then(data => renderXeTable(data));
// }

// // Lọc theo loại xe
// function filterLoaiXe() {
//     const loaiXe = document.getElementById("filter-loai-xe").value;
//     if (!loaiXe) return loadAllXe();

//     fetch(`http://127.0.0.1:5000/xe/filter/loai?loai_xe=${encodeURIComponent(loaiXe)}`)
//         .then(res => res.json())
//         .then(data => renderXeTable(data));
// }

// // Lọc theo trạng thái
// function filterTrangThai() {
//     const trangThai = document.getElementById("filter-trang-thai").value;
//     if (!trangThai) return loadAllXe();

//     fetch(`http://127.0.0.1:5000/xe/filter/trangthai?trang_thai=${encodeURIComponent(trangThai)}`)
//         .then(res => res.json())
//         .then(data => renderXeTable(data));
// }

// // Gọi khi trang load
// document.addEventListener('DOMContentLoaded', loadAllXe);

// // Thêm xe mới
// document.getElementById('formXe').addEventListener('submit', function(e) {
//     e.preventDefault();

//     const xeData = {
//         BienSo: document.getElementById('bienso').value,
//         LoaiXe: document.getElementById('loaiXe').value,
//         SoGhe: parseInt(document.getElementById('soGhe').value),
//         TrangThai: document.getElementById('trangThai').value
//     };

//     fetch('http://127.0.0.1:5000/xe', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(xeData)
//     })
//     .then(res => res.json())
//     .then(data => {
//         alert(data.message || data.error);
//         if (data.message) location.reload();
//     });
// });

// // Hàm sửa xe
// async function editXe(idXe) {
//     try {
//         const response = await fetch(`http://127.0.0.1:5000/xe/${idXe}`);
//         const dataXe = await response.json();

//         // Điền dữ liệu vào form
//         document.getElementById("editIDXe").value = dataXe.IDXe;
//         document.getElementById("editBienso").value = dataXe.BienSo;
//         document.getElementById("editLoaiXe").value = dataXe.LoaiXe;
//         document.getElementById("editSoGhe").value = dataXe.SoGhe;
//         document.getElementById("editTrangThai").value = dataXe.TrangThai;

//         openModal("modalEditXe");
//     } catch (error) {
//         console.error("Lỗi khi lấy dữ liệu xe:", error);
//         alert("Không thể tải dữ liệu xe để chỉnh sửa.");
//     }
// }



// // Sửa xe
// document.getElementById('formEditXe').addEventListener('submit', function(e) {
//     e.preventDefault();

//     const id = document.getElementById('editIDXe').value;

//     const xeData = {
//         BienSo: document.getElementById('editBienso').value,
//         LoaiXe: document.getElementById('editLoaiXe').value,
//         SoGhe: parseInt(document.getElementById('editSoGhe').value),
//         TrangThai: document.getElementById('editTrangThai').value
//     };

//     fetch(`http://127.0.0.1:5000/xe/${id}`, {
//         method: 'PUT',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(xeData)
//     })
//     .then(res => res.json())
//     .then(data => {
//         alert(data.message || data.error);
//         if (data.message) location.reload();
//     });
// });



// // Xóa xe
// function deleteXe(id) {
//     if (!confirm("Bạn có chắc chắn muốn xóa xe này không?")) return;

//     fetch(`http://127.0.0.1:5000/xe/${id}`, {
//         method: 'DELETE'
//     })
//     .then(res => res.json())
//     .then(data => {
//         alert(data.message || data.error);
//         if (data.message) location.reload();
//     });
// }

// // --------------------------------------------------------------
// // ------------------ Quản lý nhân viên

// // Lấy danh sách nhân viên
// async function loadAllNhanVien() {
//     try {
//         const response = await fetch("http://127.0.0.1:5000/nhanvien");
//         const data = await response.json();

//         const tbody = document.getElementById("nhanvien-table-body");
//         tbody.innerHTML = "";

//         data.forEach(nv => {
//             const tr = document.createElement("tr");

//             tr.innerHTML = `
//                 <td>${nv.IDNhanVien}</td>
//                 <td>${nv.HoTen}</td>
//                 <td>${nv.SDT}</td>
//                 <td>${nv.DiaChi}</td>
//                 <td><span class="tag ${getGioiTinhClass(nv.GioiTinh)}">${nv.GioiTinh}</span></td>
//                 <td>${nv.CCCD}</td>
//                 <td><span class="tag ${getChucVuClass(nv.ChucVu)}">${nv.ChucVu}</span></td>
//                 <td class="px-4 py-2">
//                 <div class="icon-actions">
//                     <i class="bx bxs-edit-alt icon edit-icon" onclick="editNhanVien('${nv.IDNhanVien}')"></i>
//                     <i class="bx bxs-trash icon delete-icon" onclick="deleteNhanVien('${nv.IDNhanVien}')"></i>
//                 </div>
//             </td>
//             `;

//             tbody.appendChild(tr);
//         });
//     } catch (error) {
//         console.error("Lỗi khi tải danh sách nhân viên:", error);
//     }
// }

// function getGioiTinhClass(gioiTinh) {
//     if (gioiTinh === "Nữ") return "tag-pink";
//     if (gioiTinh === "Nam") return "tag-blue";
//     return "";
// }

// function getChucVuClass(chucVu) {
//     switch (chucVu) {
//         case "Admin":
//             return "tag-green";
//         case "Nhân viên bán vé":
//             return "tag-brown";
//         case "Tài xế":
//             return "tag-gray";
//         default:
//             return "";
//     }
// }

// document.addEventListener('DOMContentLoaded', loadAllNhanVien);

// function filterNhanVien() {
//     const gioiTinh = document.getElementById("filterGioiTinh").value;
//     const chucVu = document.getElementById("filterChucVu").value;

//     let url = `http://127.0.0.1:5000/nhanvien/filter?`;
//     if (gioiTinh) url += `gioi_tinh=${encodeURIComponent(gioiTinh)}&`;
//     if (chucVu) url += `chuc_vu=${encodeURIComponent(chucVu)}`;

//     fetch(url)
//         .then(res => res.json())
//         .then(data => {
//             renderNhanVien(data);
//         })
//         .catch(err => {
//             console.error("Lỗi khi lọc nhân viên:", err);
//         });
// }


// function renderNhanVien(data) {
//     const tbody = document.getElementById("nhanvien-table-body");
//     tbody.innerHTML = "";

//     data.forEach(nv => {
//         // Xử lý giới tính
//         let genderClass = '';
//         if (nv.GioiTinh === "Nam") {
//             genderClass = 'tag-blue';
//         } else if (nv.GioiTinh === "Nữ") {
//             genderClass = 'tag-pink';
//         }

//         // Xử lý chức vụ
//         let roleClass = '';
//         if (nv.ChucVu === "Admin") {
//             roleClass = 'tag-green';
//         } else if (nv.ChucVu === "Nhân viên bán vé") {
//             roleClass = 'tag-brown';
//         } else if (nv.ChucVu === "Tài xế") {
//             roleClass = 'tag-gray';
//         }

//         const row = document.createElement('tr');
//         row.innerHTML = `
//             <td>${nv.IDNhanVien}</td>
//             <td>${nv.HoTen}</td>
//             <td>${nv.SDT}</td>
//             <td>${nv.DiaChi}</td>
//             <td><span class="badge ${genderClass}"> ${nv.GioiTinh}</span></td>
//             <td>${nv.CCCD}</td>
//             <td><span class="badge ${roleClass}"> ${nv.ChucVu}</span></td>
//             <td class="px-4 py-2">
//                 <div class="icon-actions">
//                     <i class="bx bxs-edit-alt icon edit-icon" onclick="editNhanVien('${nv.IDNhanVien}')"></i>
//                     <i class="bx bxs-trash icon delete-icon" onclick="deleteNhanVien('${nv.IDNhanVien}')"></i>
//                 </div>
//             </td>
//         `;
//         tbody.appendChild(row);
//     });
// }


// // thêm nhân viên
// document.getElementById("formNhanVien").addEventListener("submit", function (e) {
//     e.preventDefault();

//     const data = {
//         HoTen: document.getElementById("hoTen").value,
//         SDT: document.getElementById("soDienThoaiNV").value,
//         DiaChi: document.getElementById("diaChiNV").value,
//         CCCD: document.getElementById("cccdNV").value,
//         GioiTinh: document.getElementById("gioiTinhNV").value,
//         ChucVu: document.getElementById("chucVuNV").value
//     };

//     fetch("http://127.0.0.1:5000/nhanvien", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify(data)
//     })
//     .then(res => res.json())
//     .then(res => {
//         if (res.message) {
//             alert(res.message);
//             closeModal("modalNhanVien");
//             loadAllNhanVien();  // Hàm này gọi API get all để refresh bảng
//         } else {
//             alert("Lỗi: " + res.error);
//         }
//     })
//     .catch(err => console.error("Lỗi khi thêm nhân viên:", err));
// });


// function editNhanVien(id) {
//     fetch(`http://127.0.0.1:5000/nhanvien/${id}`)
//         .then(res => res.json())
//         .then(nv => {
//             if (!nv || nv.error) return alert("Không tìm thấy nhân viên.");

//             document.getElementById("editIDNV").value = nv.IDNhanVien;
//             document.getElementById("editHoTen").value = nv.HoTen;
//             document.getElementById("editSoDienThoaiNV").value = nv.SDT;
//             document.getElementById("editDiaChiNV").value = nv.DiaChi;
//             document.getElementById("editCCCDNV").value = nv.CCCD;
//             document.getElementById("editGioiTinhNV").value = nv.GioiTinh;
//             document.getElementById("editChucVuNV").value = nv.ChucVu;

//             openModal("modalEditNhanVien");
//         })
//         .catch(err => {
//             console.error("Lỗi khi lấy thông tin nhân viên:", err);
//             alert("Lỗi khi lấy thông tin nhân viên.");
//         });
// }


// document.getElementById("formEditNhanVien").addEventListener("submit", function (e) {
//     e.preventDefault();

//     const id = document.getElementById("editIDNV").value;

//     const data = {
//         HoTen: document.getElementById("editHoTen").value,
//         SDT: document.getElementById("editSoDienThoaiNV").value,
//         DiaChi: document.getElementById("editDiaChiNV").value,
//         CCCD: document.getElementById("editCCCDNV").value,
//         GioiTinh: document.getElementById("editGioiTinhNV").value,
//         ChucVu: document.getElementById("editChucVuNV").value
//     };

//     fetch(`http://127.0.0.1:5000/nhanvien/${id}`, {
//         method: "PUT",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify(data)
//     })
//     .then(res => res.json())
//     .then(res => {
//         if (res.message) {
//             alert(res.message);
//             closeModal("modalEditNhanVien");
//             loadAllNhanVien();
//         } else {
//             alert("Lỗi: " + res.error);
//         }
//     })
//     .catch(err => console.error("Lỗi khi cập nhật nhân viên:", err));
// });

// function deleteNhanVien(id) {
//     if (!confirm("Bạn có chắc muốn xóa nhân viên này?")) return;

//     fetch(`http://127.0.0.1:5000/nhanvien/${id}`, {
//         method: "DELETE"
//     })
//     .then(res => res.json())
//     .then(res => {
//         if (res.message) {
//             alert(res.message);
//             loadAllNhanVien();
//         } else {
//             alert("Lỗi: " + res.error);
//         }
//     })
//     .catch(err => console.error("Lỗi khi xóa nhân viên:", err));
// }



// function searchNhanVien() {
//     const ten = document.getElementById("search-nhanvien").value.trim();

//     if (ten === "") {
//         alert("Vui lòng nhập tên nhân viên cần tìm!");
//         return;
//     }

//     fetch(`http://127.0.0.1:5000/nhanvien/search?ten=${encodeURIComponent(ten)}`)
//         .then(res => res.json())
//         .then(data => {
//             if (data.error) {
//                 alert(data.error);
//                 return;
//             }

//             renderNhanVien(data); // Hàm hiển thị danh sách
//         })
//         .catch(err => {
//             console.error("Lỗi khi tìm nhân viên:", err);
//             alert("Đã xảy ra lỗi khi tìm kiếm.");
//         });
// }


// --------------------------------------------------------------
// ------------------ Quản lý khách hàng

// Tải lại danh sách khách hàng
function loadAllKhachHang() {
    fetch('http://127.0.0.1:5000/khach')
        .then(response => response.json())
        .then(data => {
            renderKhachHangTable(data);
        })
        .catch(error => console.error('Error:', error));
}
// Tìm kiếm khách hàng theo tên
function searchKhachHang() {
    const searchQuery = document.getElementById("search-khachhang").value;
    fetch(`/khach/name/${searchQuery}`)
        .then(response => response.json())
        .then(data => {
            renderKhachHangTable(data);
        })
        .catch(error => console.error('Error:', error));
}

// Lọc khách hàng theo giới tính
function filterKhachHang() {
    const gioiTinh = document.getElementById("filterGioiTinhKH").value;
    const url = gioiTinh ? `/khach/gioitinh/${gioiTinh}` : '/khach';
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            renderKhachHangTable(data);
        })
        .catch(error => console.error('Error:', error));
}

// Hiển thị danh sách khách hàng vào bảng
function renderKhachHangTable(khachList) {
    const tbody = document.getElementById("khachhang-table-body");
    tbody.innerHTML = ''; // Xóa dữ liệu cũ

    khachList.forEach(khach => {
        const tr = document.createElement('tr');
        
        // Thêm dữ liệu vào mỗi ô
        tr.innerHTML = `
            <td>${khach.IDKhach}</td>
            <td>${khach.HoTen}</td>
            <td><span class="tag ${khach.GioiTinh === 'Nam' ? 'tag-blue' : 'tag-pink'}">${khach.GioiTinh}</span></td>
            <td>${khach.CCCD}</td>
            <td>${khach.SDTKhach}</td>
        `;
        
        tbody.appendChild(tr);
    });
}



document.addEventListener("DOMContentLoaded", function () {
    loadAllKhachHang();
});


// ---------------------------------------------------------------
// ------------------ Quản lý vé
// Tải tất cả vé
function loadAllVe() {
    fetch('/vexe')
        .then(res => res.json())
        .then(data => renderVeTable(data))
        .catch(err => console.error('Error:', err));
}

// Tìm kiếm vé theo ID
function searchVe() {
    const idVe = document.getElementById('search-ve').value.trim();
    if (!idVe) return;

    fetch(`/vexe/${idVe}`)
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                renderVeTable([]);
            } else {
                renderVeTable([data]);
            }
        })
        .catch(err => console.error('Error:', err));
}

// Hiển thị dữ liệu vé vào bảng
function renderVeTable(veList) {
    const tbody = document.getElementById("ve-table-body");
    tbody.innerHTML = "";

    veList.forEach(ve => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${ve.IDVe}</td>
            <td>${ve.IDChuyen}</td>
            <td>${ve.IDKhach}</td>
            <td>${ve.IDXe}</td>
            <td>${ve.NgayDatVe}</td>
            <td>${ve.GiaVe}</td>
            <td class="px-4 py-2">
                <div class="icon-actions">
                    <i class="bx bxs-trash icon delete-icon" onclick="deleteVe('${ve.IDVe}')"></i>
                </div>
            </td>
            
        `;
        tbody.appendChild(tr);
    });
}

// Hủy vé
function deleteVe(idVe) {
    if (!confirm("Bạn có chắc muốn hủy vé này?")) return;

    fetch(`/vexe/${idVe}`, {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ IDVe: idVe })
    })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            loadAllVe();
        })
        .catch(err => console.error('Error:', err));
}

// Gọi khi trang được tải
window.onload = loadAllVe;

// đăng xuất
document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.querySelector(".items li:last-child a");

    logoutButton.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "http://127.0.0.1:5000/logout"; // Gọi route logout của Flask
    });
});
