from time import sleep
auswahl = 0
etage = 0
eg = 0

'''
Programm Fahrstuhl
'''
print('+------------------------------+')
print('|       Fahrstuhl Menu         |')
print('| ____________________________ |')
print('|                              |')
print('|       Auswahl Menü:          |')
print('|                              |')
print('|        Etage 6               |')
print('|        Etage 5               |')
print('|        Etage 4               |')
print('|        Etage 3               |')
print('|        Etage 2               |')
print('|        Etage 1               |')
print('|        EG                    |')
print('|        Etage -1              |')
print('|        Etage -2              |')
print('|                              |')
print('|       -------------------    |')
print('|       Wähle eine Etage       |')
print('+------------------------------|')
print()

auswahl = int(input())
print ('Sie haben die Etage:', auswahl, 'gewählt ')

while eg < auswahl:
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    eg = eg +1
    
    if eg == auswahl:
        print ('Sie sind an Etage:', auswahl, 'angekommen')
    
while eg > auswahl:
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    eg = eg -1
    
    if eg == auswahl:
        print ('Sie sind an Etage:', auswahl, 'angekommen')



    
