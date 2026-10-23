print("print hello world")
print("today is a good day")

name = "Enjie Jin"
print (name)

print ("jay")
print('zhangsan')

greet_chinese = "您好，吃了吗？ "
greet_english = "Hello, how are you? "

print(greet_chinese + "张三")
print(greet_english + "李四")

# calculate -x^2 - 2 * x + 3 = 0
import math
a = -1
b = -2
c = 3

print (-b + (math.sqrt(b**2 - 4*a*c)) / (2 * a ))
print (-b - (math.sqrt(b**2 - 4*a*c)) / (2 * a ))

#计算BMI指数
#user_weight = float(input("请输入你的体重(kg): "))
#user_height = float(input("请输入你的身高(m) "))
#user_BMI = user_weight/user_height**2 
#print("您的BMI指数为: " + str(user_BMI))

#偏瘦：user_BMI <= 18.5
#正常: 18.5 < user_BMI <= 25
#偏胖: 25 < user_BMI <= 30
#肥胖 user_BMI > 30

#if user_BMI <= 18.5:
#    print("您的体质偏瘦")
#elif 18.5 < user_BMI <= 25:
#    print("您的体质正常")
#elif 25 < user_BMI <= 30:
#    print("您的体质偏胖")
#else:
#    print("您的体质肥胖")


names = ["Anna","Jay","John"]
for name in names:
    print("Hello!" + name)

nums = [3,1,4]
for n in nums:
    print(n)

char = "loop"
for ch in char:
    print(ch.upper())

