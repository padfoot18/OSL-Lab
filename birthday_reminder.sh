echo "Entire File Content"
awk '{print $1}' birthday.csv
echo ""
today=`date +%m/%d`
echo "Today's Date is "$today

echo ""
echo "Birthday Reminder"
name=`awk -F"," '$2 == "'$today'"{print $1}' birthday.csv`

for i in $name; do
	echo "Birthday reminder" "Today is "$i" birthday"
	notify-send "Birthday reminder" "Today is "$i" birthday"
done
