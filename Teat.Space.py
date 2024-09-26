#num = int(input())
#if (num % 7 == 0) and (num % 11 != 0):
#    print("YES")
#else:
#    print("NO")

#n = int(input())
#if (5<= n <=9):
#    print("OPEN")
#else: 
#    print("CLOSED")

### Socks
#a = int(input())
#b = int(input())
#print (min(a,b))


#score = int(input())
#if ( 0 <= score <= 40):
#    print("Emerging")
#if ( 41 <= score <= 80 ):
#    print("Developing")
#if ( 81 <= score <= 100 ):
#    print("Achieved")

### Cakes and Bags
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

#if min(a,b) <= min(c,d) and max(a,b) <= max(c,d):
#    print("YES")
#else:
#    print("NO")

#n = int(input())
#for number in range(n, 0,-1):
#    print(number)

#sum = 0 
#n = int(input())
#for number in range(1, n+1, 1):
#    sum += number ** 2 #บวกใส่ค่าเดิมด้วย number ** 2
#print(sum)

### Sum of n Numbers

#sum = 0

#n = int(input())
#for number in range (1,n+1): 
#    num = int(input())
#    sum += num 
#print(sum)

### Print Even Numbers From A to B 
#a = int(input())
#b = int(input())
#for i in range(a, b+1):
#    if i % 2 == 0:
#        print (i)

### Number of Zeros

#sumnum = 0 
#n = int(input())
#for number in range(0, n):
#    i = int(input()) #ไม่รู้ n ใส่ n ในลูป
#    if i == 0:
#        sumnum += 1
#print(sumnum)

### W. Missing Hero
#n = int(input())
#total_sum_of_heroes = n * (n + 1) // 2 
#sum = 0 
#for _ in range(n - 1):
#    hero = int(input())
#    sum += hero 
#missing_hero = total_sum_of_heroes - sum 
#print(missing_hero)

### Incorrect A + B

#f = (input())
#s = (input())
#print(f + s, int(f)+int(s))

### Letter

#s = input()
#i = int(input())
#print(s[i-1])

### Insert In the Middle

#s = input().strip() 
#a = input().strip() 
#middle_index = len(s) // 2
#result_string = s[:middle_index] + a + s[middle_index:]
#print(result_string)

### Z
#a = input()
#middle_index = len(a) // 2
#result = a[middle_index:] + a[:middle_index]
#print(result)

### ZB
#s = input().strip()
#middle_index = len(s) // 2
#middle_three = s[middle_index - 1 : middle_index + 2]
#print(middle_three)

### ZC
#s = input()
#for character in s:
#    print(character)

### ZD
#s = input()
#a_win = s.count("A")
#b_win = s.count("B")
#if a_win > b_win:
#    print("ALICE")
#elif b_win > a_win:
#   print("BOB")
#else:
#   print("DRAW")


### ZF

#str = input()
#flag = True
#for i in range (len(str)):
#    if str[i] != str[len(str)-1 -i]:
#        flag = False
#if flag == True:
#    print("YES")
#else: 
#    print("NO")

### Games

### ZG. Underscores 
def add_underscores(s):
    return '_'.join(s)

s = input() 
print(add_underscores(s))
