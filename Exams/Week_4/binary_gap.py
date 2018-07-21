def maxConsecutiveOnes(x):

    count = 0

    while (x!=0):

        x = (x & (x << 1))
  
        count=count+1
     
    return count
 
print(maxConsecutiveOnes(0))
print(maxConsecutiveOnes(55))
print(maxConsecutiveOnes(12345))
print(maxConsecutiveOnes(6))
print(maxConsecutiveOnes(256))
print(maxConsecutiveOnes(22))