inputs = [input().lower().split(' ')]
text = {element: inputs[0].count(element) for element in inputs[0]}
for element in text.items():
    print(*element)
