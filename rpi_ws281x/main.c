#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <signal.h>


#include "board_info.h"
#include "clk.h"
#include "gpio.h"
#include "pwm.h"

#include "ws2811.h"

 // using the wiringPi library to control pins
#include <wiringPi.h>

#define ARRAY_SIZE(stuff)                        (sizeof(stuff) / sizeof(stuff[0]))

#define TARGET_FREQ                              WS2811_TARGET_FREQ
#define GPIO_PIN                                 18
#define DMA                                      5

#define WIDTH                                    10
#define HEIGHT                                   1
#define LED_COUNT                                (WIDTH * HEIGHT)

// define our pins that we will be using
#define TRACE_SPEED_PIN				 16
#define COLOR_SPEED_PIN				 21
#define MODE_PIN				 12

ws2811_t ledstring =
{
    .freq = TARGET_FREQ,
    .dmanum = DMA,
    .channel =
    {
        [0] =
        {
            .gpionum = GPIO_PIN,
            .count = LED_COUNT,
            .invert = 0,
            .brightness = 255,
	    // we want to manipulate each individual LED's brightness (see ws2811.h & ws2811.c)
	    .brights[0] = 255,
	    .brights[1] = 255,
	    .brights[2] = 255,
	    .brights[3] = 255,
	    .brights[4] = 255,
	    .brights[5] = 255,
	    .brights[6] = 255,
	    .brights[7] = 255,
	    .brights[8] = 255,
	    .brights[9] = 255,
        },
        [1] =
        {
            .gpionum = 0,
            .count = 0,
            .invert = 0,
            .brightness = 0,
        },
    },
};

ws2811_led_t matrix[WIDTH][HEIGHT];

int dotspos[] = { 0, 1, 2, 3, 4, 5, 6 };
ws2811_led_t dotcolors[] =
{
    0x200000,  // red
    0x201000,  // orange 	
    0x202000,  // yellow
    0x002000,  // green  
    0x000020,  // blue
    0x100020,  // indigo
    0x100010,  // purple
};


static void ctrl_c_handler(int signum)
{
    ws2811_fini(&ledstring);
}

static void setup_handlers(void)
{
    struct sigaction sa =
    {
        .sa_handler = ctrl_c_handler,
    };

    sigaction(SIGKILL, &sa, NULL);
}

int mode1()
{
	usleep(1000000);
	
	int i = 0;
	int color = 0;
	for (i = 0; i < WIDTH; i++)
	{
       		ledstring.channel[0].leds[i] = dotcolors[color++];
		if (color >= ARRAY_SIZE(dotcolors)) color = 0;
	}
	for (i = 0; i < WIDTH; i++)
	{
		ledstring.channel[0].brights[i] = 255;
       		if (ws2811_render(&ledstring)) return -1;
	}
       	if (ws2811_render(&ledstring)) return -1;
	while(1) { if(digitalRead(MODE_PIN) == 1) return 2;}
}

int mode2()
{
	usleep(1000000);
	int trackspeed = 1;
	int i = 0;
	int spacesMoved = 0;
	for (spacesMoved = 0; spacesMoved < ARRAY_SIZE(dotcolors); spacesMoved++)
	{
		int color = 0;
		for (i = 0; i < WIDTH; i++)
		{
			if(digitalRead(MODE_PIN) == 1) return 3;
    			if(digitalRead(TRACE_SPEED_PIN))
    			{
				trackspeed*=10;
				if (trackspeed > 100) trackspeed = 1;
				//printf("%d", trackspeed);
				usleep(1000000);
    			}

			int newColor = spacesMoved + color++;
			if(newColor >= ARRAY_SIZE(dotcolors)) newColor -= 7;
        		ledstring.channel[0].leds[i] = dotcolors[newColor];
			if (color >= ARRAY_SIZE(dotcolors)) color = 0;
		}
		if (spacesMoved >= 6) spacesMoved = 0;
        	if (ws2811_render(&ledstring)) return -1;
        	usleep(50000 * trackspeed);
	}	
}

