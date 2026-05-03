# 🏥 SSO Smart Planner (ประกันสังคมฉบับประชาชน)

โปรเจกต์วิเคราะห์ข้อมูลและวางแผนสวัสดิการประกันสังคมไทย เพื่อช่วยให้ผู้ประกันตนเข้าถึงสิทธิประโยชน์ได้ง่ายขึ้นและไม่เสียสิทธิ์เมื่อเปลี่ยนงาน

## ✨ ฟีเจอร์หลัก
1. **Dashboard วิเคราะห์เทรนด์:** ดูการเคลื่อนย้ายแรงงานรายจังหวัดย้อนหลัง 3 ปี (2565-2567)
2. **AI Advisor:** ปรึกษาปัญหากฎหมายประกันสังคมผ่านแชทบอทที่เข้าใจบริบทข้อมูลจริง
3. **Welfare Planner:** เครื่องมือคำนวณเงินบำนาญชราภาพแบบเข้าใจง่าย

## 🛠 เทคโนโลยีที่ใช้
- **Frontend:** Streamlit (Theme: Dark Mode)
- **Database:** DuckDB (ใช้ Query ไฟล์ Excel ความเร็วสูง)
- **Data:** Pandas & Plotly
- **AI:** Google Gemini API (หรือ OpenAI)

## 🚀 วิธีติดตั้ง
1. Clone repository: `https://github.com/Kaitokidbua/sso-project`
2. ติดตั้ง library: `pip install -r requirements.txt`
3. รันแอป: `streamlit run app.py`

## 📊 ข้อมูลที่ใช้อ้างอิง
- SSO Data Catalog (data.go.th) ปี 2565-2567