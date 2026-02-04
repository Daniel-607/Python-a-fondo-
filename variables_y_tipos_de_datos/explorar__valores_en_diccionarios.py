
>>> d = {1: 'Gato', 2: 'Perro', 3: 'Mono'}
>>> d.keys(), d.values()
(dict_keys([1, 2, 3]), dict_values(['Gato', 'Perro', 'Mono']))
>>> d.items()
dict_items([(1, 'Gato'), (2, 'Perro'), (3, 'Mono')])
>>> d.get(1), d.get(394), d.get(394, 'No encontrado')
('Gato', None, 'No encontrado')
>>> d[2]
'Perro'
>>> d[394]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 394
>>> list(d)
[1, 2, 3]
>>> len(d)
3
>>> 1 in d, 394 not in d
(True, True)
>>> iter(d), reversed(d)
(<dict_keyiterator object at 0x000001F8469BCBD0>, <dict_reversekeyiterator object at 0x000001F846D41940>)
>>> list(iter(d)), list(reversed(d))#forzando a generar una lista desde los iteradores
([1, 2, 3], [3, 2, 1])
