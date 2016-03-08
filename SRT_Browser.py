#!/usr/bin/python

from time import sleep
import os,sys,subprocess


def main():
	LogFiles = open("SRTBroswerLogs.txt",'w')
	LogFiles.write("!!*********** SRT Browser Tests ***********!! \n\n")
   	os.system("firefox https://www.youtube.com/watch?v=XISqvBVyASo &")
	sleep(10)
	subprocess.call(["xte", "key f"])
	LogFiles.write("1) Youtube Video Fullscreen - Passed \n\n")
	sleep(10)
	subprocess.call(["xte", "key f"])
	sleep(10)
	os.system("firefox https://www.google.co.in/maps/@17.4123487,78.408041010,11z &")
	sleep(10)                                                     
	subprocess.call(["xte", 'keydown Control_L' ,'key w' , 'keyup Control_L'])
	os.system("firefox https://www.google.co.in/maps/dir/AMD+India+Pvt+Ltd,+Bangalore,+Karnataka/AMD+R+and+D+Center+India+Pvt+Ltd,+APIIC+Software+Layout,+8th+-11th+Floor,+Madhapur,+11,+Inorbit+Mall+Rd,+Mindspace,+HITEC+City,+Hyderabad,+Andhra+Pradesh+500081/@15.209923,78.4648055,8z/data=!4m8!4m7!1m2!1m1!1s0x3bae11f5a938c31d:0x5cb3a142c34d3ce0!1m2!1m1!1s0x3bcb93e23889a8b1:0x6eb581e2947a72ae!3e0 &")
	sleep(10)
	LogFiles.write("2) Google Maps  - Passed \n\n")
	subprocess.call(["xte", 'key F11'])
	sleep(7)
	LogFiles.write("3) Google Maps Full Screen - Passed \n\n")
	subprocess.call(["xte", 'keydown Control_L', 'key Tab', 'keyup Control_L'])
	sleep(7)
	LogFiles.write("4) Switching Tabs in Browser - Passed \n\n")
	subprocess.call(["xte", 'keydown Control_L', 'key Tab', 'keyup Control_L'])
	sleep(10)
	subprocess.call(["xte",'mousemove 900 260'])
	sleep(10)
	subprocess.call(["xte",'mouseclick i'])
	sleep(2)
	subprocess.call(["xte",'mouseclick i'])
	sleep(10)
	subprocess.call(["xte", 'key F11'])
	os.system("firefox https://www.youtube.com/watch?v=DIqDzwd4Xfc&list=PL7RcAd6D0_T3DNrNBPM0WY6jnr-ra_gdn&index=8 &")
	sleep(10)
	subprocess.call(["xte", "key f"])
	sleep(30)
	LogFiles.write("5) 3D Youtube Video Fullscreen for 30 Seconds - Passed \n\n")
	subprocess.call(["xte", "key f"])
	sleep(10)
	i = 0
	for i in range(1,50):
		os.system("firefox https://twitter.com &")
		i = i + 1
		sleep(1)
	sleep(10)	
	LogFiles.write("6) 50 New Tabs for Twitter - Passed \n\n")
	i = 0
	for i in range(1,50):
		subprocess.call(["xte", 'keydown Control_L' ,'key w' , 'keyup Control_L'])
		sleep(1)
		i = i+1
	LogFiles.write("7) 50 Tabs Change Backward - Passed \n\n")
	sleep(10)
	subprocess.call(["xte", "key f"])	
	sleep(20)
	subprocess.call(["xte", "key f"])
	sleep(10)	
	os.system("killall firefox")
	print("Test Passed !!")
	print("Please check log file for more results.")
	LogFiles.write("===============================================================\n")
	LogFiles.write("\n Test Passed !!")

	LogFiles.close()
	



if __name__ == '__main__':
	main()



