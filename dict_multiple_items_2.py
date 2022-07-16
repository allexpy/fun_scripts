from collections import OrderedDict


d1 = {1: 'Alex', 2: 'Andrei'}
d2 = {1: 'Cristi', 2: 'Ion'}
d3 = {1: 'Sandu', 2: 'Marica'}

d = dict()

d1 = OrderedDict(sorted(d1.items()))
d2 = OrderedDict(sorted(d2.items()))
d3 = OrderedDict(sorted(d3.items()))

d1 = list(d1.items())
d2 = list(d2.items())
d3 = list(d3.items())

d['team_1'] = d1
d['team_2'] = d2
d['team_3'] = d3

d = OrderedDict(sorted(d.items()))
items = list(d.items())
