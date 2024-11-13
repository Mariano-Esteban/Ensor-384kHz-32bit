#!/bin/sh

echo "empieza el tiempo de espera"
date

sleep 10
#/home/rock/Ensor/tiempodeespera.py

echo "termina el tiempo de espera"
date

echo "empieza a grabar"

/home/ensor/Ensor/ti.py /home/ensor/Ensor/mic_14_2K5_384_32.csv 1
arecord -D hw:0,0 -d 10 --max-file-time 10 -c 2 -r 384000 -f S32_LE -v -t wav --use-strftime /media/ensor/Ensor384/%Y/%m/%d/prueba_384_32bits-%H-%M-%v.wav


#sudo /home/rock/Ensor/eea.py

#systemctl poweroff  


