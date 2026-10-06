import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================

st.set_page_config(
    page_title="Tính Lãi Tiền Gửi Tiết Kiệm",
    page_icon="💰",
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