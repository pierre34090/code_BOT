#!/bin/bash
#tcpdump src port 5555 -i wlp7s0 | tcpflow -c | tee packets.log &
sleep 2
while :
do
	for i in `seq 0 3`
	do
		echo "$i"
		java -jar sikulixide-2.0.4.jar -r scriptSikuli.py --arg $i
		sleep 2

	    python main.py 
	    cd datasDofus/
	    git add *
	    git commit -m "Regular Upade From MaisonMere"
	    git push
	    chown pierre *
	    cd ..
	   	echo "" > packets.log
	done
done