#A student will not be allowed to sit in exam if his attendance is less than 75%. take the following input from the user
#a) no of classes held
#b) no of classes attended
#and print percentage of class attended. Also print if the student is allowed to sit in exam or not
no_of_class_held=int(input("Enter number of classes held"))
no_of_class_attended=int(input("Enter number of classes attended"))
if(no_of_class_attended>no_of_class_held):
    print("Invalid input")
else:
    percentage=(no_of_class_attended/no_of_class_held)*100
    print("Percentage of attendance =", percentage, "%")
    if(percentage>=75):
        print("Eligible to sit in exam")
    else:
        print("Not eligible to sit in exam")
