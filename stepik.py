# print(list(range(1,5+1)))

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[0:6])

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# s = [min(numbers), max(numbers)]
# print(sum(s))

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens)/len(evens)
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3], rainbow[6] = 'Зеленый', 'Фиолетовый'
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print((numbers1 * 2) + (numbers2 * 9) + numbers3)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[::2]
#
# print(numbers)

# numbers = [4, 2, 8, 6, 5]
# numbers.append(7)
# numbers.append(1)
# print(numbers)

# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers)

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10,
#            10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5,
#            6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
#
# if (5 and 17) in numbers: print('YES')
# else: print('NO')
#
# del numbers[0]
# del numbers[-1]
# print(numbers)

# vvod = int(input())
# rezult = []
# for i in range(vvod):
#     rezult.append(input())
# print(rezult)

# l = []
# for i in range(ord('z') - ord('a') + 1):
#     l.append(chr(ord('a') + i) * (i + 1))
# print(l)

# n = int(input())
# l = []
# for i in range(n):
#     n2 = int(input())
#     n2 **= 3
#     l.append(n2)
# print(l)

# n = int(input())
# l = []
# for i in range(1,n+1):
#     if n % i == 0:
#         l.append(i)
# print(l)

# n, n2 = int(input()), int(input())
# l = []
# for i in range(n-1):
#     nn = int(input())
#     l.append(n2 + nn)
#     n2 = nn
# print(l)

# n = int(input())
# l = []
# l2 = []
# for i in range(n):
#     n2 = int(input())
#     l.append(n2)
#     if l[i] % 2 == 0: # print(l)
#         l2.append(l[i])
# print(l2)

# n = int(input())
# l, l2 = [], []
# for i in range(n):
#     l = int(input())
#     if i % 2 == 0:
#         l2.append(l)
# print(l2)

# n = int(input())
# li = []
# for _ in range(n):
#     li.append(input())
# index = int(input())
# res = ''
# for s in li:
#     if len(s) >= index:
#         res += s[index - 1]
#
# print(res)

# n = int(input())
# l = []
# for i in range(n):
#     l.extend(input())
# print(*l)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# s = []
# sch = 0
# for i in range(len(numbers)):
#     s = numbers[i] ** 2
#     sch += s
# print(sch)

# n = int(input())
# l = []
# l2 = []
# for i in range(n):
#     l.append(int(input()))
#     l2.append((l[i]**2) + (2*l[i]) + 1)
# print(*l, sep='\n')
# print()
# print(*l2, sep='\n')

# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
#
# for s in l:
#     if s != min(l) and s != max(l):
#         print(s)

# n = int(input())
# l = []
# for _ in range(n):
#     l2 = input()
#     if l2 not in l:
#         l.append(l2)
# print(*l, sep='\n')


# n = [input() for _ in range(int(input()))]
# k = [input() for _ in range(int(input()))]
# # print(n)
# # print(k)
# for i in n:
#     for s in k:
#         if s.lower() not in i.lower():
#             break
#     else:
#         print(i)





























