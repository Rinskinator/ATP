import random
import time
from functools import wraps

# def testRange(*args, **kwargs):
#     def inner(func):
#         print("Decorator2")
#         value = func()
#         if value >= kwargs["minimum"] and value <= kwargs["maximum"]:
#             print("Value within range: ", value)
#             return lambda :value
#         else:
#             print("Value out of range: ", value)
#             return lambda :False

#     return inner


previous_temperature = []

def temperature_simulator():
    if len(previous_temperature) == 0:
        temperature = random.randint(-40, 155)
        if temperature <= -25 and temperature >= 140:
            return temperature            
    else:
        if random.randint(0,1) == 0:
            if random.randint(0,1) == 0:
                temperature = previous_temperature[-1] + 0.5
            else:
                temperature = previous_temperature[-1] - 0.5
        else:
            if random.randint(0,1) == 0:
                temperature = previous_temperature[-1] + 3.0
            else:
                temperature = previous_temperature[-1] - 3.0

    return temperature
    
def testRange(func):
    def inner():
        value = func()
        if value >= -25 and value <= 140:
            return value
        else:
            return False

    return inner

def testDifference(func):
    def inner():
        value = func()

        if len(previous_temperature) == 0:
            previous_temperature.append(value)
            return True
        else:
            difference = abs(previous_temperature[-1] - value)
            if difference <= 1:
                previous_temperature.append(value)
                return True
            else:
                previous_temperature.append(value)
                return False
    return inner

    
@testDifference                           
@testRange
# (minimum=-25, maximum=140)               
def getTemperature():
    temp = temperature_simulator()
    return temp

for i in range(0,10):
    test_result = getTemperature()
    print("Test result : ", test_result)


print("Previous temperatures: ", previous_temperature)

