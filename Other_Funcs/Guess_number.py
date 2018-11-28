sum = 0
l = [1,2,3]
for i in l:
    sum+=i
print(sum/len(l))

from random import randrange

guess_number=randrange(1,10)
not_bingo=True
miss_try=1

print('I\'ve chosen a number from 1 to 10! Try to guess it in 3 times!')

while not_bingo and(miss_try <= 3):
    your_num=input('Your turn #' + str(miss_try) + ': ')
    if (int (your_num) == guess_number):
        print('Bingo! You\'ve guessed my number! It is ', guess_number)
        not_bingo=False
        break
    else:
        print('Do you need a hint? My number is between', guess_number - 2, ' and', guess_number + 2)
    miss_try += 1
else:
    print('Unfortunatelly, you haven\'t guessed my number in 3 times. Try next time!')