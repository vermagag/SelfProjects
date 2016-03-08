#!/usr/bin/python
#S3 including 3D OpenGLApps
#Script should run only in root mode(Super User).
#Developed by : gagan.verma@amd.com 

from time import sleep,ctime
import sys,os,dircache,random,commands,time,decimal

start_time = time.time()
choice = 0
dur = 0
cycles = 0

def check_utils():
	if not os.path.isfile('/usr/bin/cifs.idmap') and not os.path.isfile('/usr/bin/nfsidmap'):
		os.system("sudo apt-get install nfs-common cifs-utils")	
	
def glmark():
	glmark_check = os.path.isfile('/usr/bin/glmark2')
	if str(glmark_check) == 'False':	
		print('Please install GLMark2 by command "sudo apt-get install glmark2"')
		sleep(2)
		os.system("sudo apt-get install glmark2")
	print("Initiating S3 with "+str(cycles)+" cycles along with Glmark. Please wait !!!")				
	sleep(2)
	os.system("glmark2 --run-forever &")
	sleep(5)
	S3()
	os.system("killall glmark2")
def glxgears():
	global cycles
	glxgears_check = os.path.isfile('/usr/bin/glmark2')
	if str(glxgears_check) == 'False':	
		print('Please install Glxgears by command "sudo apt-get install mesa-utils"')
		sleep(2)
		os.system("sudo apt-get install mesa-utils")
	print("Initiating S3 with "+str(cycles)+" cycles along with Glxgears. Please wait !!!")				
	sleep(2)
	os.system("glxgears &")	
	sleep(5)
	S3()
	os.system("killall glxgears")

	
def furmark():
	furmark_check = os.path.isfile('/home/atitest/GpuTest_Linux_x64_0.7.0/start_furmark_windowed_1024x640.sh')
	if str(furmark_check) == 'False':	
		print("****Error****")
		print('Please copy "GpuTest_Linux_x64_0.7.0" from the server and extract to $home directory and run this script again."')
		sleep(2)
		yes = raw_input("If you want to copy and install automatically from server //hydingfs/ press (y/n) : ")
		if str(yes) == 'y' or str(yes)== 'Y':
			check_utils()
			if not os.path.exists('a'):
				os.makedirs('a')
			print("Initiating Server......")
			sleep(2)
			os.system("mount -t cifs -o username=taccuser,passwd=AH64_uh1 //hydingfs/cde_qa a/")
			print("Copying GpuTest_Linux_x64_0.7.0.zip from server to current location......")
			os.system("cp -f a/linux/OpenGL/GpuTest_Linux_x64_0.7.0.zip .")				
			os.system("unzip GpuTest_Linux_x64_0.7.0.zip")
						
		else:
			sys.exit(0)
	print("Initiating S3 with "+str(cycles)+" cycles along with Furmark_WindowMode. Please wait !!!")		
	sleep(2)
	os.system("chmod 777 /home/atitest/GpuTest_Linux_x64_0.7.0/start_furmark_windowed_1024x640.sh")
	os.chdir("/home/atitest/GpuTest_Linux_x64_0.7.0")	
	os.system("sh start_furmark_windowed_1024x640.sh &")
	sleep(5)
	S3()
	os.chdir("/home/atitest/")	
	os.system("killall GpuTest")
	sleep(2)	
	sys.exit(0)

def triangle():

	furmark_check = os.path.isfile('/home/atitest/GpuTest_Linux_x64_0.7.0/start_furmark_windowed_1024x640.sh')
	if str(furmark_check) == 'False':	
		print("****Error****")
		print('Please copy "GpuTest_Linux_x64_0.7.0" from the server and extract to $home directory and run this script again."')
		sleep(2)
		yes = raw_input("If you want to copy and install automatically from server //hydingfs/ press (y/n) : ")
		if str(yes) == 'y' or str(yes)== 'Y':
			if not os.path.exists('a'):
				os.makedirs('a')
			print("Initiating Server......")
			sleep(2)
			check_utils()
			os.system("mount -t cifs -o username=taccuser,passwd=AH64_uh1 //hydingfs/cde_qa a/")
			print("Copying GpuTest_Linux_x64_0.7.0.zip from server to current location......")
			os.system("cp -f a/linux/OpenGL/GpuTest_Linux_x64_0.7.0.zip .")				
			os.system("unzip GpuTest_Linux_x64_0.7.0.zip")
						
		else:
			sys.exit(0)
	print("Initiating S3 with "+str(cycles)+" cycles along with Triangle_WindowMode. Please wait !!!")		
	sleep(2)
	os.system("chmod 777 /home/atitest/GpuTest_Linux_x64_0.7.0/start_triangle_windowed_1024x640.sh")
	os.chdir("/home/atitest/GpuTest_Linux_x64_0.7.0")	
	os.system("sh start_triangle_windowed_1024x640.sh &")
	sleep(5)
	S3()
	os.chdir("/home/atitest/")
	os.system("killall GpuTest")
	sleep(2)	
	sys.exit(0)

