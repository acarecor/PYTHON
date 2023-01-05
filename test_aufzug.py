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

auswahl = int (input())

if auswahl == 1:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == 2:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg +1)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == 3:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg +1)
    sleep (0.1)
    print ('Aktuelle Etage', eg +2)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == 4:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg +1)
    sleep (0.1)
    print ('Aktuelle Etage', eg +2)
    sleep (0.1)
    print ('Aktuelle Etage', eg +3)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == 5:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg +1)
    sleep (0.1)
    print ('Aktuelle Etage', eg +2)
    sleep (0.1)
    print ('Aktuelle Etage', eg +3)
    sleep (0.1)
    print ('Aktuelle Etage', eg +4)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == 6:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg +1)
    sleep (0.1)
    print ('Aktuelle Etage', eg +2)
    sleep (0.1)
    print ('Aktuelle Etage', eg +3)
    sleep (0.1)
    print ('Aktuelle Etage', eg +4)
    sleep (0.1)
    print ('Aktuelle Etage', eg +5)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == -1:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Sie sind an Etage:', auswahl, 'angekommen')

elif auswahl == -2:
    print ('Sie haben die Etage:', auswahl, 'gewählt ')
    print ('Aktuelle Etage', eg)
    sleep (0.1)
    print ('Aktuelle Etage', eg -1)
    print ('Sie sind an Etage:', auswahl, 'angekommen')
    



