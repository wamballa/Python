"""
Challenge 22

Write a program that:
asks the user for the distance (in metres)
asks the user for the time in seconds that a journey was completed in
calculates and outputs the average speed using a function

"""

def averageSpeed (distance,time):
    return distance / time

print ("Average speed calculator")

distance = float(input("Enter the distance travelled in metres: "))
time = float(input("Enter the time taken in seconds: "))

print ("Average speed for your journey is %.2f metres per second" % averageSpeed(distance,time))