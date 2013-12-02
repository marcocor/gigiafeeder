import threading
import time
from threading import Event
from threading import Thread

give_food_event = Event()

def servo_control(food_type):
  print('Servo control started.')
  while True:
   give_food_event.wait()
   print ('Giving food.')
   give_food_event.clear()

servo_t = Thread(target=servo_control, args=['crocchette'])
servo_t.start()
time.sleep(2)
give_food_event.set()
time.sleep(2)
give_food_event.set()


