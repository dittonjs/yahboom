#-*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time
import math



#Motor pin initialization operation


class YahboomTank:
  def __init__(self):
    self.left_motor_ratio = 0.0 # -1 to 1
    self.right_motor_ratio = 0.0
    self.mode = mode
    #Definition of  motor pin
    self.IN1 = 20
    self.IN2 = 21
    self.IN3 = 19
    self.IN4 = 26
    self.ENA = 16
    self.ENB = 13

    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)

    #Ignore warning information
    GPIO.setwarnings(False)
    self._motor_init()

  def _motor_init():
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    self.pwm_ENA = GPIO.PWM(ENA, 2000)
    self.pwm_ENB = GPIO.PWM(ENB, 2000)
    self.pwm_ENA.start(0)
    self.pwm_ENB.start(0)

  def set_left_motor_ratio(self, ratio, commit = True):
    if ratio == self.left_motor_ratio: return
    if ratio < -1: self.left_motor_ratio = -1.0
    elif ratio > 1: self.left_motor_ratio = 1.0
    else self.left_motor_ratio = ratio
    if commit:
      self._commit()

  def set_right_motor_ratio(self, ratio, commit = True):
    if ratio == self.right_motor_ratio: return
    if (ratio < -1) self.right_motor_ratio = -1.0
    elif (ratio > 1) self.right_motor_ratio = 1.0
    else self.right_motor_ratio = ratio
    if commit:
      self._commit()

  def set_motor_ratios(self, l, r, commit=True):
    self.set_left_motor_ratio(l, False)
    self.set_right_motor_ratio(r, False)
    if commit:
      self._commit()

  def _commit(self):
    GPIO.output(IN1, GPIO.HIGH if self.left_motor_ratio > 0 else GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH if self.left_motor_ratio <= 0 else GPIO.LOw)
    GPIO.output(IN3, GPIO.HIGH if self.right_motor_ratio > 0 else GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH if self.right_motor_ratio <= 0 else GPIO.LOW)
    self.pwm_ENA.ChangeDutyCycle(math.abs(self.left_motor_ratio) * 100)
    self.pwm_ENB.ChangeDutyCycle(math.abs(self.right_motor_ratio) * 100)

  def destroy(self):
    self.pwm_ENA.stop()
    self.pwm_ENB.stop()
    GPIO.cleanup()



