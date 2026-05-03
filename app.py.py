import streamlit as st

st.set_page_config(page_title="SSO Smart Planner", page_icon="🏥", layout="wide")

# ปรับแต่งธีมให้ดูง่าย
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2 { color: #ffbd45 !important; }
    .stButton>button { background-color: #ffbd45; color: black; border-radius: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 ประกันสังคมอุ่นใจ (SSO Smart Planner)")
st.header("ยินดีต้อนรับครับ!")

st.info("💡 แอปนี้จะช่วยให้คุณเช็กสิทธิประโยชน์ และวางแผนชีวิตเมื่อต้องเปลี่ยนงานหรือเกษียณ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("มองหาอะไรอยู่ครับ?")
    st.write("- อยากรู้ว่าจังหวัดเรามีสิทธิอะไรบ้าง?")
    st.write("- ลาออกแล้วย้ายมาตรา เงินหายจริงไหม?")
    st.write("- ปรึกษา AI เรื่องสิทธิทำฟันหรือบำนาญ")

with col2:
    st.success("👈 เลือกเมนูทางซ้ายมือเพื่อเริ่มต้นใช้งานได้เลย!")

st.divider()
st.caption("จัดทำโดย: ทีมงาน SSO Smart Planner | ข้อมูลอ้างอิงจาก SSO Data Catalog")
