#!/bin/bash
FILE="/home/atitest/flag.txt"

if [ -e $FILE ] 
then
    while read line
    do 
	if [ $line -gt 0 ] 
	then
	    echo $(($line - 1)) > flag.txt
	    echo  "Test is clear in Iteration $line" >> /home/atitest/log
            echo "******** Reboot in 5 secs *********" 
	    echo "\n"
            sleep 10
            echo atitech | sudo -S reboot
	else
	    echo "Test is completed!!"
	fi

    done < /home/atitest/flag.txt 

    else 
        echo "Please enter the cycle" 
        read cyc
        echo $(($cyc - 1)) > /home/atitest/flag.txt
        echo "Test is clear in Iteration $cyc" > /home/atitest/log
        echo "******** Reboot in 5 secs *********" 
        sleep 5
        echo atitech | sudo -S reboot
fi
