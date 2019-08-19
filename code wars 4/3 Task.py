def solution(number):
    summan=0
    for i in range(number):
        if i%3==0 or i%5==0:
            summan+=i
    return summan