def numberOfSteps(num):
        " Given an integer num, return the number of steps to reduce it to zero."
        "In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it."
        temp = num
        counter = 0
        while temp!=0:
            if temp%2 == 0:
                temp/=2
                counter += 1
            else:
                temp -= 1
                counter += 1
        
        return counter


if __name__ == '__main__':

    print(numberOfSteps(65))