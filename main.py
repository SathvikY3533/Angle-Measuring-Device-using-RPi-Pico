from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

WIDTH = 128
HEIGHT = 64

i2c = I2C(1, scl = Pin(15), sda = Pin(10), freq = 200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)
oled.show()

def main():
    ax=round(imu.accel.x,3)
    ay=round(imu.accel.y,3)
    az=round(imu.accel.z,3)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,1)
    #print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    oled.fill(0)
    oled.text("-- Angle Tool --", 0, 0)
    oled.text("X-axis: " + str(round((ax*90)-4)), 0, 16)
    oled.text("Y-axis: " + str(round(ay*90)), 0, 32)
    if (round((ax*90)-4) < 0):
        oled.text("^" , 110, 16)
    elif(round((ax*90)-4) > 0):
        oled.text("v" , 110, 16)
    else:
        oled.text("-" , 110, 16)
    
    if(round(ay*90) < 0):
        oled.text("<", 110, 32)
    elif(round(ay*90) > 0):    
        oled.text(">", 110, 32)
    else:
        oled.text("-", 110, 32)
    oled.text("---* Degree *---", 0, 50)
    oled.show()
    sleep(.5)

if __name__ == '__main__':
    try:
        while (KeyboardInterrupt):
            main()
    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()



