#!/usr/bin/env python3
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def print_fibonacci(length):
    fibo = list()
    for i in range(length):
       fibo.append(recur_fibo(i))
    print(fibo)