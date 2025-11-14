
**Binaural recording**

According to Wikipedia:

[**https://en.wikipedia.org/wiki/Binaural\_recording**](https://en.wikipedia.org/wiki/Binaural_recording)

**Binaural recording** is a method of [recording](https://en.wikipedia.org/wiki/Sound_recording_and_reproduction) [sound](https://en.wikipedia.org/wiki/Sound_recording) that uses two [microphones](https://en.wikipedia.org/wiki/Microphone), arranged with the intent to create a [3D](https://en.wikipedia.org/wiki/Three-dimensional_space) [stereo sound](https://en.wikipedia.org/wiki/Stereo_sound) sensation for the listener of actually being in the room with the performers or instruments. This effect is often created using a technique known as dummy head recording, wherein a [mannequin](https://en.wikipedia.org/wiki/Mannequin) head is fitted with a microphone in each ear. Binaural recording is intended for replay using headphones and will not translate properly over stereo speakers. This idea of a three-dimensional or "internal" form of sound has also translated into useful advancement of technology in many things such as stethoscopes creating "in-head" acoustics and IMAX movies being able to create a three-dimensional acoustic experience.

We will use the [Ensor-384 card](https://forums.raspberrypi.com/viewtopic.php?p=2347164&hilit=audio+adc+hat#p2266347) to make binaural recordings.

We'll build binaural microphones by modifying a pair of headphones.

We'll modify a pair of headphones we have lying around that we no longer use, or if we don't have any, we can buy some inexpensive headphones.

We'll remove the speakers and replace them with two INFINEON “IM73A135V01” analog differential microphones, the same ones we used on the [Ensor-384 card](https://forums.raspberrypi.com/viewtopic.php?p=2347164&hilit=audio+adc+hat#p2266347).

These are the two microphones:

![Fig. 1](binuaral_images/1.jpg)



And these are the headphones I bought on AliExpress.

[https://es.aliexpress.com/item/1005008562014087.html?spm=a2g0o.order\_list.order\_list\_main.29.6fa5194dLEUutc\&gatewayAdapt=glo2esp](https://es.aliexpress.com/item/1005008562014087.html?spm=a2g0o.order_list.order_list_main.29.6fa5194dLEUutc&gatewayAdapt=glo2esp)

We will remove the speakers from these headphones and place two INFINEON “IM73A135V01” analog differential microphones inside. We will also drill a 3mm diameter hole in the center of the outer part of each earcup, which will align with the microphone input hole located inside.

Each microphone will have a soldered 4-wire audio cable, and at the other end of the cable will be a 4-ring male audio connector.

[https://es.aliexpress.com/item/1005006762462706.html?spm=a2g0o.order\_list.order\_list\_main.22.6fa5194dLEUutc\&gatewayAdapt=glo2esp](https://es.aliexpress.com/item/1005006762462706.html?spm=a2g0o.order_list.order_list_main.22.6fa5194dLEUutc&gatewayAdapt=glo2esp)

This cable has a male connector on one end and a female connector on the other.

We will cut 1 meter of cable from the end with the male connector and also cut 15 cm of cable from the end with the female connector.

The two female connectors on each cable will be connected to microphone inputs 2 and 3 on the Ensor-384 card to facilitate the connection of the headphones.

**Detailed steps for modifying the headphones**

1\. Carefully disassemble the headphones.

First, cut the wires at the edge of the earbuds, remove the ear pads, and then remove the speaker covers. These covers simply have three pegs to attach to the base. They aren't glued, but you have to pull firmly to remove them. Remove the covers carefully, as the pegs can break. I broke two.

2\. Drill a 3mm diameter drill bit into the back of the headphones.

As shown in the following image.

3.- Glue the two Infineon microphones to the inside of the headphones, making sure that the microphone hole is aligned with the hole drilled in the headphone.

4\. Insert the stripped end of the audio cable through the hole on the bottom of the headphones.

Once the cable is inside, secure it with a cable tie and glue it to the inside of the headphones to prevent it from coming loose or moving.

Solder the four wires to the microphone:

Red wire – MBIAS (+2.75V)

Blue wire – MICP

Green wire – MICN

Copper wire – GND

5.- Fully assemble the headphones.

Next, we'll put on the headphones and connect them to the Ensor-384 sound card mounted on the Raspberry Pi, which is powered by a power bank.

We can make an initial recording at 384kHz/32bit and then test the binaural effect. We can make the recording, for example, while taking a walk around the city.

