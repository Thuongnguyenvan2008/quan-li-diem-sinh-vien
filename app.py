import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu 10 sinh viên
data = {
    'Ho_va_ten': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyen_can': [8.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.5],
    'Giua_ky': [7.0, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 7.0, 7.0, 9.0],
    'Cuoi_ky': [8.5, 8.0, 6.5, 9.0, 7.5, 6.5, 8.5, 7.5, 8.0, 9.0]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết và xếp loại
df['Tong_ket'] = (0.2 * df['Chuyen_can']) + (0.3 * df['Giua_ky']) + (0.5 * df['Cuoi_ky'])
df['Tong_ket'] = df['Tong_ket'].round(2)

def xep_loai_chuan(dtk):
    if dtk >= 8.5:
        return 'Giỏi'
    elif dtk >= 7.0:
        return 'Khá'
    elif dtk >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai_chuan)

# 1. Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 2. Hiển thị thông tin thống kê
st.subheader("2. Thống kê chung")
diem_tb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(f"- **Sinh viên có điểm cao nhất:** {sv_max['Ho_va_ten']} (Điểm: {sv_max['Tong_ket']})")
st.write(f"- **Sinh viên có điểm thấp nhất:** {sv_min['Ho_va_ten']} (Điểm: {sv_min['Tong_ket']})")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}")

# 3. Chọn sinh viên xem chi tiết qua Selectbox
st.subheader("3. Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])

# Lọc thông tin sinh viên được chọn
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]
st.info(f"""
- **Họ và tên:** {student_info['Ho_va_ten']}
- **Điểm Chuyên cần:** {student_info['Chuyen_can']}
- **Điểm Giữa kỳ:** {student_info['Giua_ky']}
- **Điểm Cuối kỳ:** {student_info['Cuoi_ky']}
- **Điểm Tổng kết:** **{student_info['Tong_ket']}**
- **Xếp loại:** **{student_info['Xep_loai']}**
""")

# 4. Biểu đồ cột trực quan hóa
st.subheader("4. Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Ho_va_ten'], df['Tong_ket'], color='#4C72B0')
ax.set_xlabel('Điểm Tổng Kết')
ax.set_ylabel('Họ tên')
ax.set_title('Biểu đồ điểm tổng kết sinh viên')
ax.set_xlim(0, 10)
ax.invert_yaxis()
st.pyplot(fig)

# 5. Thông tin người tạo (chữ nhỏ ở cuối trang)
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Họ và tên: [Tên của bạn] - MSSV: [Mã số sinh viên của bạn]</p>", unsafe_allow_html=True)
