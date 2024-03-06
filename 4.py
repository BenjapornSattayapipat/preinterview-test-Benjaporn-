from datetime import datetime, timedelta

def check_date_range(start_date, end_date, target_date):
    # แปลงวันที่จาก string เป็น datetime object
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')
    target_date = datetime.strptime(target_date, '%d-%m-%Y')

    # ตรวจสอบว่าวันที่ m อยู่ในช่วงระยะเวลา x ถึง y หรือไม่
    if start_date <= target_date <= end_date:
        # คำนวณห่างจากวันที่ x ถึง m
        days_difference = (target_date - start_date).days
        return True, days_difference
    else:
        # คำนวณห่างจากวันที่ x ถึง m
        days_difference = (target_date - start_date).days
        return False, days_difference
        

# รับวันที่ x, y และ m จากผู้ใช้
x = input("ป้อนวันที่เริ่มต้น (รูปแบบ:วัน-เดือน-ปี, เช่น 09-09-2024): ")
y = input("ป้อนวันที่สิ้นสุด (รูปแบบ: วัน-เดือน-ปี, เช่น 09-09-2024): ")
m = input("ป้อนวันที่ที่ต้องการตรวจสอบ (รูปแบบ: วัน-เดือน-ปี, เช่น 10-09-2024): ")

# เรียกใช้ฟังก์ชันเพื่อตรวจสอบ
result, days_difference = check_date_range(x, y, m)

# แสดงผลลัพธ์
if result:
    print(f"true ,{days_difference} วัน")
else:
    print(f"false ,{days_difference} วัน")
