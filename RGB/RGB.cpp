#include <iostream>
#include <wiringPi.h>
#include <wiringPiSPI.h>

int main()
{
	wiringPiSPISetup(0, 500000);
	while(true)
	{
		unsigned char data[200] = {0xf};	
		wiringPiSPIDataRW(0, data, 1);
	}
	return 0;
}

void setupPins()
{
}
