
def deuce():
    length = getLength()
    num = getNum()
    nums = getLenList(length)
    nums = mergeSort(nums)
    res = sumSearch(nums, num)
    printRes(res, num, nums)
     
def getLength():
    length = int(input('Enter a length between 1 and 100:'))
    return length

def getNum():
    num = int(input('Enter a sum to search for between 1 and 100:'))
    return num

def getLenList(length):
    import random
    nums = random.sample(range(0, 100), length)
    return nums
    
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        low = nums[:mid]
        high = nums[mid:]
        #Recursive call each half
        mergeSort(low)
        mergeSort(high)
        #two iterators for traversing the two halves
        i = 0
        j = 0
        #iterator for the main list
        k = 0
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                #The value from the low half has been used
                nums[k] = low[i]
                #Move the iterator forward
                i += 1
            else:
                nums[k] = high[j]
                j+=1
            #move to the next slot
            k+=1
        while i < len(low):
            nums[k] = low[i]
            i+=1
            k+=1
        while j < len(high):
            nums[k]=high[j]
            j+=1
            k+=1
        return nums
    
def sumSearch(nums, num):
    res = []
    #Runs each number in nums 1 at a time
    for i in nums:
        first = 0
        last = len(nums)-1
        #Solution + i = num
        solution = (num - i)
        #While loop will run until res list gets entry, or first<=last
        while first <= last and not res:
            mid = (first + last)//2
            if nums[mid] == solution:
                res.append(i)
                res.append(solution)
                return res
            else: 
                if solution < nums[mid]:
                    last = mid-1
                else:
                    first = mid+1
    return res
        
def printRes(res, num, nums):
    if not res:
        #If there aren't two numbers that sum the desired number, the list is 
        #also printed to show there aren't any sums
        print(nums)
        print('No Solution')
    else:
        print('{} + {} = {}'.format(res[0], res[1], num))   

deuce()
