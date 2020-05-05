try:
     file=open("C:\python35\test.txt","w")
     file.write("Hello python")
except IOError:
     print("Error cannot find file")
else:
     print("content written succesfully")
file.close()

try:
     c=int
     a=9
     b=0
     c=a/b
except ZeroDivisionError:
     print("Division by zero")


try:
     print(a)
except NameError:
     print("Value is not defined")



try:
     a=int(input("Enter an integer"))
     print(a)
except ValueError:
     print("Enter a valid integer number")


try:
     a=int(input("Enter a positive integer :"))
     if a <= 0 :
                raise ValueError("That is not possible")
except ValueError as ve:
           print(ve);;
