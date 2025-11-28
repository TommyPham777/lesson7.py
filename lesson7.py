import streamlit as st

st.set_page_config(page_title="Trắc nghiệm tính cách", page_icon="❓", layout="wide")

def personality_quiz():
    st.title("Hãy chọn một con vật bạn yêu thích! 🤔")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        # Thêm emoji vào nút
        b1 = st.button("Con mèo 🐈")
    with col2:
        b2 = st.button("Con chó 🐕")
    with col3:
        b3 = st.button("Con sư tử 🦁")
    with col4:
        b4 = st.button("Con ngựa 🐴")
    with col5:
        b5 = st.button("Thiên nga 🦢")

    Personality = {
        'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được đi nghỉ. 🏝️',
        'Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra. 🤝',
        'Con sư tử': 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng. ✨',
        'Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn. ⛓️',
        'Thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé. 🥰'
    }

    if b1:
        with st.expander("Con mèo - Kết quả của bạn 😸"):
            st.write(Personality["Con mèo"])
    
    if b2:
        with st.expander("Con chó - Kết quả của bạn 🐶"):
            st.write(Personality["Con chó"])
    
    if b3:
        with st.expander("Con sư tử - Kết quả của bạn 👑"):
            st.write(Personality["Con sư tử"])
    
    if b4:
        with st.expander("Con ngựa - Kết quả của bạn 💨"):
            st.write(Personality["Con ngựa"])
    
    if b5:
        with st.expander("Thiên nga - Kết quả của bạn 💖"):
            st.write(Personality["Thiên nga"])

    with st.sidebar:
        st.header("Trạng thái lựa chọn")
        
        if b1:
            st.info("Con vật bạn chọn là con mèo 🐈")
        elif b2:
            st.info("Con vật bạn chọn là con chó 🐕")
        elif b3:
            st.info("Con vật bạn chọn là con sư tử 🦁")
        elif b4:
            st.info("Con vật bạn chọn là con ngựa 🐴")
        elif b5:
            st.info("Con vật bạn chọn là thiên nga 🦢")
        else:
            st.write("Vui lòng chọn một con vật.")

if __name__ == "__main__":
    personality_quiz()
