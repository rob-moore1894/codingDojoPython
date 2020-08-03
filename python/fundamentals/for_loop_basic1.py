#Basic
for x in range(0, 151, 1):
    print (x)

#Multiples of Five
for x in range(5, 1001, 5):
    print (x)

#Counting, the Dojo Way
for x in range(1, 101, 1):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    
    print (x)

#Whoa. That Sucker's Huge
sum = 0
for x in range(1, 500000, 2):
    sum += x
print(sum)

#Countdown by Fours
for x in range(2018, 0, -4):
    print (x)

#Flexible Counter
def flexibleCounter(lowNum, highNum, mult):
    for x in range(lowNum, highNum, mult):
        print(x)

flexibleCounter(2,9,3)