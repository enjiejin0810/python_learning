# #30 days gym chedule
# #in for loop
# for day in range(1,31):
#     print(f'**********Day{day}**********')
#     for group in range(1,4):
#         print(f'This is set {group} of sit-ups!')
#     print(f'Day {day} mission completed! See u tmrw!\n')
# print('training is over, good job!')

#in while loop
day = 1
group = 1
while day <= 30:
    print(f'**********Day{day}')
    group = 1
    while group <= 3:
        print(f'This is set {group} of set-ups!')
        group += 1
    print(f'Day {day} mission completed! See u tmrw!\n')
    day += 1
print('Traning is over, good job!')
