#
# July 14, 2021
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
#

import student as student
import billing as billing


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # ------------------------------------------------
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    in_state_list = ['1001', '1003']
    course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    course_hours = [3, 4, 5, 3]
    max_size_list = [3, 2, 1, 3]
    roster_list = [['1004', '1003'], ['1001'], ['1002'], []]
    s_list = student_list
    i_s_list = in_state_list
    c_list = course_list
    h_list = course_hours
    m_list = max_size_list
    r_list = roster_list

    while True:
        id = input("Enter ID to login, or 0 to quit: ")
        if int(id) == 0:
            exit()
        if login(id, student_list):  # Verifies student's identity
            while True:
                user_input = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
                if user_input == 0:
                    print("Session ended.")
                    print()
                    break
                elif user_input == 1:
                    student.add_course(id, c_list, r_list, m_list)
                    billing.calculate_hours_and_bill(id, i_s_list, r_list, h_list)
                elif user_input == 2:
                    student.drop_course(id, c_list, r_list)
                    billing.calculate_hours_and_bill(id, i_s_list, r_list, h_list)
                elif user_input == 3:
                    student.list_courses(id, c_list, r_list)
                    billing.calculate_hours_and_bill(id, i_s_list, r_list, h_list)
                elif user_input == 4:
                    hours, total_cost = billing.calculate_hours_and_bill(id, in_state_list, roster_list, course_hours)
                    billing.display_hours_and_bill(hours, total_cost)
                else:
                    print("Invalid entry")


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input("Enter PIN: ")
    for a in range(len(s_list)):
        if id in s_list[a]:
            if pin == s_list[a][1]:
                print("ID and PIN verified." + "\n")
                return True
            else:
                print("ID or PIN incorrect." + "\n")
                return False

    print("ID or PIN incorrect." + "\n")
    return False


main()
