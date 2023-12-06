# import math
# print("Noten Berechnung\n")

# maxPunkt=float(input("give max.Punkt: "))
# erPunkt=float(input("erreichte Punkt: "))

# Prozente = erPunkt/maxPunkt * 100
# print(f"the total prozent from this is = {Prozente:.2f}%")

# if Prozente < 32:
#     print("Note 5")
# elif Prozente < 56:
#     print("Note 4")
# elif Prozente < 67:
#     print("Note 3")
# elif Prozente < 89:
#     print("Note 2")
# else:
#     print("Note 1") 

# street = input("What is ur street: ")
# print(street.capitalize() +" street")

# a=float(input("give a number "))
# b=float(input("give 2nd number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# Names lists
# names = ['ali', 'vali', 'tom', 'erik']
# print("Hi my friend " +names[1].upper()+" how ya doing".title())
# print("these ", names[0],"and", names[2], " guys are brothers")

# people=("Bob", "Tom", 'Erik', "Max", "Perry")
# for person in people:
#     print(f"hi bro {person}")

# numbers= list(range(11))
# sqrt_num=[]
# for number in numbers:
#     sqrt_num.append(number**2)
# print(numbers)
# print(sqrt_num)

# x= float(input("give a number: "))
# y=float(input("give second number: "))
# if x>y:
#     print("x>y")
# else:
#     print("x<y")


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh']

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")


# print(f"i really wanna see {t.pop(2)} as a person.\n But the problem is {z.pop(2)} he doesnt wanna talk")

# friends = []
# friends.append('John')
# friends.append('Alex')
# friends.append('Danny')
# friends.append('Sobirjon')
# friends.append('Vanya')
# print("hammasi bolib: ", len(friends))

# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)


# # Formatting numbers with a specific number of decimal places
# pi = 3.14159
# formatted_pi = f"The value of pi is approximately {pi:.2f}."

# # Using expressions and calling functions
# greeting = "Hello"
# formatted_greeting = f"{greeting.upper()} there!"

# # Using f-string with dictionary values
# person = {'name': 'Bob', 'age': 25}
# formatted_person = f"Person: {person['name']}, Age: {person['age']}"

# # Using f-string with expressions and multiline strings
# multiline_message = f"""
#     Dear {person['name']},
#     Thank you for your email.
#     Regards,
#     {greeting}
# """

# print(formatted_pi)
# print(formatted_greeting)
# print(formatted_person)
# print(multiline_message)
