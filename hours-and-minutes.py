import os

print("Enter 0 hours and 0 minutes to calculate total time.")

filePath = "hours-and-minutes.log"

hours = 0
inputHours = -1

minutes = 0
inputMinutes = -1

if os.path.exists(filePath):
    with open(filePath, "r") as f:
        data = f.readlines()
    if not data[0].strip():
        hours = 0
    elif data[0].strip():
        hours = int(data[0].strip())
    
    if not data[1].strip():
        minutes = 0
    elif data[1].strip():
        minutes = int(data[1].strip())

    print("====================")
    print("Recovered:")
    print(f"Hours: {hours}\nMinutes: {minutes}")
    print("====================")
    
    del data

while not (inputHours == 0 and inputMinutes == 0):
    inputHours = int(input("Hours: "))
    inputMinutes = int(input("Minutes: "))
    if not (inputHours == 0 and inputMinutes == 0):
        hours += inputHours
        minutes += inputMinutes
        with open(filePath, "w") as f:
            f.write(str(hours) + "\n" + str(minutes))
        print("Saved!")
        print("====================")
del inputHours
del inputMinutes

newHours = minutes // 60
leftOverMinutes = int(((minutes / 60) - newHours) * 60)

hours += newHours
minutes = leftOverMinutes

with open(filePath, "w") as f:
    f.write(str(hours) + "\n" + str(minutes))

print("====================")
print("Results:")
print(f"Hours: {hours}\nMinutes: {minutes}")
print("====================")
