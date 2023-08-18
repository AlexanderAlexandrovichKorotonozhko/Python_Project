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

# n = int(input())
# l = []
# for _ in range(n):
#     l.append(int(input()))
# for i in l:
#     if i < 0: print(i)
# for i in l:
#     if i == 0: print(i)
# for i in l:
#     if i > 0: print(i)

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# print(*input().split(), sep='\n')

# for fio in input().split():
#     print(fio[0], end='.')
#     # print('.'.join([fio[0]]))
#
#     # print('.'.join([name[0]]), end='.')

# direct = input().split(chr(92))
# print(*direct, sep='\n')

# for i in input().split():
#     print('+' * int(i))

# ip = input().split('.')
# f = ""
# for i in ip:
#     # print(i)
#     if int(i) < 256:
#         f = "ДА"
#     elif int(i) > 255:
#         f = "НЕТ"
#         break
# print(f)

# print(*list(input()), sep=input())

# # n = input().split() &&&&&&&&&&&&&&&&&&&&&&&&&&&??????????????????????????
# # sc = 0
# # for i in range(len(n)):
# # print(sc)
# a = input().split()
# s = 0
# for i in range(len(a) - 1):
#     s += a[i + 1:].count(a[i])
# print(s)


# names = ['Gvido', 'Roman' , 'Timur']
# if 'Roman' in names:
#     position = names.index('Roman')
#     print(position)
# else:
#     print('Такого значения нет в списке')

# names = ['Gvido', 'Roman' , 'Timur']
# item = names.pop(1)
# print(item)

# numbers = [8, 9, 10, 11]
#
# # print(numbers)
# numbers[1]=17
# # print(numbers)
# numbers.extend([4,5,6])
# # print(numbers)
# numbers.pop(0)
# # print(numbers)
# numbers *= 2
# # print(numbers)
# numbers.insert(3,25)
# print(numbers)

# n = input().split()
# n = list(map(int, n))
# # print(n)
#
# maxi = 0
# mini = 0
# maxi_i = 0
# mini_i = 0
#
# for i in range(len(n)):
#     # print(n[i],i)
#     if n[i] > maxi:
#         maxi = n[i]
#         maxi_i = i
# # print(maxi)
# ma = maxi
# for s in range(len(n)):
#     if n[s] < ma:
#         ma = n[s]
#         mini = n[s]
#         mini_i = s
#
# # print(mini)
# # print(maxi, maxi_i, mini, mini_i)
# n[maxi_i], n[mini_i] = mini, maxi
# print(*n)

# text = (input().lower().split())
#
# a = text.count('a')
# an = text.count('an')
# the = text.count('the')
# art_sum = a + an + the
# print('Общее количество артиклей:', art_sum)

# numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
# numbers.sort()
# del numbers[0]
# del numbers[-1]
# numbers.sort(reverse=True)
# print(numbers)

# stroka = input().split()
# stroka = list(map(int, stroka))
# # print(stroka)
# stroka.sort()
# print(stroka)
# stroka.sort(reverse=True)
# print(stroka)

# print([i ** 2 for i in range(10)])

# chars = [c for c in 'abcdefg']
# print(chars)

# keywords = ['False', 'True', 'None', 'and', 'with',
#             'as', 'assert', 'break', 'class', 'continue',
#             'def', 'del', 'elif', 'else', 'except', 'finally',
#             'try', 'for', 'from', 'global', 'if', 'import',
#             'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#             'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [s[1:] for s in keywords]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue',
#             'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if',
#             'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while',
#             'yield']
#
# lengths = [s for s in keywords if len(s) >= 5]
#
# print(lengths)

# palindromes = [int(i) for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# print(*(i**2 for i in range(1, int(input())+1)), sep='\n')

#--------------------------
# n = input().split()                             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# n = list(map(int, n))
# # print(n)
# print(*([i**3 for i in n]))

# print(*[int(i) ** 3 for i in input().split()]) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-------------------------

# print(*(input().split()), sep='\n' )

# print(*(i for i in input() if i.isdigit()), sep="")

# print(*(int(i)**2 for i in input().split() if int(i)**2 != (int(i)**2[::-1] == 4)))


# n = input().split()
#
# print([int(i)**2 for i in n if int(i) % 2 == 0 and int(i)**2 != 4])

# n = ['2','3','4','5','6','7','78','9']
# n =
# print(n)

print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])

