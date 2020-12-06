# Start
question = input("What are you trying to calculate? ")

# If statements 

if question == "Speed" or question == "speed":
  distance = input("What is the distance the object is traveling? ")
  time1 = input("How long did it take for your object to reach its end point? ")
  speedf = float(distance) / float(time1)
  print("Your speed is " + str(speedf))
elif question == "distance" or question == "Distance":
  speed = input("What is the speed the object is traveling? ")
  time1 = input("How long did it take for your object to reach its end point? ")
  distancef = float(speed) * float(time1)
  print("Your distance is " + str(distancef))
elif question == "Time" or question == "time":
  distance = input("What is the distance the object is traveling? ")
  speed = input("What is the speed the object is traveling? ")
  timef = float(distance) / float((speed))
  print("Your time is " + str(timef))
elif question == "acceleration" or question == "Acceleration":
  velocityf = input("What is your objects final velocity? ")
  velocitys = input("what is your objects starting velocity? ")
  time1 = input("How long did it take for your object to reach its end point? ")
  accelerationf = float(velocityf) - float(velocitys) / float(time1)
  print("Your acceleration is " + str(accelerationf))
else:
  exit("Please enter one of the following: Speed, Time, Distance, or Acceleration!")
  
  
# Again, please note this is a very simple project I have done using Python. Look on my page for more advanced projects, and work!
