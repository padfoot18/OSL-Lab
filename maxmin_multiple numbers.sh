max=$1
min=$1
for number in $*
do
	if [ $number -gt $max ]
	then
		max=$number
	fi

	if [ $number -lt $min ]
	then
		min=$number
	fi		
done
echo "Maximum nunber is" $max
echo "Minimum number is" $min
