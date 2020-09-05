# count

x=int(input('enter speed ',))

count=0

for i in range(70,x+1,5):
    count+=1
    #print(count)
if count > 12:
    print("s")
else:
    print("ok")

#####################

# .get used in loop to itter dictionary

branch = {'spam': 1, 'ham': 2,
'eggs': 3}

for i in branch.get:
    print(i)
####################
#Tuples in for loops also come in handy to iterate through
# both keys and values in dictionaries using the items method
D={'a':1,'b':2,'c':3}

for key in D:
    print(key,"=>",D[key])

list(D.items())

for (key,value) in D.items():
    print(key,"=>",value)

######################
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
   print(a, b, c)

a= [(1, 2, 3), (4, 5, 6)]

for i in a:
    print(i)

for (i, j, k) in a:
    print(i, j, k)

for (i, *j, k) in a:
    print(i, j, k)

#
# nested loop
items =['aaa',111,(4,5),2.01]
tests= [(4,5),3.14]

for key in tests:
    for item in items:
        if item ==key:
            print(key,"was found")
            break
    else:
        print(key,"not found!")

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key,"not found")

[key for key in tests if key in items]
####################
seq1= 'spam'
seq2= 'scam'

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)
[x for x in seq1 if x in seq2]
######################
# indentation

x =1
if x:
    y= 2
    if y:
        print('block2')
    print('block1')
print('block0')

#######################
sum = 0
for x in [1,2,3,4,5]:
    sum += x
print(sum)
#######################
# for loops work on strings and tuples:
S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S: print(x, end=' ')

for x in T: print(x, end=' ')

#####################
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:  # loop target itself can actually be a tuple of targets.
    print(a, b)
for a in T:
    print(a)
#####################
# if .endswith():

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

##############
"""
You can always code such unique iterations with a while loop and 
 manual indexing, but Python provides a set of built-ins that allow 
 you to specialize the iteration in a for:
• The built-in RANGE function produces a series of successively higher 
  integers, which can be used as indexes in a for.
• The built-in ZIP function returns a series of parallel- item tuples,
  which can be used to traverse multiple sequences in a for.
• The built-in ENUMERATE function generates both the values and indexes 
  of items in an iterable, so we don’t need to count manually.
• The built-in MAP function can have a similar effect to zip in Python 2.X,
  though this role is removed in 3.X.
"""
#######
# range
list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
list(range(5,-5,-1))

for i in range(3):
    print(i, 'Pythons')

X = 'spam'
for item in X: print(item, end=' ')

for i in range(len(X)): print(X[i], end=' ')

# zip


S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

for i in range(len(S)):
    x = S[i:] + S[:i]
    print(x, end=' ')


l=[1,2,3]
for i in range (len(l)):
    x= l[i:] + l[:i]
    print(x, end= '')

for i in range (len(l)):
    l= l[1:] + l[:1]
    print(l, end= '')



######## ZIP  ##########

L1 = [1,2,3,4]
L2 = [5,6,7,8]
#in 3.X where we must wrap it in a
# list call to display all its results
# at once
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print(list(zip(T1, T2, T3)))

# Dictionary construction with zip
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
print(list(zip(keys, vals)))


D1 = {'spam':1, 'eggs':3, 'toast':5}
D1
D1['spam']
D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)
# in Python 2.2 and later you can skip the for
# loop altogether and simply pass the zipped
# keys/values lists to the built-in dict constructor
# call:


#Generating Both Offsets and Items: enumerate

S = 'spam'

offset = 0
for item in S:
    print(offset,item)
    offset +=1
# a new built-in named enumerate does the job for
# us—its net effect is to give loops a counter “for
# free,” without sacrificing the simplicity of
# automatic iteration:
for (offset,item) in enumerate(S):
    print(offset,item)
# it returns an (index, value) tuple each time
# through the loop

[offset * item for (offset, item) in enumerate(S)]

#########

# .split()
m='aaaasdfghjkl'
def make_Dictionary(root_dir):
   all_words = []
   #emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
   for line in m:
        words = line.split()
        all_words += words
   print(all_words)

c=0
for i in all_words:
    if (i =='a'):
        c += 1
print(c)

################
# no.logical
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5 ,my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house <11 , your_house <11 ))

###########

D = {'a':1, 'b':2, 'c':3}
for i in D.keys():
    print(i, D[i])

I= iter(D)
next(I)

R = range(10)
R
list(R)
len(R)
I=iter(R)
next(I)

# enumerate
E = enumerate('spam')
E
I=iter(E)
next(I)   # Generate results with iteration protocol
list(enumerate('spam'))


#############
# list comprehension
L = [1, 2, 3, 4, 5]

L= [x+10 for x in L] # list comp
print(L)


z=[x+y for x in 'abc' for y in 'xyz']
print(z)

L = [1, 2, 3]
M=  [1, 1, 1]

for i in L:
    for j in M:
        y=i+j
        print(y)

for i in L:
    for j in M:
        y=i+j
    print(y)

###########
### map , abs
m= map(abs,(-1,0,1,-2,-3))
print(m)
next(m)

for i in m:
    print(i)

for i in m: print(i)

list(map(abs,(-1,0,1,-2,-3)))

#
import numpy as np, pandas as pd

df = pandas.read_csv('/Users/knight/Desktop/datasets/python/datasets_v/SalaryGender.csv', delimiter=',')
salary = numpy.array(df['Salary'])
gender = numpy.array(df['Gender'])
phd = numpy.array(df['PhD'])
age = numpy.array(df['Age'])

np.arange(0,9)
men_count = 0
women_count = 0

for i in range(0, 100):
    if gender[i] == 1 and phd[i] == 1:
        men_count +=1
    if gender[i] == 0 and phd[i] == 1:
        women_count +=1

print(men_count + women_count)


gender=([1, 0, 0, 1, 0, 0, 1, 0])
phd= ([1, 1, 0, 0, 1, 0, 0, 0])
men_count = 0
women_count = 0

for i in range(0, 8):
    if gender[i] == 1 and phd[i] == 1:
        men_count +=1
    if gender[i] == 0 and phd[i] == 1:
        women_count +=1

print(men_count)
print(women_count)