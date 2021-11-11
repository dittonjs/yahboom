from yahboom_tank import YahboomTank
import time

tank = YahboomTank()

try:
  tank.set_motor_ratios(.5, .5)
  time.sleep(1)
except KeyboardInterrupt:
    pass

tank.destroy()