import streamlit as st
import random
from quiz_data import QUESTIONS

# --- CẤU HÌNH UI/UX NÂNG CAO ---
st.set_page_config(page_title="Thinksmart Training Center", page_icon="🛡️", layout="centered")

# CSS để tùy biến giao diện Navy & Gold
st.markdown("""
    <style>
    /* Tổng thể nền */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Thanh Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001e3e;
        color: white;
    }
    
    /* Khung câu hỏi (Card) */
    .question-card {
        background-color: #002b5c;
        padding: 30px;
        border-radius: 20px;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 10px solid #d4af37;
        margin-bottom: 30px;
    }

    /* Tùy chỉnh nút bấm đáp án */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        border: 1.5px solid #002b5c;
        background-color: white;
        color: #002b5c;
        font-weight: 600;
        padding: 15px;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #d4af37;
        color: white;
        border-color: #d4af37;
    }

    /* Tiêu đề */
    h1 {
        color: #002b5c;
        font-family: 'Times New Roman', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CHỈNH CHU ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #d4af37;'>THINKSMART</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Duy trì sự đúng đắn</p>", unsafe_allow_html=True)
    st.divider()
    st.write(f"📊 Hệ thống: **100 Câu thực chiến**")
    st.write(f"🏷️ Trạng thái: **Đang hoạt động**")
    st.divider()
    if st.button("🔄 LÀM MỚI BỘ ĐỀ"):
        st.session_state.clear()
        st.rerun()

# --- LOGIC APP ---
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
st.title("🛡️ Đào Tạo Chiến Binh IUL")
st.write("Dành riêng cho đội ngũ Agent Thinksmart Insurance")

# Hiển thị câu hỏi trong khung Card
st.markdown(f"""
    <div class="question-card">
        <span style="color: #d4af37; font-weight: bold;">CÂU HỎI #{q['id']}</span>
        <p style="font-size: 22px; margin-top: 10px;">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

# Các nút đáp án
for opt in q['options']:
    if st.button(opt, disabled=st.session_state.answered, key=opt):
        st.session_state.choice = opt
        st.session_state.answered = True
        st.rerun()

# Hiển thị kết quả và giải thích sâu sắc
if st.session_state.answered:
    st.markdown("---")
    if st.session_state.choice == q['answer']:
        st.success("🎯 **CHÍNH XÁC!** Bạn nắm bắt tâm lý rất tốt.")
    else:
        st.error(f"🔴 **CẦN XEM LẠI!** Đáp án đúng là: **{q['answer']}**")
    
    with st.expander("📝 XEM GIẢI THÍCH TỪ MANAGER (ANH CÔNG)", expanded=True):
        st.write(q['explanation'])
    
    st.write("")
    if st.button("TIẾP TỤC BỐC QUẺ ➡️", type="primary"):
        next_q()
        st.rerun()
