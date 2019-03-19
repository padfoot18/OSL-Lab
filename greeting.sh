hour=`date +%H`

if [ $hour -ge 0 -a $hour -lt 12 ]
then 
	echo "Good morning"
	notify-send "Greeting" "Good morning"
elif [ $hour -ge 12 -a $hour -lt 16 ]
then
	echo "Good afternoon"
	notify-send "Greeting" "Good afternoon"
else
	echo "Good evening"
	notify-send "Greeting" "Good evening"
fi
