# read animals.txt
# and write animals_new.txt
file = open('animals.txt', 'r', encoding='utf-8')
file_out = open('animals_new.txt', 'w', encoding='utf-8')
for x in file:
    file_out.write(x.rstrip() + ' ')
file.close()
file_out.close()
