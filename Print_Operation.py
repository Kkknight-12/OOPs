#You have nicely written the codes !!!
#with proper comments. I liked the professionalism in your codes . 

x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)
# Custom separator
print(x, y, z, sep=',')

#  print adds an end-of-line character to terminate the output line.
#  You can suppress this and avoid the line break altogether by passing
#  an empty string to the end keyword argument -> end=' '
print(x, y, z, end='')

# end='...'
print(x, y, z, end='...\n')

# You can also combine keyword arguments to specify both
# separators and end-of-line strings—they may appear in any order but
# must appear after all the objects being printed
print(x, y, z, sep='...', end='!\n')

print(x, y, z,end=''); print(x, y, z)
# end='\n' to break line
print(x, y, z, end='\n'); print(x, y, z)

print('%s...%s' % (x, y))
