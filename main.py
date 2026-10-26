import math 
# 1 ceil songa eng yaqin butun soni yuqoridan oladi 
# print(math.ceil(-7.9))

# 2 floor songa eny yaqin butun soni pastdan oladi 
# print(math.floor(0.3))

# 3 trunc kasr soning butun qismini oladi 
# print(math.trunc(2.3))

# 4 fabs soning absolyut qiymatini modulini oladi 
# print(math.fabs(-96.3))

# 5 factorail n soning faktorialini shiqaradi 
# print(math.factorial(5))

# 6 comb n ta elementdan k tasini olish usullar yigindisi 
# print(math.comb(5,2))

# 7 perm n ta element bilan k elementlarning orin almashtirishlar sonin 
# print(math.perm(5,2))

# 8 sqrt noning ildizi 
# print(math.sqrt(25))

# 9 log(x, base) soning logarifmi agar tikar bolmasa ln(x) qilip olip ketadi 
# print(math.log(2.71))

# 10 log2(x) 2 tikarda logarifm x 
# print(math.log2(4))

# 11 log10(x) 10 tikarda logarifm x 
# print(math.log10(10000))

# 12 radians x gradusni radian ga otkazish 
# angle = 90 
# radian = math.radians(angle)
# print(radian)

# 13 sin(x) x sining sinusi 
# print(math.sin(radian))

# 14 cos(x) x ning cosinusi 
# print(math.cos(radian))

# 15 tan(x) x ning tangensi 
# print(math.tan(radian))

# Dictionaries 
# my_dict = {1,2,3,4,5,6,7,8,9}
# print(my_dict)

# Sets 
# my_set = {1,2,3,5,5,5,6,6}
# print(my_set)

# Lists 
# my_list = [
#     1,2,3,4,65,12,9,52
# ]
# print(my_list)
# 1 append(x) aqirina taza bir element qosiw 
# my_list.append(1000)
# print(my_list)

# 2 pop(index) index arqali element oshiriw 
# my_list.pop(0) 
# print(my_list)

# 3 insert(index,value) berilgen index tin aldini taza element qosiw
# my_list.insert(0,30)
# print(my_list)

# 4 sort() elementlerdi A dan Z ke shekem yamasa -inf ; +inf [reverse=True] bolsa kerisi
# my_list.sort(reverse=True)
# print(my_list)


# Important set methods 
# my_set = {1,2,3,4,6,7,8,9}
# my_list = [0,540,64898,165]
# # my_set.update(my_list)
# # print(sorted(my_set))
# A = {1,2,3,4}
# B = {5,6,7,8,9}
# x = A.union(B)
# A_elements = A.difference(B)
# a = A.symmetric_difference(B)
# print(a)


# Tuples 
# my_tuple = (
#     1,2,3,4,5,6,7,8,9
# )
# print(my_tuple)

# numbers = {1, 2, 2, 3, 4, 4, 4, 5}
# print(len(numbers))

# a = set()
# b = set()
# print(a | b)

# x = set()
# y = set()
# print(len(a.difference(b)))

# a = set()
# b = set() 
# count = 0
# x = a.union(b) 
# if x%3 ==0 :
#     count+=1
#     print(count)
# else:
#     print('No')



# Basic Functions 
# def square(n) : 
#     return n**2
# print(square(5))

# def is_even(n):
#     if n %2 == 0 :
#         return True 
#     else:
#         return False 
# print(is_even(7))    

# def maximum(a,b,c):
#     return max(a,b,c)
# print(maximum(1,2,3))

# def sum_a(a):
#     result = 0 
#     for x in range(1,a+1):
#         result+=x
#     return result 
# print(sum_a(5))    


# exercise 5  not solved 
# def count_divissors(n):
#     count = 0
#     if n<=0:
#         return count 
#     else:
#         for a in range(1,n+1):
#             if n % a == 0 or n % a ==1:
#                 count += 1
#                 return count
#             else:
#                 return count 
# print(count_divissors(5))            


# exercise 6  not solved 
def is_prime(n):
    count  = 0
    limit = int(n**0.5)
    for x in range(1,limit+1):
        if n % x == 0:
            if x == n //x:
                count+=1
        else:
            count+=2
    return count 
print(is_prime(12))        




# exercise 7 
# def digit_sum(n):
#     result = 0 
#     result += n%10
#     n//10
#     return result
# print(digit_sum(32))

# exercise 8 solved 
# def greatest(a,b):
#     divissors_of_a = set()
#     divissors_of_b = set()
#     for x in range(1,a+1):
#         if a % x == 0 :
#             divissors_of_a.add(x)
#     for y in range(1,b+1):
#         if b%y==0:
#             divissors_of_b.add(y)
#     common_divissors = divissors_of_a.intersection(divissors_of_b)
#     result = max(common_divissors)
#     return   result 
# print(greatest(12,21))

# exercise 9  not solved 




# exercise 10 not solved 
# def is_perfect(n):
#     divissors = []
#     for a  in range(1,n+1):
#         if n % a == 0 :
#             divissors.append(a)
#     if sum(divissors) == n :
#         return True 
#     else:
#         return False 
# print(is_perfect(6))    
            






