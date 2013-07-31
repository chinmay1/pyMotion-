import cv2
from time import gmtime, strftime
import time

def diffImg0(t0,t1):
    d = cv2.absdiff(t0,t1)
    return cv2.countNonZero(d)

cam = cv2.VideoCapture(0)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_BGR2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_BGR2GRAY)
base = diffImg0(t,t_plus)

while True:
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_BGR2GRAY)

  new = diffImg0(t,t_plus)
  back = base - (base *(37.0/100.0))
  front = base + (base *(37.0/100.0))  
  base = (new+base)/2

if((new > front ) or (new < back)):
      time.sleep(1)
      cv2.imwrite(strftime("%Y.%m.%d.%H.%M.%S", gmtime())+".png",t_plus)
