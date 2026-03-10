import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Thinksmart Training", page_icon="🛡️", layout="centered")

# CSS tập trung vào nút bấm và khung giải thích (BỎ MÀU ĐỎ GẮT)
st.markdown("""
    <style>
    /* Nền App sáng sủa */
    .stApp {
        background-color: #FFFFFF;
    }

    /* 1. CHỈNH CHU 4 NÚT ĐÁP ÁN - MÀU NAVY & GOLD */
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
        transition: all 0.2s ease !important;
    }
    
    /* Hiệu ứng khi rê chuột: Đổi sang viền Gold, nền Navy nhạt */
    .stButton>button:hover {
        border-color: #D4AF37 !important;
        background-color: #F3F4F6 !important;
        color: #002B5C !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }

    /* 2. KHUNG GIẢI THÍCH SANG TRỌNG (NAVY & GOLD) */
    .explanation-container {
        background-color: #002B5C; /* Màu Navy đậm sang trọng */
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #D4AF37; /* Điểm nhấn Gold */
        margin-top: 25px;
        color: #FFFFFF; /* Chữ trắng cho dễ đọc */
    }
    
    .question-text {
        font-size: 24px;
        font-weight: 700;
        color: #002B5C;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR TRẮNG SÁNG ---
with st.sidebar:
    st.markdown("### THINKSMART")
    st.caption("Training System")
    st.write(f"Tiến độ: {len(QUESTIONS)} câu")
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

# PHẦN GIẢI THÍCH HIỂN THỊ NGAY - MÀU SANG TRỌNG
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
