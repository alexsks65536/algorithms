from collections import defaultdict

# set_s = defaultdict(dict)
# set_s = defaultdict(int)
# set_s = defaultdict(set)
# set_s = defaultdict(list)
# n = set_s['first', 'second', 'third']
#
# print(set_s)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    print(k, v)


