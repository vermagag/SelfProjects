#!/usr/bin/python
#Script should run only in normal user mode.
#Developed by : gagan.verma@amd.com 

from time import sleep,ctime
from subprocess import Popen,PIPE
import sys,os,dircache,random,commands,time,decimal

start_time = time.time()
FILES = '/home/atitest/Files/' 

cycles = 0
dur = 0
before1,before2,after1,after2 =0,0,0,0
Player_Name = ' '
Filename = ' '
path = ' '
S3Playback_Logs = ' '

def getUVDStatus():
	VCLK=0.0
	DCLK=0.0
	initUVD = Popen('echo atitech | sudo -S ./atitool -clkstatus',stdout=PIPE,shell=True).communicate()[0]
	for line in initUVD.split('\n'):
		if 'VCLK' in line:
			VCLK = (line.split(':')[1].split('MHz')[0].strip())
		if 'DCLK' in line:
			DCLK = (line.split(':')[1].split('MHz')[0].strip())
	return (float(VCLK),float(DCLK))

def monitorUVDStatusFor(Delay):
	VCLK_Sum = 0
	DCLK_Sum = 0
	count = 0
	initTime = time.time()
	while time.time()-initTime < Delay:
		a,b = getUVDStatus()
		VCLK_Sum = VCLK_Sum + float(a)
		DCLK_Sum = DCLK_Sum + float(b)
		count = count + 1
	return float(VCLK_Sum/count),float(DCLK_Sum/count)

def rendercheck():
	global before1,before2,after1,after2 
	after1,after2 = monitorUVDStatusFor(10)
	print after1,after2,before1,before2	
	if after1 > before1 and after2 >= before2:
		return str("Passed! Gpu is rendering")
	else :
		return str("Failed! Gpu is not rendering")

def check():	
	vlc_check = os.path.isfile('/usr/bin/vlc')
	mpv_check= os.path.isfile('/usr/bin/mpv')
	mplayer_check = os.path.isfile('/usr/bin/mplayer')
	MediaFiles = os.path.isdir('/home/atitest/Files')
	AtiTool = os.path.isfile('/home/atitest/atitool')

	if str(vlc_check) == 'False':	
		print('Please install VLC by command for Ubuntu "sudo apt-get install vlc" for Fedora "sudo yum install vlc "')
		sys.exit()		
	if str(mpv_check) == 'False':
		print('Please install MPV by command for Ubuntu "sudo apt-get install mpv" for Fedora "sudo yum install mpv "')
		sys.exit()
	if str(mplayer_check) == 'False':
		print('Please install MPlayer by command for Ubuntu  "sudo apt-get install mplayer" for Fedora "sudo yum install mplayer"')
		sys.exit()
	if str(MediaFiles) == 'False' :
		os.system("mkdir /home/atitest/Files")
		print("Please add all the video files in 'Files' folder in Home directory.")	
		sys.exit()
	else:	
		filenames = os.listdir(FILES)
		for filename in filenames:
			os.rename(os.path.join(FILES, filename), os.path.join(FILES, filename.replace(' ', '_')))

	if str(AtiTool) == 'False':
		print("Please copy and extract latest ATI TOOL from //hydingfs/ to Home directory.")
		sys.exit()

def help():
	print("How too use S3_Playeback ?")
	print("$./S3Playback.py <cycles> <duration>")

def S3(dur):
	print "**sleep**"	
	status = commands.getstatusoutput("echo atitech | sudo -S rtcwake -m mem -s "+str(dur))
	

def main():
	count = 1
	global before1,before2,after1,after2
	global Player_Name
	global Filename,path,S3Playback_Logs
	print("\n!!! ************ I hope you have done below steps before initializing this script ************ !!! \n")
	print("1) Installed all media players e.g MVP, Mplayer, VLC etc.")
	print("2) Copied all the media file in \"/home/<user>/Files/\" directory." )
	print("3) Copied and exract ATI Tool to home directory.\n")
	print("Wait checking system .... ")
	sleep(5)	
	check()
	if '--help' in sys.argv:
	    help()
	    sys.exit(0)

	if len(sys.argv) > 2:
		cycles = int(sys.argv[1])
		dur = int(sys.argv[2])
	else:
		cycles = int(raw_input("Please  enter the number of s3 cycles for test : " ))
		dur = int(raw_input("Please enter the Duration in Secs : "))

	if cycles > 0:
		for i in range(cycles):
			S3Playback_Logs = open("/home/atitest/S3Playback_Logs.txt",'a')
			S3Playback_Logs.write("\n"+str(ctime())+" S3 Passed in "+str(count)+" Cycle. "+"\n");
			Players = {'mpv':'mpv -vo vdpau -hwdec=vdpau ','mplayer':'mplayer ','vlc':'vlc '}
			Player_Name = str(random.choice(Players.keys()))
			Filename = random.choice(dircache.listdir(FILES))
			Path = os.path.join(FILES,Filename)
			before1,before2 = getUVDStatus()
			os.system(Players[Player_Name]+Path+" &")
			RenderResult = rendercheck()

			S3Playback_Logs = open("/home/atitest/S3Playback_Logs.txt",'a')
			S3Playback_Logs.write(str(ctime())+" Player Name : "+str(Player_Name)+", File Name : "+str(Filename)+"\n"+"GPU Rendering Status : "+str(RenderResult)+"\nAverage Score: VCLK = "+str(after1)+" DCLK = "+str(after2)+"\n");
			S3Playback_Logs.write("_________________________________________________________________________________________________\n")			
			S3Playback_Logs.close()
			sleep(20)			
			S3(dur)
			sleep(10)
			os.system("killall "+Player_Name)			
			cycles = cycles -1
			count = count + 1
	
	S3Playback_Logs = open("/home/atitest/S3Playback_Logs.txt",'a')
	S3Playback_Logs.write("=================================================================================================\n");
	S3Playback_Logs.write("\nTest is sucessfully completed!!\n");
	S3Playback_Logs.write("Total Time taken by Test = "+str(round(decimal.Decimal(((time.time() - start_time)/60),2)))+" Mins"+"\n");
	S3Playback_Logs.close()
	
	
		
if __name__ == '__main__':
	main()
			
