from pizzapi import *

address = Address('1347 Angora Lake Road', 'South Lake Tahoe', 'CA', '96150')

aaron = ('Aaron', 'Pfister', 'akpfister@live.com', address)

store = address.closest_store()

print(store.data)

menu = store.get_menu()

print('\n' * 10)

print(menu.display())
