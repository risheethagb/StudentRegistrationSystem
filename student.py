#
# July 18, 2021
# This program defines 3 programs (list, add, and drop courses) for the class registration
#

def list_courses(id, c_list, r_list):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------
    count = 0
    sc_list = []
    for i in range(len(c_list)):  # This loop loops through the class rosters
        if id in r_list[i]:
            sc_list.append(c_list[i])
            count += 1
        else:
            continue
    print("Courses registered: ")
    for course in sc_list:
        print(course)
    print("Total number:", count)
    print()


def add_course(id, c_list, r_list, m_list):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    c = input("Enter course you want to add: ")
    if c in c_list:
        index = c_list.index(c)  # This saves the index number of where the course is found
        if len(r_list[index]) == m_list[index]:
            print("Course already full")
            print()
        elif id in r_list[index]:
            print("You are already enrolled in that course.")
            print()
        else:
            r_list[index].append(id)
            print("Course added")
            print()
    else:
        print("Course not found")
        print()


def drop_course(id, c_list, r_list):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------
    c = input("Enter course you want to drop: ")
    if c in c_list:
        index = c_list.index(c)  # This saves the index number of where the course is found
        if id not in r_list[index]:
            print("You are not enrolled in that course.")
            print()
        else:
            r_list[index].remove(id)
            print("Course dropped")
            print()
    else:
        print("Course not found")
        print()
