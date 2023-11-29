# Question 1
# create avg function in python
def avg(*args):
    length_of_numbers = len(args)
    sum_of_numbers = sum(args)

    return float(sum_of_numbers / length_of_numbers)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print(res)

# Question 2 
# String Representations of Objects

# class car 
# constructor : max_speed, unit_of_speed (km/h, mph)
# return strings : Car with the maximum speed of {max_speed} {speed_unit}

# classboat
# constructor : max_speed (knots)
# for output : Car with the maximum speed of {self.max_speed} knots 

class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit
    
    def __str__(self) -> str:
        return f'Car with the maximum speed of {self.max_speed} {self.speed_unit}'

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    
    def __str__(self) -> str:
        return f'Car with the maximum speed of {self.max_speed} knots'
