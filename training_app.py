import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Thinksmart Training", page_icon="🛡️", layout="centered")

# CSS Tập trung đúng yêu cầu: Sidebar Cam 3D và Hover Nút trắc nghiệm
st.markdown("""
    <style>
    /* 1. SIDEBAR CHỮ CAM 3D NỔI BẬT */
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] span {
        color: #FF8C00 !important; /* Màu cam đậm */
        font-weight: bold !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3) !important; /* Hiệu ứng 3D đổ bóng */
        font-size: 18px !important;
    }

    /* 2. HIỆU ỨNG HOVER CHO 4 NÚT TRẮC NGHIỆM */
    .stButton>button {
        width: 100%;
        text-align: left !important;
        padding: 18px 25px !important;
        border-radius: 8px !important;
        border: 1px solid #D1D5DB !important;
        background-color: #F9FAFB !important;
        color: #111827 !important;
        font-size: 16px !important;
        margin-bottom: 8px !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; /* Hiệu ứng mượt */
    }
    
    .stButton>button:hover {
        border-color: #D4AF37 !important;
        background-color: #FFFFFF !important;
        color: #002B5C !important;
        transform: translateY(-3px) scale(1.02); /* Nút nổi lên và to ra nhẹ */
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    }

    /* KHUNG GIẢI THÍCH NAVY & GOLD (GIỮ NGUYÊN) */
    .explanation-container {
        background-color: #002B5C;
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #D4AF37;
        margin-top: 25px;
        color: #FFFFFF;
    }
    
    .question-text {
        font-size: 24px;
        font-weight: 700;
        color: #002B5C;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CHỮ CAM 3D) ---
with st.sidebar:
    st.markdown("### THINKSMART")
    st.markdown("Training System")
    st.markdown(f"Tiến độ: {len(QUESTIONS)} câu")
    if st.button("Làm mới bộ đề"):
        st.session_state.clear()
        st.rerun()

# --- LOGIC ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.choice = None

def next_q():
    st.session_state.current_q = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.choice = None

q = st.session_state.current_q

# --- GIAO DIỆN CHÍNH ---
st.markdown(f"<p style='color: #D4AF37; font-weight: bold;'>CÂU HỎI #{q['id']}</p>", unsafe_allow_html=True)
st.markdown(f"<div class='question-text'>{q['question']}</div>", unsafe_allow_html=True)

# 4 Đáp án trắc nghiệm
for opt in q['options']:
    label = opt
    if st.session_state.answered:
        if opt == q['answer']:
            label = f"✅ {opt}"
        elif opt == st.session_state.choice:
            label = f"❌ {opt}"
            
    if st.button(label, key=opt, disabled=st.session_state.answered):
        st.session_state.choice = opt
        st.session_state.answered = True
        st.rerun()

# PHẦN GIẢI THÍCH (GIỮ NGUYÊN)
if st.session_state.answered:
    st.markdown(f"""
        <div class="explanation-container">
            <p style="color: #D4AF37; font-weight: bold; font-size: 18px; margin-bottom: 10px;">💡 TƯ DUY XỬ LÝ:</p>
            <p style="line-height: 1.6; font-size: 16px;">{q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("TIẾP TỤC ➡️", type="primary"):
        next_q()
        st.rerun()
