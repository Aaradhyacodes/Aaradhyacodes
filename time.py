import time
# get current hour ( 0-23)
hour = int(time.strftime("%H"))
if 0 <= hour < 12:
 print("good morning")
elif 12<=hour<18:
 print("good afternoon")
else:
 print("good evening")
