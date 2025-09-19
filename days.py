num = int(input("Enter a number from 1 to 7: "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if 1 <= num <= 7:
    print("The day is:", days[num])
else:
    print("Invalid input! Please enter a number between 1 and 7.")

