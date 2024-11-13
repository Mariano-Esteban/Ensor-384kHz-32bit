#!/bin/sh

# Para probar, es necesario modificar spdif-receiver a 768000 y compilar kernel

echo "empieza el tiempo de espera"
date

sleep 5


echo "termina el tiempo de espera"
date

echo "empieza a grabar"

/home/ensor/Ensor/ti.py lin_2_20K_768_32_1c.csv 1
arecord -D plughw:0,0 -d 10 --max-file-time 10 -c 1 -r 768000 -f S32_LE -v -t wav --use-strftime /media/ensor/Ensor384/%Y/%m/%d/antena_20K_768_32bits_1c-%H-%M-%v.wav


#sudo /home/ensor/Ensor/eea.py

#systemctl poweroff  


