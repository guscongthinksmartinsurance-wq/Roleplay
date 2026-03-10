import streamlit as st
import random
from quiz_data import QUESTIONS

# Cấu hình trang
st.set_page_config(page_title="Thinksmart Training Center", page_icon="🎓", layout="centered")

# Giao diện tiêu đề
st.title("🎓 HỆ THỐNG ĐÀO TẠO AGENT")
st.subheader("Thinksmart Insurance - Chuyên nghiệp & Đúng đắn")
st.divider()

# Khởi tạo trạng thái câu hỏi trong session_state
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

def next_question():
    st.session_state.current_question = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.session_state.user_choice = None

# Hiển thị câu hỏi
q = st.session_state.current_question

st.info(f"**CÂU HỎI SỐ {q['id']}**")
st.markdown(f"### {q['question']}")

# Hiển thị các lựa chọn dưới dạng nút bấm
for option in q['options']:
    if st.button(option, use_container_width=True, disabled=st.session_state.answered):
        st.session_state.user_choice = option
        st.session_state.answered = True
        st.rerun()

# Xử lý sau khi trả lời
if st.session_state.answered:
    if st.session_state.user_choice == q['answer']:
        st.success("✅ CHÍNH XÁC! Bạn nắm kiến thức rất tốt.")
    else:
        st.error(f"❌ CHƯA ĐÚNG. Đáp án đúng là: **{q['answer']}**")
    
    # Phần giải thích sâu sắc của anh Công
    st.markdown("---")
    st.markdown("#### 💡 TƯ DUY XỬ LÝ:")
    st.write(q['explanation'])
    
    st.divider()
    if st.button("TIẾP TỤC BỐC QUẺ ➡️", on_click=next_question, type="primary"):
        pass

# Chân trang
st.sidebar.markdown("---")
st.sidebar.write("📌 **Lưu ý cho Agent:**")
st.sidebar.caption("Học không phải để đối phó, học để thấu hiểu tâm lý khách hàng và duy trì sự đúng đắn.")
st.sidebar.caption(f"Tổng số câu hỏi: {len(QUESTIONS)}")