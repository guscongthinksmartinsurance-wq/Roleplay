import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN LUXURY ---
st.set_page_config(page_title="Thinksmart Training", page_icon="🛡️", layout="centered")

# CSS Nâng cao để làm đẹp các nút bấm và khung hiển thị
st.markdown("""
    <style>
    /* Nền tổng thể */
    .stApp {
        background-color: #F4F7F9;
    }
    
    /* Khung câu hỏi */
    .question-container {
        background-color: #001E3E;
        padding: 30px;
        border-radius: 20px;
        color: white;
        border-bottom: 5px solid #D4AF37;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    /* Nút bấm đáp án - Chỉnh chu & Hiệu ứng */
    .stButton>button {
        width: 100%;
        text-align: left !important;
        padding: 18px 25px !important;
        border-radius: 12px !important;
        border: 2px solid #E0E0E0 !important;
        background-color: white !important;
        color: #333 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        margin-bottom: 12px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }
    
    .stButton>button:hover {
        border-color: #D4AF37 !important;
        color: #D4AF37 !important;
        background-color: #FFF9E6 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(212, 175, 55, 0.2) !important;
    }

    /* Khung giải thích hiện ngay */
    .explanation-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #D4AF37;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }

    /* Tùy chỉnh Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001E3E;
    }
    .sidebar-text { color: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 class='sidebar-text' style='color: #D4AF37;'>THINKSMART</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'>Training System v2.0</p>", unsafe_allow_html=True)
    st.divider()
    st.write(f"📂 Bộ đề: **{len(QUESTIONS)} câu**")
    if st.button("🔄 LÀM MỚI"):
        st.session_state.clear()
        st.rerun()

# --- LOGIC XỬ LÝ ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

def go_next():
    st.session_state.current_q = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

q = st.session_state.current_q

# --- GIAO DIỆN CHÍNH ---
st.markdown(f"""
    <div class="question-container">
        <p style="color: #D4AF37; font-weight: bold; letter-spacing: 2px;">CÂU HỎI #{q['id']}</p>
        <h2 style="color: white; font-family: 'Segoe UI', sans-serif; line-height: 1.4;">{q['question']}</h2>
    </div>
    """, unsafe_allow_html=True)

# Hiển thị 4 đáp án (cân chỉnh dòng đàng hoàng)
for option in q['options']:
    # Kiểm tra nếu đã trả lời thì highlight đáp án đúng/sai bằng icon
    btn_label = option
    if st.session_state.answered:
        if option == q['answer']:
            btn_label = f"✅ {option}"
        elif option == st.session_state.user_choice:
            btn_label = f"❌ {option}"

    if st.button(btn_label, key=option, disabled=st.session_state.answered):
        st.session_state.user_choice = option
        st.session_state.answered = True
        st.rerun()

# HIỂN THỊ KẾT QUẢ VÀ GIẢI THÍCH (Hiển thị ngay không cần Expander)
if st.session_state.answered:
    if st.session_state.user_choice == q['answer']:
        st.success("**CHÍNH XÁC!**")
    else:
        st.error(f"**CHƯA ĐÚNG!** Đáp án chính xác là: {q['answer']}")
    
    # Khung giải thích chuyên sâu
    st.markdown(f"""
        <div class="explanation-box">
            <h4 style="color: #001E3E; margin-top: 0;">💡 TƯ DUY CHIẾN THUẬT:</h4>
            <p style="color: #444; line-height: 1.6; font-size: 16px;">{q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("TIẾP TỤC THỬ THÁCH ➡️", type="primary"):
        go_next()
        st.rerun()

st.markdown("---")
st.caption("Duy trì sự đúng đắn • Thinksmart Insurance 2026")
