# can i create a function that allows me to switch between km to miles and miles to km?

distance = float(input("Enter Distance: "))
#distance = 100
measure = input("Enter 'miles or km': ")
#measure = "miles"

if measure == "miles":
    def convert_km(distance):
        return 1.6 * distance
    km_output = convert_km(distance)
    print(distance, "miles equals", round(km_output, 2), "km's")
elif measure == "km":
    def convert_m(distance):
        return 0.625 * distance # update formula
    miles_output = convert_m(distance)
    print(distance, "km's equals", round(miles_output,2), "miles")
else:
    print("Error: enter correct measure (miles/km)")



