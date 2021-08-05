#
# July 13, 2021
# This program calculates the course hours and cost of enrollment and display them
#

def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    # This function calculates the bill based on
    # $225 per credit hour for in-state students and $850 per credit hour for out-of-state students
    # After calculating the bill, the function returns the total number of credit hours and the total cost of enrollment.
    hours = 0
    for i in range(len(r_list)):
        if id in r_list[i]:
            hours += h_list[i]
    if id in i_s_list:
        cost = 225
    else:
        cost = 850
    total_cost = cost * hours
    return hours, total_cost


def display_hours_and_bill(hours, cost):
    # This function displays the total number of credit hours and the total cost of enrollment
    print("Course load: %s credit hours" % hours)
    print("Enrollment cost: $%0.2f" % cost)
    print()
