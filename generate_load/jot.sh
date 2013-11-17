#!/bin/sh 

rm -fr file_100MB

dd if=/dev/zero bs=1024 count=100000 of=file_100MB

for counter in $(jot 500)
do
        dd if=file_100MB of=/dev/null bs=64k
	#echo $counter
done
