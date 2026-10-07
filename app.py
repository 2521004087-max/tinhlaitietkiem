import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================

st.set_page_config(
    page_title="Tính Lãi Tiền Gửi Tiết Kiệm",
    page_icon="logo.jpg",
    layout="centered"
)

# ==============================
# HÀM ĐỊNH DẠNG TIỀN
# ==============================

def format_money(value):
    return f"{value:,.0f}".replace(",", ".") + " VNĐ"


# ==============================
# TIÊU ĐỀ
# ==============================

st.title("💰 TÍNH LÃI TIỀN GỬI TIẾT KIỆM")

st.write(
    "Công cụ tính toán tiền lãi theo phương pháp lãi đơn "
    "hoặc lãi kép."
)
# ==============================
# ĐỀ XUẤT KHOẢN GỬI PHÙ HỢP
# ==============================

st.subheader("🎯 Đề xuất khoản gửi phù hợp")

st.write(
    "Hãy cho biết bạn thuộc nhóm đối tượng nào để hệ thống "
    "đưa ra gợi ý về kỳ hạn và hình thức nhận lãi."
)

with st.form("form_de_xuat"):
    doi_tuong = st.selectbox(
        "👤 Bạn thuộc nhóm đối tượng nào?",
        [
            "Sinh viên / người mới bắt đầu tiết kiệm",
            "Người đi làm, thu nhập ổn định",
            "Gia đình có khoản tiền nhàn rỗi",
            "Người lớn tuổi / nghỉ hưu",
            "Kinh doanh / thu nhập không ổn định"
        ]
    )

    nut_de_xuat = st.form_submit_button(
        "🔍 ĐỀ XUẤT CHO TÔI",
        use_container_width=True
    )

if nut_de_xuat:

    if doi_tuong == "Sinh viên / người mới bắt đầu tiết kiệm":
        st.success("🎓 Gợi ý cho bạn")
        st.write("• Kỳ hạn tham khảo: **1–3 tháng**")
        st.write("• Hình thức nhận lãi: **Cuối kỳ**")
        st.write(
            "💡 Lý do: Ưu tiên tính linh hoạt và có thể sử dụng "
            "tiền khi cần."
        )

    elif doi_tuong == "Người đi làm, thu nhập ổn định":
        st.success("💼 Gợi ý cho bạn")
        st.write("• Kỳ hạn tham khảo: **6–12 tháng**")
        st.write("• Hình thức nhận lãi: **Cuối kỳ**")
        st.write(
            "💡 Lý do: Có thu nhập ổn định nên có thể dành "
            "một phần tiền nhàn rỗi cho kỳ hạn dài hơn."
        )

    elif doi_tuong == "Gia đình có khoản tiền nhàn rỗi":
        st.success("👨‍👩‍👧 Gợi ý cho bạn")
        st.write("• Kỳ hạn tham khảo: **6–12 tháng**")
        st.write("• Hình thức nhận lãi: **Hàng quý hoặc cuối kỳ**")
        st.write(
            "💡 Lý do: Phù hợp với khoản tiền chưa cần sử dụng "
            "ngay trong thời gian trung hạn."
        )

    elif doi_tuong == "Người lớn tuổi / nghỉ hưu":
        st.success("👴 Gợi ý cho bạn")
        st.write("• Kỳ hạn tham khảo: **3–6 tháng**")
        st.write("• Hình thức nhận lãi: **Hàng tháng hoặc hàng quý**")
        st.write(
            "💡 Lý do: Có thể ưu tiên dòng tiền lãi định kỳ "
            "để phục vụ chi tiêu."
        )

    else:
        st.success("💼 Gợi ý cho bạn")
        st.write("• Kỳ hạn tham khảo: **1–3 tháng**")
        st.write("• Hình thức nhận lãi: **Cuối kỳ**")
        st.write(
            "💡 Lý do: Ưu tiên tính linh hoạt vì có thể cần "
            "tiền cho hoạt động kinh doanh."
        )

    st.caption(
        "⚠️ Đây là gợi ý tham khảo phục vụ mục đích học tập, "
        "không phải tư vấn tài chính cá nhân."
    )
st.divider()


# ==============================
# NHẬP THÔNG TIN
# ==============================

st.subheader("📋 Thông tin khoản tiền gửi")

tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=100000,
    value=100000000,
    step=1000000
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    max_value=600,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

loai_lai = st.selectbox(
    "Phương pháp tính lãi",
    [
        "Lãi đơn",
        "Lãi kép"
    ]
)

