import streamlit as st
import google.generativeai as genai

st.title("🤖 ผู้ช่วย AI ปรึกษาสิทธิประกันสังคม")

# ตั้งค่า API Key (ต้องใส่ใน Streamlit Secrets)
# genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.chat_message("assistant").write("สวัสดีครับ ผมคือ AI ผู้เชี่ยวชาญด้านประกันสังคม มีอะไรอยากให้ผมช่วยวางแผนไหมครับ?")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# แสดงประวัติการแชท
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("ตัวอย่าง: อายุ 28 ส่งมา 3 ปี ลาออกแล้วสิทธิหายไหม?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # ส่วนนี้คือ Logic การส่ง Prompt (จำลองคำตอบ)
    response = f"ตอบคุณ: {prompt} \n\n (ในระบบจริง AI จะนำข้อมูลจากไฟล์ Excel ปี 2567 และกฎหมายมาตรา 33, 39, 40 มาประมวลผลให้คุณครับ)"
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)