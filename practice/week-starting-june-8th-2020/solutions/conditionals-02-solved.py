# There are four seasons. Each season starts as another one comes to an end. 
# Spring begins with the Vernal Equinox, Thursday, March 19, 2020, 11:50 p.m.
# Summer begins with the Summer Solstice, Saturday, June 20, 2020, 5:44 p.m.
# Autumn begins with the Autumnal Equinox, Tuesday, September 22, 2020, 9:31 a.m.
# Winter begins with the Winter Solstice, Monday, December 21, 2020, 5:02 a.m.


# 1) Write a function called season_teller that takes a number corresponding to a month (1-12) and prints the season that is in effect during that month. If the that month observes a season change, print the season that is in effect at the start of the month as well as information about when the season will change. 

# Example: if the number is:

    # 5 ==> "It's Spring."
    # 8 ==> "Summer"
    # 6 ==> "June marks the end of Spring and the beginning of Summer with the Summer Solstice, Saturday, June 20, 2020, 5:44 p.m."
    # 13 ==> "Theres no 13th month, please enter a number 1-12"


# # # # # # # # # # # # # #    S O L U T I O N    # # # # # # # # # # # # # #


def season_teller(month_num):
  if month_num > 0 and month_num < 3:
    print("It's Winter")
  elif month_num > 3 and month_num < 6:
    print("It's Spring")
  elif month_num > 6 and month_num < 9:
    print("It's Summer")
  elif month_num > 9 and month_num < 12:
    print("It's Autumn")
  elif month_num == 3:
    print("March marks the end of Winter and the beginning of Spring with the Vernal Equinox, Thursday, March 19, 2020, 11:50 p.m.")
  elif month_num == 6:
    print("June marks the end of Spring and the beginning of Summer with the Summer Solstice, Saturday, June 20, 2020, 5:44 p.m.")
  elif month_num == 9:
    print("September marks the end of Summer and the beginning of Autumn with  the Autumnal Equinox, Tuesday, September 22, 2020, 9:31 a.m.")
  elif month_num == 12: 
    print("December marks the end of Autumn and the beginning of Winter with the Winter Solstice, Monday, December 21, 2020, 5:02 a.m.")
  else:
    to_string = str(month_num)
    if to_string[:-2] == "13":
      suffix = "th"
    elif to_string[-1] == "1":
      suffix = 'st'
    elif to_string[-1] == "2":
      suffix = 'nd'
    elif to_string[-1] == "3":
      suffix = 'rd'
    else:
      suffix = 'th'
    print("Theres no {month_num}{suffix} month, please enter a number 1-12".format(month_num = month_num, suffix = suffix))


season_teller(20)
  

