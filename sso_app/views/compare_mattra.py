"""หน้าเทียบมาตรา (เพื่อนทำต่อ)"""
import streamlit as st
from lib.auth import require_login, get_profile

require_login()
st.title("⚖️ เทียบมาตรา 33 / 39 / 40")
prof = get_profile()
st.caption(f"ปัจจุบันคุณอยู่มาตรา {prof.get('mattra')}")
st.info("TODO: ตารางเทียบสิทธิประโยชน์ 3 มาตรา (ดึงจาก JSON ที่ทำไว้แชทเก่า)")
