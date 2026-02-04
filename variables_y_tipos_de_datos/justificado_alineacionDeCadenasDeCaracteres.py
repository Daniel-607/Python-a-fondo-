>>> 'casa'.center(40)
'                  casa                  '
>>> 'casa'.center(40, '.')
'..................casa..................'
>>> 'casa'.center(80, '.')
'......................................casa......................................'
>>> 'casa'.center(2, '_')
'casa'
>>> 'casa'.center(20, '_')
'________casa________'
>>> 'casa'.rjust(40)
'                                    casa'
>>> 'casa'.rjust(40,';')
';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;casa'
>>> 'casa'.rjust(40,':')
'::::::::::::::::::::::::::::::::::::casa'
>>> 'casa'.rjust(40,'>')
'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>casa'
>>> 'casa'.ljust(40)
'casa                                    '
>>> 'casa'.ljust(40,';')
'casa;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'
>>> 'casa'.ljust(40,':')
'casa::::::::::::::::::::::::::::::::::::'
>>> 'casa'.ljust(40,'-')
'casa------------------------------------'
>>> '56'.zfill(20)
'00000000000000000056'
>>> '-56'.zfill(20)
'-0000000000000000056'
>>> '+56'.zfill(20)
'+0000000000000000056'
>>> 'casa'.zfill(20)
'0000000000000000casa'
>>> '-casa'.zfill(20)
'-000000000000000casa'
>>>


'''Se pueden combinar las funciones para formatear textos algo mas complejos, como los siguientes, 
en los que se muestran los resultados de dos equipos:'''

'equipo1:'.ljust(20) + '34'.rjust(5) + 'vs'.center(6) + '12'.ljust(5) + ':equipo2'.rjust(20)
'equipo1:               34  vs  12               :equipo2'
>>>
 