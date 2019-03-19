#!/bin/bash
# Shell script to find max min of n numbers

read -p "Enter n: " n
echo "enter $n numbers"

i=0
while [ $i -lt $n ]; do
	read arr[$i]
	i=`expr $i + 1`
done

i=1
max=${arr[0]}
min=${arr[0]}
while [ $i -lt $n ]; do
	if [ ${arr[$i]} -gt $max ]; then
		max=${arr[$i]}
	fi
	if [ ${arr[$i]} -lt $min ]; then
		min=${arr[$i]}
	fi
	i=`expr $i + 1`
done

echo "Max=$max, Min=$min"
