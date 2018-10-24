#BMI calculator
name1 = "matt s"
height_m1 = 5
weight_kgl = 90

name2 = "meagan s"
height_m2 = 3.5
weight_kg2 = 70

name3 = "dena d"
height_m3 = 1.2
weight_kg3 = 80

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi:",int(bmi))
    #print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kgl)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)