"""หน้า AI Chatbot — โหมด AI (เพื่อนทำต่อ / เอา Gemma มาเสียบ)"""
import streamlit as st
from lib.auth import require_login, get_profile

require_login()
st.title("🤖 ผู้ช่วย AI (Gemma)")
prof = get_profile()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for m in st.session_state["messages"]:
    st.chat_message(m["role"]).write(m["content"])

if q := st.chat_input("ถามเรื่องประกันสังคม..."):
    st.session_state["messages"].append({"role": "user", "content": q})
    st.chat_message("user").write(q)
    # TODO: ส่ง q + prof (context) ไปที่ Gemma API / FastAPI backend แชทเก่า
    ans = f"(ตัวอย่าง) จะตอบโดยอิงว่าคุณเป็นมาตรา {prof.get('mattra')}"
    st.session_state["messages"].append({"role": "assistant", "content": ans})
    st.chat_message("assistant").write(ans)
