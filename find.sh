for i in $(cat readfile.txt); do
	find . -name "$i" -print -exec rm -rv {} +

done
