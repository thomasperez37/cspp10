seconds = input("Please input the number of seconds: ")
minutes = int(seconds)/60
hours = int(minutes)/60
print(str(int(seconds)) + " seconds is " + str(int(hours)) + " hours, " + str(int(minutes)) + " minutes, and " + str(int(seconds)%60) + " seconds.")