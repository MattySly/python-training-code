# calculator for KM to Mile conversion

miles = 100

def convert(miles):
    return 1.6 * miles
km = convert(miles)
if miles < 400:
    print(miles, "miles is equals", round(km, 2) ,"km's")
else:
    print("that's too many to count")


