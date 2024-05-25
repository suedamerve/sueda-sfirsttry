import datetime
users=[]

while True:
    name=input("Write your name: ")
    surname=input("Write your surname: ")
    birthday=input("What is your birthday year: ")
    todays_date=datetime.date.today()
    age=todays_date.year - int(birthday)
    user={"Name":name,
          "Surname": surname,
          "Birthday":birthday,
          "Age":age}
    users.append(user)
    print(users)
    decision = input("To continue press Enter, To finish press q: ")
    if decision == "q":
        break
    else:
        continue
print(users)

   
    




































