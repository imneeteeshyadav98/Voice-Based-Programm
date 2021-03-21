import os
import speech_recognition as sr
import webbrowser
os.system("banner CHAT")
r=sr.Recognizer()
while True:
	with sr.Microphone() as source:
		print('Start saying......')
		r.adjust_for_ambient_noise(source, duration=1)  
		audio=r.listen(source)
		print("we got it, plz wait")
	p=r.recognize_google(audio)
	#p=input()
	print(p)
	if (("date" in p)) and (("Run" in p) or("execute" in p)):
		#os.system("date")
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=date")
	elif (("process" in p) and (("show" in p) or ("all" in p))):
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=ps -aux")
	elif ((("memory" in p) or("ram" in p) or("free" in p)) and (("show" in p) or ("all" in p))):
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=free -m")
	elif ((("mount" in p) or ("storage" in p)) and (("show" in p) or("all" in p))):
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=df -h")
	elif ((("storage" in p) or ("partitions" in p)) and (("disk" in p))):
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=fdisk -l")
		#os.system("fdisk -l")
	elif ((("webserver" in p) or ("httpd" in p)) and (("status" in p))):
		webbrowser.get('firefox').open("http://192.168.0.104/cgi-bin/menu_based_web.py?x=fdisk -l")
	elif ("stop" in p):
		exit()
	else:
		print("not understand")