def unigine_heaven():

	if str(os.path.isdir('/home/atitest/Unigine_Heaven-4.0')) == 'False':
		if str(os.path.isfile('/home/atitest/Unigine_Heaven-4.0.run')) == 'False':
			print ("\n****Error****")
			print ('Please copy "Unigine_Heaven-4.0.run" from the server and extract to $home directory and run this script again.\n')
			sleep(2)
			yes = raw_input("If you want to copy and install automatically from server //hydingfs/ press (y/n) : ")
			if str(yes) == 'y' or str(yes)== 'Y':
				print("Copying UnigineHeaven-4.0 from server //hydinfs/ to current location......... ")
				sleep(2)
				check_utils()
				if not os.path.exists('a'):
					os.makedirs('a')
				os.system("mount -t cifs -o username=taccuser,passwd=AH64_uh1 //hydingfs/cde_qa a/")
				os.system("cp -f a/linux/OpenGL/unigine/Unigine_Heaven-4.0.run .")
				sleep(3)				
				os.system("./Unigine_Heaven-4.0.run")			
			
			else:
				sys.exit(0)			
	else:
		os.system("chmod 777 Unigine_Heaven-4.0.run")
		print ("Installing Unigine Heaven 4.0. Please wait !!!")			
		sleep(2)
			
				
			
			
	os.chdir("/home/atitest/Unigine_Heaven-4.0/")
	print("Please click on run to start Unigine Heaven!!")
	sleep(5)
	os.system("./heaven &")
	print ("Initiating S3 with "+str(cycles)+" cycles along with Unigine Heaven 4.0. Please wait !!!")	
	sleep(20)
	S3()
	os.chdir("/home/atitest")
	os.system("killall heaven_x64")
	sleep(2)
	os.system("killall browser_x64")
	sleep(5)
	sys.exit(0)	

def S3():

	count = 0
	global choice
	global dur,cycles
	TestName = {1:'glmark2',2:'glxgears',3:'Furmark_Window_1024x640',4:'Triangle_Window_1024x640',5:'Unigine Heaven 4.0'}	
	S3OpenGL_Logs = open("/home/atitest/S3OpenGL_Logs.txt",'a')
	S3OpenGL_Logs.write("!!--------------- Test S3 along with Open GL Application : "+str(TestName[choice])+" ---------------!!\n");
	S3OpenGL_Logs.close()	
	if cycles > 0:
		for i in range(cycles):

			#print('**sleep**')			
			status = commands.getstatusoutput("echo atitech | sudo -S rtcwake -m mem -s "+str(dur))
			cycles = cycles -1
			count = count + 1
			S3OpenGL_Logs = open("/home/atitest/S3OpenGL_Logs.txt",'a')
			S3OpenGL_Logs.write("\n"+str(ctime())+" S3 Passed in "+str(count)+" Cycle. "+"\n");
			S3OpenGL_Logs.close()	
	
	S3OpenGL_Logs = open("/home/atitest/S3OpenGL_Logs.txt",'a')
	S3OpenGL_Logs.write("\n========================================================================================\n");
	S3OpenGL_Logs.write("\nTest is sucessfully completed!!\n");
	S3OpenGL_Logs.write("Total Time taken by Test = "+str(round(decimal.Decimal(((time.time() - start_time)/60),2)))+" Mins"+"\n");
	S3OpenGL_Logs.close()
	print('Test is sucessfully completed!!')	
	print('\n*****Please check the logs for result******\n')

def menu():
	global choice
	print ("\n!!----Please chose 3D App along with S3----!!")
	print("1. GLMark2")
	print("2. Glxgears")
	print("3. Furmark_Window_1024x640")
	print("4. Triangle_Window_1024x640")
	print("5. Unigine Heaven 4.0 ")
	choice = int(raw_input("\nPlease choose you option : "))
	
def main():
	global dur,cycles
	
	if os.getuid() != 0:
		print("****ERROR****")
		print ("Please run this script is superuser mode.")
		sys.exit(0)
	
	cycles = int(raw_input("Please  enter the number of s3 cycles for test : " ))
	dur = int(raw_input("Please enter the Duration in Secs : "))
	menu()
	sleep(2)
	if choice == 1:
		glmark()
	elif choice == 2:
		glxgears()
	elif choice == 3:
		furmark()
	elif choice == 4:
		triangle()
	elif choice == 5:
		unigine_heaven()
	else:
		print("Please enter correct input !!")
		sleep(3)
		menu()



if __name__ == '__main__':
	main() 
