# the list "walks" is already defined
# your code here
distance = 0
for dic in walks:
    distance += dic.get('distance')
print(distance // len(walks))
