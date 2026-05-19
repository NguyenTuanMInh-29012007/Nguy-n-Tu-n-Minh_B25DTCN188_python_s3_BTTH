choice = ""

while choice != 'n':
    employee_number = int(input("Nhập số lượng nhân viên: "))
    for i in range(employee_number):
        name_employee = input("Nhập tên nhân viên: ")
        while(name_employee.strip() == ''):
            name_employee = input("[!] Lỗi. Tên khong được để trống. Vui lòng nhập lại!: ")

        number_of_working_days = int(input("Nhập số ngày đi làm: "))
        while(number_of_working_days < 0):
            number_of_working_days = int(input("[!] Lỗi. Số ngày làm nhập không hợp lệ! Vui lòng nhập lại: "))

        if(number_of_working_days < 20):
            message = "Cần cải thiện chuyên cần"
        else:
            message = "Nhân viên chuyên cần tốt"

        print(f"----Thông tin nhân viên: {employee_number - 1}----")
        print("Tên: ", name_employee)
        print("Số ngày đi làm: ", number_of_working_days)
        print(message)
        print("-----------------------------")

    choice = input("Tiếp tục chương trình? (y/n)")
    while(choice != 'y' and choice != 'n'):
        choice = input("[!] Lỗi: Hãy chọn (y/n): ")
else:
    print("Chương trình kết thúc!")