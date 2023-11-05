import pprint as pp
data = input()

letters = {}

for i in data:
    letters.setdefault(i, 0)
    letters[i] += 1

pp.pprint(letters)
