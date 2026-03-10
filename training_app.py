import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Thinksmart Training", page_icon="🛠", layout="centered")

st.markdown("""
    <style>
    @keyframes shine {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] span {
        background: linear-gradient(to right, #BF953F 20%, #FCF6BA 40%, #B38728 60%, #FBF5B7 80%, #AA771C 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
        font-size: 20px !important;
        animation: shine 3s linear infinite; /* Hiệu ứng ánh kim chạy qua chạy lại */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1) !important;
        display: inline-block;
    }

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
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    
    .stButton>button:hover {
        border-color: #D4AF37 !important;
        background-color: #FFFFFF !important;
        color: #002B5C !important;
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    }

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

with st.sidebar:
    st.markdown("### THINKSMART INSURANCE")
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

st.markdown(f"<p style='color: #D4AF37; font-weight: bold;'>CÂU HỎI #{q['id']}</p>", unsafe_allow_html=True)
st.markdown(f"<div class='question-text'>{q['question']}</div>", unsafe_allow_html=True)

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


