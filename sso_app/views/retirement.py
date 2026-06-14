"""หน้าวางแผนเกษียณ/บำนาญ (เพื่อนทำต่อ)"""
import streamlit as st
from lib.auth import require_login, get_profile

require_login()
st.title("🏖️ วางแผนเกษียณ / บำนาญ")
prof = get_profile()
years = prof.get("months_contributed", 0) // 12
st.metric("ส่งสมทบมาแล้ว", f"{years} ปี")
st.info("TODO: คำนวณบำนาญชราภาพจากอายุ + ปีสมทบ + ฐานเงินเดือนใน prof")
