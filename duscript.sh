for i in $(cat readfile.txt); do
	for j in $(find . -name $i); do
		echo $j
du -sch  $j
sleep 2
done
done
