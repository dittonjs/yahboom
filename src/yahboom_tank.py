#-*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Motor pin initialization operation


class YahboomTank:
  def __init__(self):
    self.left_motor_ratio = 0.0 # -1 to 1
    self.right_motor_ratio = 0.0

    #Definition of  motor pin
    self.IN1 = 20
    self.IN2 = 21
    self.IN3 = 19
    self.IN4 = 26
    self.ENA = 16
    self.ENB = 13

    # pin for the activation button
    self.key = 8

    self.ECHO_PIN = 0
    self.TRIG_PIN = 1

    self.sonor_initialized = False

    self.ServoPin = 23

    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)
    self._motor_init()

  def _motor_init(self):
    GPIO.setup(self.ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(self.IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(self.IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(self.ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(self.IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(self.IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(self.key,GPIO.IN)
    GPIO.setup(self.ServoPin, GPIO.OUT)
    #Set the PWM pin and frequency is 2000hz
    self.pwm_ENA = GPIO.PWM(self.ENA, 2000)
    self.pwm_ENB = GPIO.PWM(self.ENB, 2000)
    self.pwm_ENA.start(0)
    self.pwm_ENB.start(0)
    self.pwm_servo = GPIO.PWM(self.ServoPin, 50)
    self.pwm_servo.start(0)

  def servo_appointed_detection(self, pos):
    self.pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)

  def init_sonar(self):
    # signal is sent to the trigger pin to start sonar
    # then response is made through the echo pin
    GPIO.setup(self.TRIG_PIN,GPIO.OUT)
    GPIO.setup(self.ECHO_PIN,GPIO.IN)
    self.sonor_initialized = True

  def get_sonar_distance(self):
    if not self.sonor_initialized:
      self.init_sonar()

    GPIO.output(self.TRIG_PIN, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(self.TRIG_PIN, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(self.TRIG_PIN, GPIO.LOW)

    t3 = time.time()

    while not GPIO.input(self.ECHO_PIN):
        t4 = time.time()
        if (t4 - t3) > 0.03 :
            return -1


    t1 = time.time()
    while GPIO.input(self.ECHO_PIN):
        t5 = time.time()
        if(t5 - t1) > 0.03 :
            return -1

    t2 = time.time()
    time.sleep(0.01)
#    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    return ((t2 - t1)* 340 / 2) * 100


  def set_left_motor_ratio(self, ratio, commit = True):
    if ratio == self.left_motor_ratio: return
    if ratio < -1: self.left_motor_ratio = -1.0
    elif ratio > 1: self.left_motor_ratio = 1.0
    else: self.left_motor_ratio = ratio
    if commit:
      self._commit()

  def set_right_motor_ratio(self, ratio, commit = True):
    if ratio == self.right_motor_ratio: return
    if ratio < -1: self.right_motor_ratio = -1.0
    elif ratio > 1: self.right_motor_ratio = 1.0
    else: self.right_motor_ratio = ratio
    if commit:
      self._commit()

  def set_motor_ratios(self, l, r, commit=True):
    self.set_left_motor_ratio(l, False)
    self.set_right_motor_ratio(r, False)
    if commit:
      self._commit()

  def wait_for_activate_key(self):
    while GPIO.input(self.key):
      pass
    while not GPIO.input(self.key):
      time.sleep(0.01)
      if not GPIO.input(self.key):
        time.sleep(0.01)
        while not GPIO.input(self.key):
            pass

  def _commit(self):
    GPIO.output(self.IN1, GPIO.HIGH if self.left_motor_ratio > 0 else GPIO.LOW)
    GPIO.output(self.IN2, GPIO.HIGH if self.left_motor_ratio <= 0 else GPIO.LOW)
    GPIO.output(self.IN3, GPIO.HIGH if self.right_motor_ratio > 0 else GPIO.LOW)
    GPIO.output(self.IN4, GPIO.HIGH if self.right_motor_ratio <= 0 else GPIO.LOW)
    self.pwm_ENA.ChangeDutyCycle(abs(self.left_motor_ratio) * 100)
    self.pwm_ENB.ChangeDutyCycle(abs(self.right_motor_ratio) * 100)

  def destroy(self):
    self.pwm_ENA.stop()
    self.pwm_ENB.stop()
    GPIO.cleanup()



