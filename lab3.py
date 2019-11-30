import Cifer


site = Cifer.SPR.Server('shmail.ru')

evgeniy = Cifer.SPR.Client('onejka228')
tatyana = Cifer.SPR.Client('larina2000')

evgeniy.register(site, 'ilovetatyana')
tatyana.register(site, 'onegindebil')

print(str(site))

evgeniy.login(site, 'ilovetatyana')
