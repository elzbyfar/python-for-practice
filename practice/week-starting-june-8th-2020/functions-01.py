
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Given the above data structure, write a function called translate_to_month. The function should take an argument of a number and return the month which corresponds to the number. If the number is negative or greater than 12, alert the user to provide an appropriate number.

# Examples: If the user inputs:
# 3 ==> "March"
# 8 ==> "October"
# 41 ==> "Please provide an appropriate number"


def translate_to_month(num):
    return months[num]


print(translate(2))
