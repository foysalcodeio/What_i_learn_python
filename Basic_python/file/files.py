'''
a = open('create.txt', 'w')
#getting info file name and type
print('name = ', a.name)
print('is it closed ? ', a.close)
print('mood = ', a.mode)
a.write('python is a something')
a.close()


#appending to a file, adding to data
f = open('create.txt', 'a')
f.write('I also love javascript')
f.close()



# r+ function, read file.txt to console
f = open('create.txt', 'r+')
info = f.read(12)
print(info)
f.close()
'''
# w mode, new data write into file.txt
f = open('create.txt', 'w')
f.write('All is lost!!!')
f.close()

