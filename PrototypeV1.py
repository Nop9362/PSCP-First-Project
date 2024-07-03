"""check your class schedule"""

# def check_student_id(student_id):
#     """เช็ค row ที่ตรงกับรหัสนักศึกษาที่มีอยู่ใน Data รายชื่อนศ. (Student_Data)"""
#     ## ถ้ามันไม่มีให้ทำการกรอกใหม่ไปเรื่อยๆ จนกว่าจะมี หรือ ถ้าเจอคำว่า End ให้หยุดการทำงาน
#     if student_id in student_data['id'] :
#         #run function "check_schedule"

def main():
    student_data = ["67070125","67070086","67070052","67070116","67070063"]
    """receive input (Student_ID)"""
    your_student_id = input("Please Enter Your Student ID: ")
    while your_student_id != "End" :
        if your_student_id in student_data :
            #run function "check_schedule"
            # print subject and time
            # run function "add more student id?" opinion
            your_student_id = "End"
        else :
            print("Student_ID not found. Try again.")
            your_student_id = input("Please Enter Your Student ID: ")
    print("Thank you for using Qingque's 'check your class schedule' :)")
main()