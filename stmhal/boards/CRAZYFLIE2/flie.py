"""crazyflie utility functions"""

def fly():
    print("i cant do that dave")

MyMapperDict = { 'LeftMotorDir' : pyb.Pin.cpu.C12 }
pyb.Pin.dict(MyMapperDict)
g = pyb.Pin("LeftMotorDir", pyb.Pin.OUT_OD)
   

24AA64 =  0b01010000 # mem
MPU9250 = 0b01101001 # IMU
LPS25H =  0b01011101 # Presure sensor

adc = pyb.ADCAll(resolution)
val = adc.read_core_temp()      # read MCU temperature
val = adc.read_core_vbat()      # read MCU VBAT
val = adc.read_core_vref()      # read MCU VREF

class Flie:
    Blue_LED = pyb.Pin(pyb.Pin.board.LED_BLUE_L, pyb.Pin.OUT_PP)
    MOTOR1 = pyb.Pin.cpu.A1  # timer 2 ch2
    MOTOR2 = pyb.Pin.cpu.B11 # timer 2 ch4
    MOTOR3 = pyb.Pin.cpu.A15 # timer 2 ch1
    MOTOR4 = pyb.Pin.cpu.B9  # timer 4 ch4
#    m1 = pyb.Pin(MOTOR1, pyb.Pin.OUT_PP)
#    m2 = pyb.Pin(MOTOR2, pyb.Pin.OUT_PP)
#    m3 = pyb.Pin(MOTOR3, pyb.Pin.OUT_PP)
#    m4 = pyb.Pin(MOTOR4, pyb.Pin.OUT_PP)

    t2 = pyb.Timer(2)
    t2.init(freq=328000)
    t4 = pyb.Timer(4)
    t4.init(freq=328000)
    m1 = t2.channel(2, pyb.Timer.PWM, pin=MOTOR1, pulse_width_percent=0)
    m2 = t2.channel(4, pyb.Timer.PWM, pin=MOTOR2, pulse_width_percent=0)
    m3 = t2.channel(1, pyb.Timer.PWM, pin=MOTOR3, pulse_width_percent=0)
    m4 = t4.channel(4, pyb.Timer.PWM, pin=MOTOR4, pulse_width_percent=0)

    def set_fans(value):
        self.m1.pulse_width_percent(value)
        self.m2.pulse_width_percent(value)
        self.m3.pulse_width_percent(value)
        self.m4.pulse_width_percent(value)

class Expansion:
    IO1 = pyb.Pin.cpu.B8
    IO2 = pyb.Pin.cpu.B5
    IO3 = pyb.Pin.cpu.B4
    IO4 = pyb.Pin.cpu.C12

Pin(Pin.cpu.B4, mode=Pin.OUT_PP)

#define MIN_THRUST  10000
#define MAX_THRUST  60000
#altHoldMinThrust    = 00000; // minimum hover thrust - not used yet
#altHoldBaseThrust   = 43000; // approximate throttle needed when in perfect hover. More weight/older battery can use a higher value
#altHoldMaxThrust    = 60000; // max altitude hold thrust
