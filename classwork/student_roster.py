counter = 0
run_program = True
student_dict = {}
while run_program == True:
    counter = counter + 1
    first_name = input("Please give us the student's first name: ")
    last_name = input("Please give us the student's last name: ")
    grade = input("Please give us the student's grade level: ")
    student_dict['student' + str(counter) + '1'] = first_name + last_name
    student_dict['student' + str(counter) + '2'] = grade
    student_dict['student' + str(counter) + '3'] = len(first_name)
    student_dict['student' + str(counter) + '4'] = len(last_name)
    end_prompt = input("Do you want to add more students?['y' or 'n'] ")
    while end_prompt != 'y' and end_prompt != 'n':
        print("Not a valid response.")
        end_prompt = input("Do you want to add more students?['y' or 'n'] ")
        if end_prompt == 'n':
            run_program = False
for student in len(student_dict)/4:
    student_name = student_dict['student' + str(student) + '1']
    student_grade = student_dict['student' + str(student) + '2']
    first_name_len = student_dict['student' + str(counter) + '3']
    last_name_len = student_dict['student' + str(counter) + '4']
    print("{} {} in {}".format(student_name))