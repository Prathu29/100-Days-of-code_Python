# Good morning sir (Exercise)
import time
timestamp = time.strftime('%H: %M')
print(timestamp)

hours = int(time.strftime('%H'))
if(0<=hours<12):
    print('Good morning')
elif(12<=hours<16):
    print('Good Afternoon')
else:
    print('Good Evening')