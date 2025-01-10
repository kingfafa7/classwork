#Mustafa Hasan Ali
#12/12/2024

first_name=str(input("Enter your first name: "))
last_name=str(input("Enter your last name: "))
age=int(input("Enter your age: "))

print()
print("Hello",first_name,last_name)
print("you are age years old","so you should be this tall")

for _ in range(age):
    print("*")