import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN CHUYÊN NGHIỆP ---
st.set_page_config(
    page_title="Thinksmart Training Center",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: white;
        color: #002060;
        border: 1px solid #002060;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #002060;
        color: white;
    }
    div[data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
    }
    .question-box {
        background-color: #002060;
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
        border-left: 8px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR TINH GỌN ---
with st.sidebar:
    st.image("https://thinksmartinsurance.com/wp-content/uploads/2023/10/cropped-Thinksmart-Insurance-Logo.png", width=200) # Link logo minh họa
    st.markdown("---")
    st.markdown("### 🎓 LỘ TRÌNH ĐÀO TẠO")
    st.info(f"Tổng bộ đề: **{len(QUESTIONS)} Câu**")
    st.caption("Hãy tập trung vào tư duy xử lý tình huống thực tế thay vì chỉ nhớ đáp án.")
    
    if st.button("🔄 LÀM LẠI TỪ ĐẦU"):
        st.session_state.clear()
        st.rerun()

# --- LOGIC XỬ LÝ ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

def next_question():
    st.session_state.current_question = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

# --- GIAO DIỆN CHÍNH ---
st.title("🛡️ CHIẾN BINH THINKSMART")
st.write("Hệ thống luyện tập đối đáp & Kiến thức hưu trí Mỹ")

q = st.session_state.current_question

# Khung hiển thị câu hỏi
st.markdown(f"""
    <div class="question-box">
        <small>MÃ CÂU HỎI: #{q['id']}</small>
        <br>
        <p style="font-size: 20px; font-weight: 500;">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

# Hiển thị các đáp án
cols = st.columns(1) # Để dọc cho dễ đọc trên điện thoại
for option in q['options']:
    if st.button(option, disabled=st.session_state.answered):
        st.session_state.user_choice = option
        st.session_state.answered = True
        st.rerun()

# Phản hồi sau khi chọn
if st.session_state.answered:
    st.divider()
    if st.session_state.user_choice == q['answer']:
        st.success("✨ **CHÍNH XÁC!** Bạn đang đi đúng hướng.")
        st.balloons()
    else:
        st.error(f"⚠️ **CẦN LƯU Ý!** Đáp án đúng là: \n\n **{q['answer']}**")
    
    # Phần giải thích sâu sắc
    with st.container():
        st.markdown("#### 💡 TƯ DUY CỦA MANAGER:")
        st.info(q['explanation'])
        
        if st.button("TIẾP TỤC THỬ THÁCH ➡️", type="primary"):
            next_question()
            st.rerun()

# Footer
st.markdown("---")
st.caption("© 2026 Thinksmart Insurance Training System.")
