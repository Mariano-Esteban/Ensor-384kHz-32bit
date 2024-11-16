# Ensor-384kHz-32bit

Audio ADC HAT for the Raspberry Pi.

The Ensor-384 is a high-resolution analog-to-digital converter for the Raspberry Pi, support sample rates up to 384kHz/32bit

## Features:

•	Dedicated 768kHz/32bit high-quality Burr-Brown ADC. Texas Instruments TLV320ADC6140

•	Stereo input. Two differential Microphones onboard. Infineon IM73A135V01

•	Two optional auxiliary input to balanced and not balanced microphones, or line in.

•	Connects directly to the Raspberry Pi, no additional cables needed.

•	Compatible with all Raspberry Pi models with a 40-pin GPIO connector.

•	Directly powered from the Raspberry Pi, no additional power supply.


## Specifications:


     ADC input voltage Differential,  	2-VRMS full-scale inputs	

     ADC input voltage Single-ended, 	1-VRMS full-scale inputs	

     ADC signal-to-noise ratio	122db	

     ADC THD+N	-98db	

     Frequency response	20Hz-80kHz	

     Input gain	0db to 42dB	

     Sample rates	48kHz - 384kHz / 32bit.	


## Developed application:

Stereo audio recorder up to 384kHz - 32 bits

With a bandwidth of 20Hz to 80kHz, it can be used in the following fields:


      General purpose high fidelity audio recorder.

      Bioacoustics

      Passive acoustic monitoring of wildlife

      Monitoring of biodiversity and the environment

      Animal behavior analysis


The Ensor-384 card together with the Raspberry Pi card form an automatic audio recording system of very high quality.
Records 2 audio channels of up to 384000 samples per second and 32 bits per sample
Audio recording is done on a USB flash drive connected to the Raspberry Pi

The Ensor-384 card is compatible with any Raspberry Pi. 3, 4, or 5

Ensor-384 is a professional audio digitizer card capable of digitizing two audio channels with a signal sampling rate of up to 384,000 samples per second and a resolution of 32 bits per sample. The digitized signal is sent to the Raspberry Pi via I2S for recording on a USB flash drive

The Ensor-384 card has two differential microphones MEMS soldered on it for digitizing the two audio channels. It also has the possibility of connecting two other external differential microphones, single ended microphones or line in


The Ensor-384 card connects to the Raspberry Pi via the 40-pin GPIO expansion connector

