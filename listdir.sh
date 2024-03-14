echo "enter your folder: "
read folder
for i in $(ls $folder); do
#	for j in $(ls -d */); do
	echo $i
	#echo $i
done
#done
