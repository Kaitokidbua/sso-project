import pandas as pd
import glob
import os

def clean_all_files():
    # 1. สร้างโฟลเดอร์เก็บไฟล์ที่สะอาดแล้ว
    output_dir = "cleaned_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. ไปดึงไฟล์ทั้งหมดในโฟลเดอร์ data/
    all_files = glob.glob("data/*.xlsx") + glob.glob("data/*.xls")
    
    for file in all_files:
        try:
            # อ่านไฟล์โดยข้ามหัวตารางที่รก (ส่วนใหญ่อยู่ 3 แถวแรก)
            df = pd.read_excel(file, skiprows=3)
            
            # ลบบรรทัดที่ไม่มีชื่อจังหวัด และลบบรรทัด "รวม" ออก
            df = df.dropna(subset=[df.columns[0]])
            df = df[~df.iloc[:, 0].str.contains("รวม|Total", na=False)]
            
            # ใส่ "ปี" เข้าไปโดยดูจากชื่อไฟล์
            if "2565" in file: df['ปี'] = 2565
            elif "2566" in file: df['ปี'] = 2566
            elif "2567" in file: df['ปี'] = 2567
            
            # เซฟเป็นไฟล์ใหม่ที่สะอาด
            filename = os.path.basename(file).replace(".xlsx", ".csv").replace(".xls", ".csv")
            df.to_csv(f"{output_dir}/cleaned_{filename}", index=False, encoding='utf-8-sig')
            
        except Exception as e:
            print(f"เกิดข้อผิดพลาดกับไฟล์ {file}: {e}")

if __name__ == "__main__":
    clean_all_files()