The analog-to-digital converter (ADC) used on the card is the Texas Instruments chip
[TLV320ADC6140](https://www.ti.com/product/TLV320ADC6140), Quad-channel 768-kHz Burr-Brown audio analog-to-digital converter (ADC) with 122-dB SNR

[TLV320ADC6140](https://www.ti.com/product/TLV320ADC6140) chip description according to the manufacturer's datasheet:


“The [TLV320ADC6140](https://www.ti.com/product/TLV320ADC6140) is a Burr-Brown™ high performance, audio analog-to-digital converter (ADC) that supports simultaneous sampling of up to four analog channels or eight digital channels for the pulse density modulation (PDM) microphone input. The device supports line and microphone inputs, and allows for both single-ended and differential input configurations. The device integrates programable channel gain, digital volume control, a programmable microphone bias voltage, a phase-locked loop (PLL), a programmable high-pass filter (HPF), biquad filters, low-latency filter modes, and allows for sample rates up to 768 kHz. The device supports time-division multiplexing (TDM), I 2S, or left-justified (LJ) audio formats, and can be controlled with either the I2C or SPI interface. These integrated high-performance features, along with the ability to be powered from a single-supply of 3.3 V or 1.8 V, make the device an excellent choice for space-constrained audio systems in far-field microphone recording applications. The TLV320ADC6140 is specified from –40°C to +125°C, and is offered in a 24-pin WQFN package”


The Ensor-384 board design is based on the Texas Instruments evaluation board
for the TLV320ADC6140 chip. Its study is recommended:

[ADC6140EVM-PDK](https://www.ti.com/tool/ADC6140EVM-PDK)

[User’s Guide](https://www.ti.com/lit/ug/sbau335/sbau335.pdf?ts=1729872619393&ref_url=https%253A%252F%252Fwww.ti.com%252Ftool%252FADC6140EVM-PDK)


The two microphones soldered onto the Ensor-384 board are from Infineon, reference:
[IM73A135V01](https://www.infineon.com/dgdl/Infineon-IM73A135-DataSheet-v01_00-EN.pdf?fileId=8ac78c8c7f2a768a017fadec36b84500). IP57 dust and water resistant analog XENSIVTM MEMS microphone.

These microphones have a bandwidth ranging from 20Hz to 80KHz, which allows them to digitize ultrasounds, for example, those produced by bats.


Description of the [IM73A135V01](https://www.infineon.com/dgdl/Infineon-IM73A135-DataSheet-v01_00-EN.pdf?fileId=8ac78c8c7f2a768a017fadec36b84500) microphone. According to the manufacturer's data sheet:


“The [IM73A135V01](https://www.infineon.com/dgdl/Infineon-IM73A135-DataSheet-v01_00-EN.pdf?fileId=8ac78c8c7f2a768a017fadec36b84500) is designed for applications which require a microphone with high SNR (low self-noise), low distortion (high AOP), which is also IP57 robust to dust and water. Best-in-class Signal to Noise Ratio (SNR) of 73dB(A) enables far field and low volume audio pick-up. The flat frequency response (20Hz low-frequency roll-off) and tight manufacturing tolerance improve the performance of multi-microphone array applications. The high-performance analog microphone ASIC contains an extremely low noise preamplifier and a high-performance differential output amplifier. Different power modes can be selected in order to suit specific current consumption requirements. Each IM73A135V01 microphone is calibrated with an advanced Infineon calibration algorithm, resulting in small sensitivity tolerances (± 1dB).”

To achieve good stability in the digitalization of the audio signal, a high-quality oscillator of 24.756 MHZ and 2.5ppm with an operating temperature range of -30ºC to +75ºC from the Abracon firm has been used, reference:

[ASTX-H11-24.576MHZ-T](https://abracon.com/Oscillators/ASTX-H11.pdf)

The voltage regulator circuit used to power the analog-to-digital conversion stage of the TLV320ADC6140 is the one recommended by Texas Instruments due to its excellent features, reference:

[TPS73533QDRBRQ1](https://www.ti.com/product/TPS735-Q1). Automotive 500-mA, low-noise, low-IQ, low-dropout voltage regulator with enable

[TPS73533QDRBRQ1](https://www.ti.com/product/TPS735-Q1) chip description. According to the manufacturer's datasheet:

“The TPS735-Q1 family of low-dropout (LDO), low power linear regulators offers excellent ac performance with very low ground current. High power-supply rejection ratio (PSRR), low noise, fast start-up, and excellent line and load transient responses are provided while consuming a very low 46 µA (typical) ground current. The TPS735-Q1 family of devices is stable with ceramic capacitors and uses an advanced BiCMOS fabrication process to yield a typical dropout voltage of 280 mV at 500-mA output. The TPS735-Q1 family of devices uses a precision voltage reference and feedback loop to achieve overall accuracy of 2% (VOUT > 2.2 V) over all load, line, process, and temperature variations. This family of devices is fully specified from TA = –40°C to 125°C and is offered in a low-profile, 3-mm × 3-mm VSON package.”


Ensor-384 SCH

![Ensor-384-32bit_sch](https://github.com/user-attachments/assets/295f3e69-c7c7-405f-b348-3a96253d8a15)

Ensor-384 PCB
 
![Ensor384-32](https://github.com/user-attachments/assets/d96bebc5-13aa-4e0e-9e86-e9cfa4a97657)
![Ensor-384-32bit_pcb](https://github.com/user-attachments/assets/18768a3a-f827-424d-b6ae-bcc8b3611110)
 
Ensor-384 connected to the Raspberry Pi 3 B+
Where you can see the two auxiliary inputs
 for two other differential microphones
They also support unbalanced microphone or line input.


![Ensor384 - RPi3B+](https://github.com/user-attachments/assets/10ea50f8-09e6-45e2-ab53-ffa75a98457f)

 

