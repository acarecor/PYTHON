
def menu():
    print()
    print(' _______________________________ ')
    print('|                               |')
    print('|           Guten Tag!          |')
    print('|-------------------------------|')
    print('| Kaffesorten:                  |')
    print('|                               |')
    print('| 1.Espresso                    |')
    print('| 2.Schwarzer Kaffee            |')
    print('|_______________________________|')
    print()


menu()

while True:
    
        kaffeesorten = int(input('Welchen Kaffee möchten Sie, wählen Sie eine Nummer: '))
        
        
        if kaffeesorten == 1:
            print('Sie haben ein Espresso gewählt')
        elif kaffeesorten == 2:
            print ('Sie haben einen schwarzen Kaffee gewählt')
        else:
            print('Diese Kaffeesorte ist  nicht vorhanden')

        print()
        milch = str(input('Möchten Sie Ihre Kaffee mit Milch?: Ja/Nein: '))

        if milch == 'Ja' or milch =='ja' or milch =='JA':
            print('Sie haben einen Kaffee mit Milch gewählt')
        else:
            print('Sie haben einen Kaffee ohne Milch gewählt')

        print()
        zucker = str(input('Möchten Sie Ihre Kaffee mit Zucker?: Ja/Nein: '))

        if zucker == 'Ja' or zucker=='ja' or zucker=='JA':
            print('Sie haben einen Kaffee mit Zucker gewählt')
        else:
            print('Sie haben einen Kaffee ohne Zucker gewählt')

        print()
        tasse = str(input('Haben Sie Ihre eigene Tasse dabei?: Ja/Nein: '))

        if tasse == 'Ja' or tasse == 'ja' or tasse == 'JA':
            print('Bitte stellen Sie Ihre Tasse in der Kaffeemaschine!. ')
            print('Ihr Kaffee wird vorbereitet')
            print()
           
            print('Ihr Kaffee ist fertig!') 
        else:
            print('Ihr Kaffee wird vorbereitet')
            print()
            
            print('Ihr Kaffee ist fertig!\n')
            print()
            print('      *******************         ')
      
        menu()

