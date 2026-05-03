import streamlit as st
import pandas as pd
import duckdb

# การตั้งค่าหน้าจอแบบ Dark Mode และภาษาไทย
st.set_page_config(
    page_title="SSO Smart Planner",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS เพื่อความสวยงามและอ่านง่าย
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #ffbd45 !important; font-family: 'Sarabun', sans-serif; }
    p, span { font-size: 18px !important; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ffbd45; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🏥 ประกันสังคมอุ่นใจ (SSO Smart Planner)")
    st.subheader("เช็กสิทธิ วิเคราะห์อนาคต เพื่อคนไทยทุกมาตรา")
    
    st.info("💡 ยินดีต้อนรับครับ! คุณสามารถเลือกเมนูทางด้านซ้ายเพื่อ 'ดูสถิติ' หรือ 'ปรึกษา AI' ได้เลย")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🧐 ปัญหายอดฮิตที่เราช่วยคุณได้:
        - "ลาออกจากงานแล้วต้องทำไงต่อ?"
        - "ส่งประกันสังคมมา 20 ปี ย้ายมาตราแล้วเงินหายจริงไหม?"
        - "อายุ 55 แล้ว จะได้เงินก้อนหรือเงินบำนาญเท่าไหร่?"
        """)
    
    with col2:
        st.image("https://www.sso.go.th/wpr/assets/default/images/sso_logo.png", width=200)

    st.divider()
    st.write("📌 จัดทำขึ้นเพื่อให้ข้อมูลประกันสังคมเข้าถึงง่ายที่สุดสำหรับทุกคน")

if __name__ == "__main__":
    main()