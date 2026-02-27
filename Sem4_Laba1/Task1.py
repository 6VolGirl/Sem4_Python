import random
import time


def findElemenOfSum1(nums: list, target: int) -> list:
    """
    Находит индексы двух чисел из списка nums, которые в сумме дают target.
    """
    for i in range(len(nums)):
        secondNumber = target - nums[i]
        if (secondNumber in nums[i+1:]):
            j = nums.index(secondNumber, i+1)
            return [i, j]
    return []




def findElemenOfSum2(nums: list, target: int) -> list:
    """
    Находит индексы двух чисел из списка nums, которые в сумме дают target.
    С использованием словаря
    """
    numIndex = {}    #ключом - число, значение - индекс
    for id, num in enumerate(nums):
        secondNumber = target - num

        if secondNumber in numIndex:
            return [numIndex[secondNumber], id]
        numIndex[num] = id

    return []



nums = list(random.randint(-10000000,10000000) for _ in range(10000000))
#nums = [1, 7, 3, 3, 11, 2]
target = random.choice(nums)
#print (nums)

start_time1 = time.time()
print(findElemenOfSum1(nums, target))
end_time1 = time.time()
timeBad =end_time1-start_time1
print(f"Time1: {timeBad:.20f}")

start_time2 = time.time()
print(findElemenOfSum2(nums, target))
end_time2 = time.time()
timeGood =end_time2-start_time2
print(f"Time2: {timeGood:.50f}")