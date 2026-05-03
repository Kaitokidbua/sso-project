import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb

st.title("📊 วิเคราะห์สถิติประกันสังคม")

@st.cache_data
def get_cleaned_data():
    # ใช้ DuckDB อ่านไฟล์ทั้งหมดในโฟลเดอร์ cleaned_data
    con = duckdb.connect()
    # ถ้ายังไม่ได้รัน data_cleaning.py จะยังไม่มีไฟล์ cleaned_data/
    try:
        df = con.execute("SELECT * FROM 'cleaned_data/*.csv'").df()
        return df
    except:
        return pd.DataFrame()

df = get_cleaned_data()

if df.empty:
    st.warning("⚠️ ไม่พบข้อมูลที่คลีนแล้ว กรุณาตรวจสอบโฟลเดอร์ cleaned_data")
else:
    # กราฟเปรียบเทียบแต่ละปี
    st.subheader("แนวโน้มผู้ประกันตนรายมาตรา")
    fig = px.bar(df, x="ปี", color="มาตรา", template="plotly_dark", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("📌 ข้อมูลนี้ช่วยให้คุณเห็นว่าในแต่ละปีมีการเคลื่อนย้ายแรงงานอย่างไร")
