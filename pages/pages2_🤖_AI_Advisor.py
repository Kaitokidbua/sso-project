import streamlit as st

st.title("🤖 ปรึกษา AI เรื่องประกันสังคม")

if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงแชท
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("พิมพ์คำถามได้เลย เช่น ลาออกแล้วจะต่อ ม.39 คุ้มไหม?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # คำแนะนำจำลอง (ในอนาคตเชื่อมต่อ API)
    response = "จากการวิเคราะห์ข้อมูลของคุณ หากย้ายจาก ม.33 ไป ม.40 ทันที สิทธิว่างงานจะหายไป แนะนำให้ตรวจสอบเงินสะสมชราภาพเดิมก่อนครับ"
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
