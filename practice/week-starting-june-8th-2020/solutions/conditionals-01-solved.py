# 1) Setup your variables:
# a) Declare a variable 'is_summer' and set it to True
# b) Declare a variable 'temperature' and set it to 90
# c) Declare a variable 'is_raining' and set it to False


# 2) If statement number 1:
# a) Write an if statement that prints "Where are my shorts?" if is_summer is True.
# b) If summer is False print "I guess I'll wear pants today"


# 3) If statement number 2:
# a) Write another if statement that prints "Whoa, mucho caliente" if temperature is above 85.
# b) If temperature is below 85 print "Nice, the temperature is mild outside".


# 4) If statement number 3:
# a) Write another if statement that prints "Grab an umbrella" if is_raining is True.
# b) If is_raining is False print "Put the umbrella away!"


# 5) If statement number 4:
# a) Write an if statement that prints "Perfect day to catch Corona at the beach!" if is_summer is True, and temperature is above 85, and is_raining is False.
# b) Print "Stay in but blast the AC" if temperature is above 85 and is_raining is True.
# c) Print "Not hot enough for the beach...I guess no Corona for me :/" if is_summer is True and temperature is below 85
# d) Print "It's so hot it feels like summer" if is_summer is False and temperature is above 85

# # # # # # # # # # # # # #    S O L U T I O N    # # # # # # # # # # # # # #

is_summer = True
temperature = 83
is_raining = False

if is_summer == True:
    print("Where are my shorts?")
else:
    print("I guess I'll wear pants today.")

if temperature > 85:
    print('Whoa, mucho caliente!')
else:
    print("Nice, the temperature is mild outside.")

if is_raining == True:
    print("Grab an umbrella")
else:
    print("Put the umbrella away!")

if is_summer == True and is_raining == False and temperature > 85:
    print("Perfect day to catch Corona at the beach!")
elif is_raining == True and temperature > 85:
    print("Stay in but blast the AC")
elif is_summer == True and temperature < 85:
    print("Not hot enough for the beach...I guess no Corona for me :/")
elif is_summer == False and temperature > 85:
    print("It's so hot it feels like summer")
else:
    None
