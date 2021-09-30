userTemperature = float(input("enter your temperature : "))
covidAlert = False

if userTemperature <37 :
    covidAlert = False
    print("you temp is too low ")

elif userTemperature == 37 :

    covidAlert = False
    print(" your temperature is normal ")


else:
    covidAlert = True
    print("please your temperature is too high and you must be Quarantine !!")