hinh_thuc_nhan = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Lãnh lãi hàng tháng",
        "Lãnh lãi hàng quý",
        "Lãnh lãi cuối kỳ"
    ]
)


st.divider()


# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Lãi suất dạng thập phân
    r = lai_suat / 100

    # Kỳ hạn tính theo năm
    so_nam = ky_han / 12


    # ==========================================
    # LÃI ĐƠN
    # ==========================================

    if loai_lai == "Lãi đơn":

        # Tổng lãi trong toàn bộ kỳ hạn
        tong_lai = tien_gui * r * so_nam

        # Lãi mỗi tháng
        lai_thang = tien_gui * r / 12

        # Lãi mỗi quý
        lai_quy = tien_gui * r / 4

        # Xác định tiền lãi định kỳ
        if hinh_thuc_nhan == "Lãnh lãi hàng tháng":

            lai_dinh_ky = lai_thang

        elif hinh_thuc_nhan == "Lãnh lãi hàng quý":

            lai_dinh_ky = lai_quy

        else:

            lai_dinh_ky = tong_lai

        tong_tien = tien_gui + tong_lai


    # ==========================================
    # LÃI KÉP
    # ==========================================

    else:

        # Lãi kép theo tháng
        if hinh_thuc_nhan == "Lãnh lãi hàng tháng":

            so_ky = ky_han
            lai_suat_ky = r / 12

            tong_tien = tien_gui * (
                1 + lai_suat_ky
            ) ** so_ky

            tong_lai = tong_tien - tien_gui

            # Lãi của kỳ đầu tiên
            lai_dinh_ky = tien_gui * lai_suat_ky


        # Lãi kép theo quý
        elif hinh_thuc_nhan == "Lãnh lãi hàng quý":

            so_ky = ky_han / 3
            lai_suat_ky = r / 4

            tong_tien = tien_gui * (
                1 + lai_suat_ky
            ) ** so_ky

            tong_lai = tong_tien - tien_gui

            # Lãi của kỳ đầu tiên
            lai_dinh_ky = tien_gui * lai_suat_ky


        # Lãi kép cuối kỳ
        else:

            tong_tien = tien_gui * (
                1 + r
            ) ** so_nam

            tong_lai = tong_tien - tien_gui

            lai_dinh_ky = tong_lai


    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ Đã tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "💵 Tiền lãi định kỳ",
            format_money(lai_dinh_ky)
        )

        st.metric(
            "📈 Tổng tiền lãi",
            format_money(tong_lai)
        )

    with col2:

        st.metric(
            "🏦 Tiền gốc",
            format_money(tien_gui)
        )

        st.metric(
            "💰 Tổng gốc + lãi",
            format_money(tong_tien)
        )


    # ==============================
    # THÔNG TIN CHI TIẾT
    # ==============================

    st.divider()

    st.subheader("📝 Chi tiết khoản gửi")

    st.write(
        f"**Số tiền gửi:** {format_money(tien_gui)}"
    )

    st.write(
        f"**Kỳ hạn:** {ky_han} tháng"
    )

    st.write(
        f"**Lãi suất:** {lai_suat:.2f}%/năm"
    )

    st.write(
        f"**Phương pháp:** {loai_lai}"
    )

    st.write(
        f"**Hình thức nhận lãi:** {hinh_thuc_nhan}"
    )


    # ==============================
    # CÔNG THỨC
    # ==============================

    with st.expander("📐 Xem công thức"):

        if loai_lai == "Lãi đơn":

            st.markdown(
                """
                **Lãi đơn:**

                Tiền lãi = Tiền gốc × Lãi suất × Thời gian

                Phần lãi không được cộng vào tiền gốc.
                """
            )

        else:

            st.markdown(
                """
                **Lãi kép:**

                Tổng tiền = Tiền gốc × (1 + lãi suất kỳ) ^ số kỳ

                Phần lãi được cộng vào gốc để tiếp tục
                sinh lãi ở các kỳ tiếp theo.
                """
            )


    # ==============================
    # LƯU Ý
    # ==============================

    st.info(
        "ℹ️ Kết quả mang tính chất tham khảo. "
        "Lãi suất và phương pháp tính thực tế có thể "
        "khác nhau tùy theo quy định của từng ngân hàng."
    )


# ==============================
# CHÂN TRANG
# ==============================

st.divider()

st.caption(
    "💰 Ứng dụng tính lãi tiền gửi tiết kiệm"
)
