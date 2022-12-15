import random, time

# TODO 1: Print a welcome message. Include "press Enter to start".
print("Welcome! Please press enter to start")
# TODO 2: use input() to wait for the user to press Enter
input()
# TODO 3: wait a random number of seconds, then print "DRAW!"
time.sleep(2)
print("DRAW!")
# TODO 4: Time how long it takes for the user to press Enter. Get the current time with time.time()
currentTime = time.time()
# TODO 5: use input() to wait for the user to press Enter
input("Press enter")
# TODO 6: Use time.time() again to get the time after the user pressed Enter
timeNow = time.time()
# TODO 7: Print how long it took
howLong = timeNow - currentTime
time.sleep(1)
print(howLong)
# TODO 8: Print different results, based on how long it took
if howLong > 0.3:
  print("Too slow! Try again next time.");
elif howLong < 0.1:
  print("You pressed enter too soon, didn't you?");
else:
  print("You're the fastest draw in the west, Congratulations!")