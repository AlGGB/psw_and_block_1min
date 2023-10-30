import time

user = "Petr"
psw = "abc123"

for i in range(3):
    usuario = input("write your user: ")
    password = input("write your password: ")
    if usuario == user and password == psw:
        break
    

if psw == password and user == usuario:
 print(f"welcome, {user}")
     
else:
     print("access denied ")
     print("Wait 1 min and try again")
wait = 60
time.sleep(wait)





    