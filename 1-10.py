#1
nums = [100, 200, 300, 400, 500]
nums.pop()
nums.pop()
print(nums)

#2
l = [200, 100, 300]
l.insert(2, 10000)
print(l)

#3
#답은 3번

#4
#3번 class 'str'

#5
#답은 4번

#6
#정답 2번

#7
#답은 3번 5번

#8
#답은 84

#9
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

#10
n = int(input())
for i in range(1,n+1):
	print(" "*(n-i)+("*"*(2*i-1)))