int mode3()
{
	usleep(1000000);
	int trackspeed = 1;
	int i = 0;
	int color = 0;
	for (i = 0; i < WIDTH; i++)
	{
       		ledstring.channel[0].leds[i] = dotcolors[color];
		if (color >= ARRAY_SIZE(dotcolors)) color = 3;
		ledstring.channel[0].brights[i] = 0;
        	if (ws2811_render(&ledstring)) return -1;
	}

	int current = 0;
	int prev = 0;
	int pp = 0;
	int off = 0;
	for (current = 0; current < WIDTH; current++)
	{	
		for (i = 0; i < WIDTH; i++)
		{
			if(digitalRead(MODE_PIN) == 1) return 4;
    			if(digitalRead(TRACE_SPEED_PIN))
    			{
				trackspeed*=10;
				if (trackspeed > 100) trackspeed = 1;
				//printf("%d", trackspeed);
				usleep(1000000);
    			}

       			ledstring.channel[0].leds[i] = dotcolors[color];
			if (color >= ARRAY_SIZE(dotcolors)) color = 3;
			ledstring.channel[0].brights[i] = 0;
        		if (ws2811_render(&ledstring)) return -1;
		}
    	
		ledstring.channel[0].brights[off] = 0;
		ledstring.channel[0].brights[pp] = 50;
		ledstring.channel[0].brights[prev] = 150;
		ledstring.channel[0].brights[current] = 255;
		
		off = pp;
		pp = prev;
		prev = current;
		
		if (current >= 9) current = -1;

        	if (ws2811_render(&ledstring)) return -1;
        	usleep(50000 * trackspeed);
	}
}

int mode4()
{
	int trackspeed = 1;
	int colorspeed = 1;
	int current = 0;
	int prev = 0;
	int pp = 0;
	int off = 0;
	int color = 0;
	usleep(1000000);
	while(1)
	{
		int spacesMoved = 0;
		for (spacesMoved = 0; spacesMoved < ARRAY_SIZE(dotcolors); spacesMoved++)
		{
			int i = 0;
			for (i = 0; i < WIDTH; i++)
			{
				int newColor = spacesMoved + color++;
				if(newColor >= ARRAY_SIZE(dotcolors)) newColor -= 7;
        			ledstring.channel[0].leds[i] = dotcolors[newColor];
				if (color >= ARRAY_SIZE(dotcolors)) color = 0;
				if(ws2811_render(&ledstring)) return -1;
			}
        		usleep(50000 * colorspeed);
			for (current = 0; current < WIDTH; current++)
			{	
				int i = 0;
				for (i = 0; i < WIDTH; i++)
				{
					if(digitalRead(MODE_PIN) == 1) return 1;
    					if(digitalRead(TRACE_SPEED_PIN))
    					{
						trackspeed*=10;
						if (trackspeed > 100) trackspeed = 1;
						//printf("%d", trackspeed);
						usleep(1000000);
    					}
	
       					ledstring.channel[0].leds[i] = dotcolors[color];
					ledstring.channel[0].brights[i] = 0;
       		 			if (ws2811_render(&ledstring)) return -1;
				}
    	
				ledstring.channel[0].brights[off] = 0;
				ledstring.channel[0].brights[pp] = 50;
				ledstring.channel[0].brights[prev] = 150;
				ledstring.channel[0].brights[current] = 255;
			
				off = pp;
				pp = prev;
				prev = current;

        			if (ws2811_render(&ledstring)) return -1;
        			usleep(50000 * trackspeed);
			}
			if (current >= 9) current = -1;
		}
		if (spacesMoved >= 7) spacesMoved = 0;
        	if (ws2811_render(&ledstring)) return -1;
	}	
}

int main(int argc, char *argv[])
{
    if (board_info_init() < 0) return -1;
    setup_handlers();
    if (ws2811_init(&ledstring)) return -1;
    
    int mode = 1; // 1, 2, 3, 4

    wiringPiSetupGpio();

    pinMode(TRACE_SPEED_PIN, INPUT);
    pullUpDnControl(TRACE_SPEED_PIN, PUD_UP);

    pinMode(MODE_PIN, INPUT);
    pullUpDnControl(MODE_PIN, PUD_UP);

    pinMode(COLOR_SPEED_PIN, PUD_UP);
    pullUpDnControl(COLOR_SPEED_PIN, PUD_UP);

    setvbuf(stdout, NULL, _IONBF, 0); // clearing up buffer problems with printf

    while (1)
    {
	switch(mode)
	{
		case 1:
			mode = mode1(); break;
		case 2:
			mode = mode2(); break;
		case 3:
			mode = mode3(); break;
		case 4:
			mode = mode4(); break;
	}	
    }
    //ws2811_fini(&ledstring);
    return 0;
}
