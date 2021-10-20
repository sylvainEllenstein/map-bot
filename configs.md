FILE WITH ALL INSTRUCTIONS FOR Env. INSTALLATION
Contains the links for install / docs about lib etc...

python-smbus :
https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/configuring-your-pi-for-i2c


importation : 
https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library


Vector images on python : 
https://pypi.org/project/drawSvg/


Writing in files in python :
https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/ + reading file : go to link at the end


Ajouter un bus I2C pour une centrale inertielle, écraser le SPI par exemple :
modifier fichier boot/config.txt
dtovertlay=i2c-gpio, bus=4,i2c_gpio_delay_us=1,i2c_gpio_sda=27,i2c_gpio_scl=22

https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all
