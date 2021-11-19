from yahboom_tank import YahboomTank
import time

tank = YahboomTank()
try:
  tank.set_motor_ratios(1, 1)
  time.sleep(0.5)
  tank.set_motor_ratios(0, 1)
  time.sleep(1)
  tank.set_motor_ratios(1, 1)
  time.sleep(1)
except KeyboardInterrupt:
  pass
tank.destroy()