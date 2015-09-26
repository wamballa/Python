"""
Challenge 7

Write a program that:
asks the user how long on average they spend watching TV each day
if it is less than 2 hours, outputs ‘That shouldn’t rot your brain too much’; if it is less than 4 hours per day, outputs ‘Aren’t you getting square eyes?’; otherwise outputs ‘Fresh air beats channel flicking’
"""
hours=int(input("How many hours of TV do you watch?"))
if hours <2:
    print("That shouldn't rot your brain to much")
elif hours <4 and hours >=2:
    print("Aren't you getting square eyes?")
elif hours >=4:
    print("Fresh air beats channel flicking")
