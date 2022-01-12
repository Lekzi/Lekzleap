import time as t
import os
t.sleep(5)
x= "Enter a valid option!"
os.system ("clear")
print ("""Lekzleap is a python programme for checking leap year""")
t.sleep(8)
os.system("clear")
t.sleep(4)
def loop():
	os.system ("clear")
	os.system (" figlet Lekzleap Leap year Checker")
	t.sleep(6)
	print("""
	Tool Name:Lekzleap
	Creator:Lêkzï
	Team:Greyhax0rs
        Contact me on whatsapp:+2347064822519
        Special thanks to spider Anon greyhat for his support
        """)
	t.sleep(5)
print("Login to Lekzleap")
uname = input("Username: ")
pwd = input("Password: ")
print("Checking Username and password...") 
t.sleep(5)
if uname != "Lekzleap" and pwd != "Lekzleap@112":
  print("Incorrect Username or Password!")
  t.sleep(3)
  os.system("https://github.com/Lekzi/Lekzleap")
loop()
year = input('year you want to check: ')
year_num = int(year)

if year_num % 4 == 0:
    print(year_num, 'is a Leap Year')
else:
    print(year_num, 'is not a Leap Year')
