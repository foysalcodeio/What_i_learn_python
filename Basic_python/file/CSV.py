import csv

file = open('example.csv')
file_reader = csv.reader(file)

# data = list(file_reader)
# print(data)

for row in file_reader:
    print('Row no = '+str(file_reader.line_num)+' ' + str)