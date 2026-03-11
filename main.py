
weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds? (k or l): ")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 1)} {unit}")


weight = float(input("Enter the weight: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

area = weight * width * height

print(f"The area is {area}")
