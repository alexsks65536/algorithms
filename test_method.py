from collections import OrderedDict


data = OrderedDict.fromkeys('abcde')
print(data)

data.move_to_end('e', last=False)
print(data)

# data.move_to_end('b', first=True)
# print(data)
#
# data.rotate(1)
#
# data.move_to_start('d', last=True)
