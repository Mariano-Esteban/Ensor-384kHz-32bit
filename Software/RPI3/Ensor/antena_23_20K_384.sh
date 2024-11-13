#!/bin/sh

echo "empieza el tiempo de espera"
date

sleep 5


echo "termina el tiempo de espera"
date

echo "empieza a grabar"

/home/ensor/Ensor/ti.py lin_23_20K_384_32.csv 1
arecord -D hw:0,0 -d 60 --max-file-time 60 -c 2 -r 384000 -f S32_LE -v -t wav --use-strftime /media/ensor/Ensor384/%Y/%m/%d/antena_20K_384_32bits-%H-%M-%v.wav


#sudo /home/ensor/Ensor/eea.py

#systemctl poweroff  


