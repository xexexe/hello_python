name = raw_input('What is your name?\n')
print 'Hi, %s.' % name

#My practice
age = raw_input('How old are your?\n')
age_int = int(age)
if age_int > 20 and age_int <=40:
    print 'Hi, %s, your are young' %name
elif age_int > 40 and age_int <= 80:
    print 'Hi, %s, o.o' %name
elif age_int > 80:
    print 'Hi, %s, your are older man' %name
