# -*- coding: utf-8 -*-

def subarray(x,y,n):
    minimum = n+1
    for a in range (0,n):
        total = x[a]
        if (total>y):
            return total
        for b in range(a+1,n):
            total += x[b]
            if total>y and (b-a+1) < minimum:
                minimum = (b-a+1)
                result = x[a:b+1]
    return result

array = list(map(int, input("Enter array-X: ").split( )))
number = int(input("Enter the number-y:"))
length = len(array)

sub_arr = subarray(array,number,length)
print("Output subarray of smallest length is",sub_arr)