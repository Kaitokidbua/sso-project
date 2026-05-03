import pandas as pd
import glob
import os

def clean_all_files():
    output_dir = "cleaned_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ดึงไฟล์ทั้งหมดจากโฟลเดอร์ data/ ที่บัวลากวางไว้
    all_files = glob.glob("data/*.xlsx") + glob.glob("data/*.xls")
    
    for file in all_files:
        try:
            # อ่านข้อมูล (ข้ามหัวตารางราชการ 3 แถวแรก)
            df = pd.read_excel(file, skiprows=3)
            
            # ลบแถวว่างและแถว "รวม" เพื่อไม่ให้กราฟเพี้ยน
            df = df.dropna(subset=[df.columns[0]])
            df = df[~df.iloc[:, 0].str.contains("รวม|Total", na=False)]
            
            # ระบุปีจากชื่อไฟล์
            year = "2567"
            if "2565" in file: year = "2565"
            elif "2566" in file: year = "2566"
            
            df['ปี'] = year
            
            # เซฟเป็น CSV เพื่อความเร็ว
            filename = os.path.basename(file).replace(".xlsx", ".csv").replace(".xls", ".csv")
            df.to_csv(f"{output_dir}/cleaned_{filename}", index=False, encoding='utf-8-sig')
            print(f"Cleaned: {filename}")
        except Exception as e:
            print(f"Error {file}: {e}")

if __name__ == "__main__":
    clean_all_files()
