import os
import speech_recognition as sr
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
		os.system("date")
	elif (("process" in p) and (("show" in p) or ("all" in p))):
		os.system("ps -aux")
	elif ((("memory" in p) or("ram" in p) or("free" in p)) and (("show" in p) or ("all" in p))):
		os.system("free -m")
	elif ((("ipaddress" in p) or ("ip " in p) or ("IP" in  p) or ("Ip address" in p)) and (('show' in p) or("system" or p))):
		os.system("ifconfig wlp3s0")
	elif ((("mount" in p) or ("storage" in p)) and (("show" in p) or("all" in p))):
		os.system("df -h")
	elif ((("storage" in p) or ("partitions" in p)) and (("disk" in p))):
		os.system("fdisk -l")
	elif ((("web server" in p) or ("httpd" in p)) and (("status" in p))):
		os.system("systemctl status httpd")
	elif ((("web server" in p) or ("httpd" in p)) and (("Start" in p))):
		os.system("systemctl start httpd")
	elif ((("web server" in p) or ("httpd" in p)) and (("stop" in p))):
		os.system("systemctl stop httpd")
	elif ((("mini cube" in p) or("mini kube" in p) or ("mini cube cluster" in p)) and (("status" in p))):
		os.system("minikube status")
	elif ((("mini cube " in p) or ("mini kube" in p ) or ("mini cube cluster" in p)) and (("Start" in p))):
		os.system("minikube start")
	elif ((("minishift" in p) or ("mini cube cluster" in p)) and (("stop" in p))):
		os.system("minikube start")
	elif ((("minishift" in p) or ("mini shift" in p)) and (("status" in p))):
		os.system("minishift status")
	elif ((("minishift" in p) or ("mini shift" in p)) and (("start" in p))):
		os.system("minishift start")
	elif ((("mini cube" in p) or ("mini cube cluster" in p)) and (("stop" in p))):
		os.system("minishift stop")
	elif ((("docker" in p) or ("information" in p)) and (("show" in p))):
		os.system("docker info")
	elif ((("docker status" in p) or ("docker")) and (("status" in p))):
		os.system("systemctl status docker")
	elif ((("docker start" in p) or ("docker")) and (("start" in p))):
		os.system("systemctl start docker")
	elif ((("docker stop" in p) or ("docker")) and (("stop" in p))):
		os.system("systemctl stop docker")
	elif (("stop" in p) or ("stop the process" in p)):
		exit()
	else:
		print("not understand")