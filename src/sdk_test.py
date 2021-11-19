from yahboom_tank import YahboomTank
import time

tank = YahboomTank()

try:
  # tank.wait_for_activate_key()
  # # print(tank.get_sonar_distance())
  # time.sleep(1)
  # state = 0

  # tank.servo_appointed_detection(0)
  # time.sleep(1)

  # tank.servo_appointed_detection(180)
  # time.sleep(1)

  # tank.servo_appointed_detection(90)
  # time.sleep(1)
  while True:
    dist = tank.get_sonar_distance()
    print(dist)
    if dist > 65:
      tank.set_motor_ratios(0.7, 0,7)
    else:
      tank.set_motor_ratios(-.7, 0.7)

    if state == 0:
      tank.servo_appointed_detection(0)
      time.sleep(.3)
      state = 1
    else:
      tank.servo_appointed_detection(180)
      time.sleep(.3)
      state = 0




  # tank.set_motor_ratios(.5, .5)
  # time.sleep(1)
  # tank.set_motor_ratios(-.5, -.5)
  # time.sleep(1)
  # tank.set_motor_ratios(0, .5)
  # time.sleep(1)
  # tank.set_motor_ratios(.5, 0)
  # time.sleep(1)
  # tank.set_motor_ratios(-.5, .5)
  # time.sleep(1)
  # tank.set_motor_ratios(.5, -.5)
  # time.sleep(1)



except KeyboardInterrupt:
  pass

tank.destroy()