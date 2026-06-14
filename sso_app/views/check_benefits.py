"""หน้าเช็คสิทธิ (เพื่อนทำต่อ) — ตัวอย่างการดึง profile จาก session"""
import streamlit as st
from lib.auth import require_login, get_profile

require_login()
st.title("✅ เช็คสิทธิของฉัน")

prof = get_profile()   # <-- ดึงข้อมูลที่ user กรอกหน้าแรก ไม่ต้องถามซ้ำ
st.write(f"คุณอยู่ **มาตรา {prof.get('mattra')}** ส่งสมทบมาแล้ว "
         f"**{prof.get('months_contributed')} เดือน** "
         f"ฐานเงินสมทบ **{prof.get('salary'):,} บาท**")

st.info("TODO: เอา rule-based advisor (SSOMasterAdvisor) จากแชทเก่ามาเสียบตรงนี้ "
        "แล้วคำนวณสิทธิจาก prof ได้เลย")
