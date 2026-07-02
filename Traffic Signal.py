signal = input("Enter signal (Red/Yellow/Green): ")

if signal.lower() == "red":
    print("Stop")
elif signal.lower() == "yellow":
    print("Get Ready")
elif signal.lower() == "green":
    print("Go")
else:
    print("Invalid Signal")
