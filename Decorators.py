import random
import time

def testRange(*args, **kwargs):
    def inner(func):
        value = func()
        if value >= kwargs["minimum"] and value <= kwargs["maximum"]:
            print("Value within range: ", value)
            return lambda :value
        else:
            print("Value out of range: ", value)
            return lambda :False

    return inner

def testDifference(func):
    def inner():
        # value = func()
        # previous_temperature = 40
        # # if previous_temperature == None:
        # #     print("First measurement")
        
        # difference = abs(previous_temperature - value)
        # print("Difference : ", difference)
        # if difference <= 1:
        #     print("Valid measurement; difference valid")
        # else:
        #     print("Invalid measurement; difference to big")

        # previous_temperature = value
        return func()
    return inner

      
@testDifference
@testRange(minimum=-25, maximum=140)  
def getTemperature():
    random.seed(time.time())
    return random.randint(-40, 155)


for i in range(0,10):
    print("Forloop")
    test_result = getTemperature()
