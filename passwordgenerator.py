import random

lower = 'dewansh'

upper = 'DEWANSH'

number = '0559'

symbol = '()*'

all = lower + upper + number + symbol

len = 12

password = "".join(random.sample(all,len))

print('Your password is '+ password)