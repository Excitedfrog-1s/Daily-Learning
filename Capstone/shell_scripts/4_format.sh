#!/bin/bash

'''
Format pcap files to txt and upload to AWS S3 server.
'''

istart=0
iend=1
jstart=1
jend=5
set=training

for i in $(seq $istart $iend)
do
    for j in $(seq $jstart $jend)
    do
        istr=$(printf "%03d" "$i")
        jstr=$(printf "%04d" "$j")
        tshark -r $HOME/pcap/$istr-$jstr.pcap -Y ssl -F k12text -w $HOME/txt/$istr-$jstr.txt
        aws s3 cp $HOME/pcap/$istr-$jstr.pcap s3://usyd2019comp5703/$set/pcap/$istr/
        aws s3 cp $HOME/txt/$istr-$jstr.txt s3://usyd2019comp5703/$set/txt/$istr/
        rm -f $HOME/txt/$istr-$jstr.txt
    done
done
