import os
import pyttsx3 

print("************************")

print()
print("Press 1 to open: Firefox")
print("Press 2 to open: Gedit")
print("Press 3 to open: VLC")
print("Press 4 to quit")
print()

while True:
 print("Enter your choice:")
 p=input()
 if int(p)==1:
  os.system("firefox")
 elif int(p)==2:
  os.system("gedit")
 elif int(p)==3:
  os.system("vlc")
 elif int(p)==4:
  break
 else:
  print("Not supported")
