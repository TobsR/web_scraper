# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
count_groups = []
groups_number = int(input())
groups_dict = dict.fromkeys(groups)
for i in range(groups_number):
    groups_dict[groups[i]] = int(input())
print(groups_dict)
