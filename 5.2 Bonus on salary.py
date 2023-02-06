def salarycal(grade,salary):
    if(salary>10000):
        if(grade=='A'):
            salary=salary+(salary/5)
            print(salary)
        elif(grade=='B'):
            salary=salary+(salary/10)
            print(salary)
    else:
        if(grade=='A'):
            salary=salary+(salary/7)
            print(salary)
        elif(grade=='B'):
            salary=salary+(salary/12)
            print(salary)
grade=input("enter your grade like 'A' or 'B' ")
salary=int(input("enter ur salary: "))
salarycal(grade,salary)
