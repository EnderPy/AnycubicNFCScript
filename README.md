# AnycubicNFCScript

Python script to automatically create a set of NFC commands to colour filament and brand for ACE Pro 

Requires python (and matplotlib) installed

## To use:

1. run python file `python ./main.py`
2. input colour name or enter to skip to enter hex code
3. it will ask for hex code if you didnt enter a colour, or didnt find the colour (Black #000000 default)
4. input filament type (PLA+ default)
5. will print out NFC commands
 
[2025-01-26 10-58-44.webm](https://github.com/user-attachments/assets/3aeab5d0-44d0-4d1e-abec-82b22cc423ee)

### Parameters:

You can use the following parameters for quickly generate the NFC commands.

`--copy`: Copy output to clipboard

`--no-print`: Do not show output on screen

`--hex`: Color hex (e.g. #123456, $12345678)

`--color`: Color name

`--material`: Material (e.g. PLA)

 
## To write:

1. open relevant NFC writing tool (I used NFC tools pro)
2. go to other -> advanced NFC commands


<img src="Tutorial/Screenshot_20250126_110040_NFC%20Tools.jpg" width="200px"/>

3. Paste into box
<img src="Tutorial/Screenshot_20250126_110055_NFC Tools.jpg" width="200px"/>

4. place NFC tag under phone and confirm it detects it

<img src="Tutorial/20250126_110130.jpg" height="300px"/>

<img src="Tutorial/20250126_110137.jpg" height="300px"/>

5. send command

 <img src="Tutorial/Screenshot_20250126_110143_NFC Tools.jpg" width="200px"/>

 * note: it may not show this option if there is too much text, if so you can cut half of the commands out AFTER a comma (,) and paste it as a seperate command

<img src="Tutorial/Screenshot_20250126_110105_NFC Tools.jpg" width="200px"/>
<img src="Tutorial/Screenshot_20250126_110118_NFC Tools.jpg" width="200px"/>

after:

<img src="Tutorial/Screenshot_20250126_110156_NFC Tools.jpg" width="200px"/>
<img src="Tutorial/Screenshot_20250126_110206_NFC Tools.jpg" width="200px"/>

7. attach to filament roll and confirm it works!


### NOTICE: I have tested this by myself using NTAG215 tags and have success, i am not responsible for any damages this causes to you or your equipment.
