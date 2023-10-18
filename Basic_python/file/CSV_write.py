import csv

output_file = open('out.csv', 'w', newline=' ')
output_writer = csv.writer(output_file)
output_writer.writer(['1','3', '5', '6'])
output_writer.writer(['1','2', '4', '10'])
output_writer.writer(['12','0', '3', '7'])
output_file.close()




