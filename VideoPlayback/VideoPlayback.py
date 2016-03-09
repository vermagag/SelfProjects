#!/usr/bin/python
#Use this script as normal user mode.
#Developed by : gagan.verma@amd.com

from time import sleep,ctime,gmtime,strftime
from subprocess import Popen,PIPE
import sys,os

FilePath =''
Path = ''
PlayerName = '' 
Time = ''

# For getting help for the script
def help():
	print("\nHow to use VideoPlayback ?")
	print("$./VideoPlayback.py --player <Player Name> --path <File Path> --instance <No.> --time <Duration S/M/H> ")
	print("example : ./VideoPlayback --player vlc --instance 5 --time 8H --path /home/atitest/xyz.mp4 \n")
	print("List of Players :: \nvlc\nmplayer\nmpv\nkodi\n")	

# To check is no command line argument in command 
if len(sys.argv) == 1:
	print("Please read the instructions to use this script.")
	help()
	sys.exit()

# To check ATITOOL is present in system or not
def AtiToolCheck():
	AtiTool = os.path.isfile('/home/atitest/atitool')
	if str(AtiTool) == 'False':
		print("AtiTool is missing ......")
		print("Please copy and extract latest ATITOOL from //hydingfs/ to Home directory.")
		sys.exit()

# To get UVD CLock Status 
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

# To monitor UVD Clock 
def monitorUVD():
	Engaged = 'No'
	V,D = getUVDStatus()
	if V > 300 and D > 300:
		Engaged = True
	else:
		Engaged = False
	return str(Engaged)

# To check particular player is installed of not
def isPlayerInstalled(PlayerName):
	check = os.path.isfile('/usr/bin/'+str(PlayerName))
	return check


# To convert Hour and Minute Values to Seconds
def delayInSeconds(Delay):
	if 'H' in Delay or 'h' in Delay:
		return int(filter(str.isdigit,Delay))*3600
	if 'M' in Delay or 'm' in Delay:
		return int(filter(str.isdigit,Delay))*60
	if 'S' in Delay or 's' in Delay:
		return int(filter(str.isdigit,Delay))
	if '' in Delay:
		return int(Delay)

def main():

	global FilePath
	global PlayerName
	global Time
		
	AtiToolCheck()

	if '--help' in sys.argv[0]:
		help()
		sys.exit(0)
		
	PlayerName = sys.argv[sys.argv.index('--player') + 1]
	Instance = sys.argv[sys.argv.index('--instance') + 1]
	Duration = sys.argv[sys.argv.index('--time') + 1]
	Time = delayInSeconds(Duration)	

	VideoPlayback_Logs = open("/home/atitest/VideoPlayback_Logs.txt",'a')	
	VideoPlayback_Logs.write("************************ "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+" VideoPlayback ************************\n");
	VideoPlayback_Logs.write("Player = "+str(PlayerName)+"\n");
	VideoPlayback_Logs.write("No. of Instances = "+str(Instance)+"\n");
	VideoPlayback_Logs.write("Time Durations = "+str(Duration)+"\n");
	
	VideoPlayback_Logs.close()
	if str(isPlayerInstalled(PlayerName)) == 'False':
		print(str(PlayerName)+" Player is not installed in your system.")
		print("Please install "+str(PlayerName)+" player by using command for Ubuntu \"sudo apt-get install "+str(PlayerName)+"\" or for Fedora \"sudo yum install "+str(PlayerName)+"\".")
		sys.exit(1)

	if str(PlayerName) != 'vlc' and str(PlayerName) != 'mpv' and str(PlayerName) != 'kodi' and str(PlayerName) != 'mplayer':
			print("Please Enter valid player name like vlc, mplayer, kodi and mvp.\n")
			sys.exit(1)
	

	if '--path' in sys.argv:
		Path = sys.argv[sys.argv.index('--path') + 1]
		
		if os.path.isfile(Path):
			FilePath = Path
			
		else:
			count = 1
			for filename in os.listdir(Path):
				os.rename(os.path.join(Path, filename), os.path.join(Path, filename.replace(' ', '_')))

			VideoPlayback_Logs = open("/home/atitest/VideoPlayback_Logs.txt",'a')				
			VideoPlayback_Logs.write("\nFrom the selected directory path \" "+str(Path)+" \"\n\n");
			for FileName in os.listdir(Path):
				VideoPlayback_Logs.write(str(count)+". File Name = "+str(FileName)+"\n");
				os.chdir(Path)
				for i in range(int(Instance)):				
					if PlayerName == 'vlc':
						os.system("echo atitech | sudo -S vlc-wrapper --avcodec-hw=vdpau --repeat "+str(FileName)+" &")
						sleep(5)
						VideoPlayback_Logs.write("Video rendering - "+str(monitorUVD()+"\n"))

					else:
						os.system("echo atitech | sudo -S "+str(PlayerName)+" -loop 1000 "+str(FileName)+" &")
				sleep(Time)
				VideoPlayback_Logs.write(":--- Passed ---:\n\n");
				os.system("echo atitech | sudo -S killall "+str(PlayerName))
				count = count + 1	
			VideoPlayback_Logs.close()
			sys.exit(0)			
			
	
	else:	
		if os.path.isfile('David_Guetta_-_Titanium_ft._Sia.mp4'):
			FilePath = str(os.getcwd())+"/David_Guetta_-_Titanium_ft._Sia.mp4"
		else:
			print("Please restart the script and provide the path location of file or folder.")
			sys.exit()
		
	VideoPlayback_Logs = open("/home/atitest/VideoPlayback_Logs.txt",'a')				
	VideoPlayback_Logs.write("File Name and Path  = "+str(FilePath)+"\n");
	Players = {'vlc' : 'vlc-wrapper --avcodec-hw=vdpau --repeat ' ,'mplayer' : 'sudo mplayer -loop 1000 ','kodi' :'sudo kodi ','mpv' : 'sudo mpv -vo vdpau -hwdec=vdpau -loop 1000 '}
	
	for i in range(int(Instance)):
		os.system("echo atitech | sudo -S "+Players[PlayerName]+FilePath+" &")

	sleep(5)		
	VideoPlayback_Logs.write("Video rendering - "+str(monitorUVD())+"\n")
	sleep(Time)
	os.system("echo atitech | sudo -S killall "+str(PlayerName))
	VideoPlayback_Logs.write("\n:--- Passed ---:\n");
	VideoPlayback_Logs.close()
	



if __name__ == '__main__':
	main()
