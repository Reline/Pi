# RGB LED Strip
The library used to manipulate the GPIO ports was [wiringPi](http://wiringpi.com).
Original code made during this project can be found in:  main.c ws2811.h ws2811.c

## Compiling
Run the build file located in the directory
<pre><code>./build</code></pre>

or use a C compiler to link these files - here I use gcc
<pre><code>gcc main.c ws2811.c pwm.c dma.c board_info.c mailbox.c -lwiringPi -o desiredFileName && sudo ./desiredFileName</code></pre>
