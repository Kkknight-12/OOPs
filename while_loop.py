
x = 'spam'         # 0= s , 1 = p , 2 = a, m = 3
while x:              # While x is not empty
    print(x, end=' ')
    x = x[1:]         # Strip first character off x

# Note the end=' ' keyword argument used here to place
# all outputs on the same line separated by a space;

#simple iteration in while loop
a = 0 ; b = 10
while a < b:
    print(a,end='')
    a += 1

X = 'spam'
i = 0
while i < len(X):
    print(X[i], end=' ')
    i += 1

"""
break- 
Jumps out of the closest enclosing loop (past the entire loop statement)

continue-
Jumps to the top of the closest enclosing loop (to the loop’s header line)

pass- 
Does nothing at all: it’s an empty statement placeholder

Loop else block-
Runs if and only if the loop is exited normally (i.e., without hitting a break)

General Loop Format

while test: 
    statements
    if test: break       # Exit loop now, skip else if present
    if test: continue    # Go to top of loop now, to test1
else:
    statements           # Run if we didn't hit a 'break'
"""
##################
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue  # Go to top of loop
    print(x, end=' ')

x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print(x, end=' ')
#############

while True:
    name = input('Enter name:')
    if name == 'stop': break   # break if stop is written
    age = int(input('Enter age: '))
    if age <= 10 : break         # breaks if age is written less then equal too 10
    print('Hello', name, '=>', int(age) ** 2)

#########
# else

y = 19
x = y // 2
while x > 1:
   if y % x == 0:
      print(y, 'has factor', x)
      break
   x -= 1
else:
   print(y, 'is prime')

################
# else
found = False
while x and not found:
    if match(x[0]):
        print('Ni')
        found = True
    else:
        x = x[1:]
if not found:
    print('not found')


####################



L = [1, 2, 3]
I = iter(L)                   # Obtain an iterator object from an iterable
print(I.__next__())         # Call iterator's next to advance to next item


I = iter(L)                # Manual iteration: what for loops usually do
while True:
    try:                       # try statement catches exceptions
        X = I.__next__()
    except StopIteration:
        break
    print(X ** 2, end=' ')
