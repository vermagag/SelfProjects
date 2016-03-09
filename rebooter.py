#!/usr/bin/python
#Copy this sript to "/etc/init.d/" and creat one symbolic link to "/etc/rc0.d/" with name "S99rebooter.py"
# Developed by "gagan.verma@amd.com"

from time import sleep,ctime
import sys,os

def main():
   if '--help' in sys.argv:
       print("copy this sript to /etc/init.d/ and creat one symbolic link to /etc/rc0.d/ with name \"S99rebooter.py\"\nCommand : \"ln -s /etc/init.d/rebooter.py /etc/rc0.d/S99rebooter.py\"\n")
       sys.exit()
   RebooterLog = open("/home/atitest/Rebooter_Log.txt",'a')
   
   if os.path.isfile("/home/atitest/Rebooter_Count.txt") == False:
      if len(sys.argv)>1:
          NumberOfReboots = int(sys.argv[1])
      else:
         NumberOfReboots = int(raw_input("Please Enter the number of Reboots: "))
      RebooterLog.write(str(ctime())+" Test Name : REBOOTER "+str(NumberOfReboots)+'\n')
      CountFD = open("/home/atitest/Rebooter_Count.txt",'w')
      CountFD.write(str(NumberOfReboots))
      CountFD.close()
   else:
      NumberOfReboots = int(open("/home/atitest/Rebooter_Count.txt").read())
      print(str(NumberOfReboots)+" cycles more to reboot")
      RebooterLog.write(str(NumberOfReboots)+" cycles more to reboot\n")
      NumberOfReboots = NumberOfReboots -1
      CountFD = open("/home/atitest/Rebooter_Count.txt",'w')
      CountFD.write(str(NumberOfReboots))
      CountFD.close()
   if NumberOfReboots >0:
      RebooterLog.close()
 #     sleep(5)
  #    print("Reboot!!")
      sleep(60)
      os.system("echo atitech | sudo -S reboot")
   else:
      RebooterLog.write(str(ctime())+" Test Finished Successfully\n")
      RebooterLog.close()
      print("Rebooter Test Finished Successfully!\n")
      sys.exit(0)

if __name__ == "__main__":
   main()
