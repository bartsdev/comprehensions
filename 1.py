# def counter(numbers):
#     factorial = 1
#     final = []
#     for number in numbers:
#         for i in range(1, number+1):
#             factorial = factorial*i
#             final.append(factorial)
#             factorial = 1
#     return final

nums = [1,2,3,4,5]



def counter(number):
        for i in range(1, number+1):
            factorial = factorial*i
        print(factorial)
        
counter(nums)