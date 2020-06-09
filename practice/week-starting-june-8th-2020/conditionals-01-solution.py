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
