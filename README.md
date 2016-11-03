# Halloween2016



![alt tag](https://raw.githubusercontent.com/topshed/Halloween2016/master/pumpkin3.jpeg) 

The idea was simple. Use two 8x8 Bi-colour LED matrices as eyes for the pumpkin that would be 'animated' to look spooky (blinking, looking from side to side etc). 

![alt tag](https://raw.githubusercontent.com/topshed/Halloween2016/master/lit2.jpeg) 

The add a PIR sensor to detected nearby movement and play a spooky sound through a speaker connected to the  Raspberry Pi. They eyes would also enter a 'hypno' mode and a string of cheap LED spiders from a pound shop would fade in and out. 

![alt tag](https://raw.githubusercontent.com/topshed/Halloween2016/master/lit1.jpeg) 

In order to use two of the LED matrices, you need to bridge (ideally with solder)  a jumper on one of them so that it has a different I2C address. The jumpers are on the back of the LED matrix backpack - I bridged the middle one, which gives an address of 0x72 (default is 0x70). If you use a differnt address, you'll need to change it in the code. 

Here is the circuit:

![alt tag](https://raw.githubusercontent.com/topshed/Halloween2016/master/halloween2016_bb.jpg) 

which can easily all fit inside a reasonably sized pumpkin.

![alt tag](https://raw.githubusercontent.com/topshed/Halloween2016/master/pumpkin2.jpeg) 