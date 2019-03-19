echo "Numbers are taken as command line arguments"

if [ $1 -ge $2 -a $1 -ge $3 ]
then
	echo $1 "is maximum"
	if [ $2 -gt $3 ]
	then 
		echo $3 "is minimum"
	else
		echo $2 "is minimum"
	fi
elif [ $2 -ge $1 -a $2 -ge $3 ]
then
	echo $2 "is maximum"
	if [ $1 -gt $3 ]
	then 
		echo $3 "is minimum"
	else
		echo $1 "is minimum"
	fi
elif [ $3 -ge $2 -a $3 -ge $1 ]
then
	echo $3 "is maximum"
	if [ $1 -gt $2 ]
	then 
		echo $2 "is minimum"
	else
		echo $1 "is minimum"
	fi
else
	echo "All numbers are same"
fi

