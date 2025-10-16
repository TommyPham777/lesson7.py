import streamlit as st

# 1. Cấu hình Trang
st.set_page_config(page_title="Trắc nghiệm tính cách", page_icon="question:", layout="wide")
st.title("Hãy chọn một con vật bạn yêu thích!")

# 2. Tạo Cột và Nút
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    b1 = st.button("Con mèo")
with col2:
    b2 = st.button("Con chó")
with col3:
    b3 = st.button("Con sư tử")
with col4:
    b4 = st.button("Con ngựa")
with col5:
    b5 = st.button("Thiên nga")

# 3. Từ điển Tính cách đã được sửa đổi với nội dung đầy đủ (hoặc giả định)
# LƯU Ý: Phần sau '...' là giả định vì không có nội dung gốc đầy đủ.
Personality = {
    "Con mèo": "Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát dục đi nhiệt, bạn cần một khoảng lặng để suy nghĩ về các mục tiêu cá nhân và cân bằng lại cảm xúc trước khi hành động.",
    "Con chó": "Bạn cam nhân dục sự hỗ trợ nhiệt tình của bạn bè và vị thế bạn là người có vẻ ngoài nói bật. Bạn luôn sẵn lòng giúp đỡ mọi người và được mọi người tin tưởng.",
    "Con sư tử": "Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hoa nhoáng và phong thái tự tin. Bạn sinh ra để làm lãnh đạo và luôn tìm kiếm sự công nhận.",
    "Con ngựa": "Có điều gì đó đang hạn chế sự tự do của bạn. Bạn cảm thấy bị ràng buộc bởi công việc hoặc trách nhiệm, và bạn mong muốn được khám phá và phiêu lưu nhiều hơn.",
    "Thiên nga": "Hiện tại bạn có khoảnh khắc thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé! Đây là giai đoạn của sự duyên dáng, hòa bình và phát triển cá nhân mạnh mẽ.",
}

# 4. Hiển thị Kết quả Chi tiết (Khu vực Chính)
if b1:
    with st.expander("Con mèo"):
        st.write(Personality["Con mèo"])

if b2:
    with st.expander("Con chó"):
        st.write(Personality["Con chó"])

if b3:
    with st.expander("Con sư tử"):
        st.write(Personality["Con sư tử"])

if b4:
    with st.expander("Con ngựa"):
        st.write(Personality["Con ngựa"])

if b5:
    with st.expander("Thiên nga"):
        st.write(Personality["Thiên nga"])

# 5. Hiển thị Lựa chọn Tóm tắt (Thanh Bên/Sidebar)
with st.sidebar:
    st.title("Trắc nghiệm tính cách")
    
    if b1:
        st.write("Con vật bạn chọn là con mèo")
    if b2:
        st.write("Con vật bạn chọn là con chó")
    if b3:
        st.write("Con vật bạn chọn là con sư tử")
    if b4:
        st.write("Con vật bạn chọn là con ngựa")
    if b5:
        st.write("Con vật bạn chọn là thiên nga")