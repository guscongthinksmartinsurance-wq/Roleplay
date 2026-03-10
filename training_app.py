import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Thinksmart Training", page_icon="🛡️", layout="centered")

# CSS tập trung vào nút bấm và khung giải thích
st.markdown("""
    <style>
    /* 1. CHỈNH CHU 4 NÚT ĐÁP ÁN */
    .stButton>button {
        width: 100%;
        text-align: left !important;
        padding: 20px 25px !important;
        border-radius: 10px !important;
        border: 1px solid #E0E0E0 !important;
        background-color: #FFFFFF !important;
        color: #333333 !important;
        font-size: 16px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease !important;
    }
    
    /* Hiệu ứng khi rê chuột vào nút */
    .stButton>button:hover {
        border-color: #002B5C !important;
        background-color: #F0F4F8 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1) !important;
        color: #002B5C !important;
    }

    /* 2. CHỈNH CHU KHUNG GIẢI THÍCH HIỂN THỊ NGAY */
    .explanation-container {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #D4AF37;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Tiêu đề câu hỏi */
    .question-text {
        font-size: 22px;
        font-weight: 600;
        color: #002B5C;
        line-height: 1.5;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (GIỮ NGUYÊN ĐƠN GIẢN) ---
with st.sidebar:
    st.title("Thinksmart")
    st.write(f"Bộ đề: {len(QUESTIONS)} câu")
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
st.markdown(f"<p style='color: #666;'>CÂU HỎI #{q['id']}</p>", unsafe_allow_html=True)
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

# PHẦN GIẢI THÍCH HIỂN THỊ LUÔN KHI CHỌN XONG
if st.session_state.answered:
    st.divider()
    if st.session_state.choice == q['answer']:
        st.success("**CHÍNH XÁC!**")
    else:
        st.error(f"**CHƯA ĐÚNG!** Đáp án đúng là: {q['answer']}")
        
    st.markdown(f"""
        <div class="explanation-container">
            <p style="color: #D4AF37; font-weight: bold; margin-bottom: 5px;">💡 GIẢI THÍCH CHUYÊN SÂU:</p>
            <p style="color: #333; line-height: 1.6;">{q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("CÂU TIẾP THEO ➡️", type="primary"):
        next_q()
        st.rerun()
