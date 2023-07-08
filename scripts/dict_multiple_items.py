import operator
from collections import OrderedDict


data = dict()
data['scores'] = dict()
data['both'] = dict()

user = 'Alex'
numbers = '5'

data['scores'][user] = 10
data['both'][user] = (data['scores'][user], numbers)
data['both'] = OrderedDict(sorted(data['both'].items(), key=operator.itemgetter(1), reverse=True))
d = data['both']
items = list(d.items())

print(items[0])
print('----------')
print(items[0][0])
print('----------')
print(items[0][1][0])
print('----------')
print(items[0][1][1])
