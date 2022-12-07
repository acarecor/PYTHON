
def showInstructions():
 
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  
  print('---------------------------')
  print('You are in the ' + currentRoom)
  
  print('Inventory : ' + str(inventory))
 
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")




inventory = []
rooms = {



           'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item'  : 'key'
                },



           'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                },
            
            'Dining Room' : {
                  'weast' : 'Hall',
                  'south' : 'Garden',
                  'item' : 'poison',
                },
           'Garden': {
             'north': 'Dining Room'}



        }

currentRoom = 'Hall'

showInstructions()



while True:

  showStatus()

  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()


  if move[0] == 'go':
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
    else:
      print('You can\'t go that way!')

  if move[0] == 'get' :
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      del rooms[currentRoom]['item']
    else:
      print('Can\'t get ' + move[1] + '!')

  if "item" in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  if currentRoom == 'Garden' and 'key' in inventory and 'poison' in inventory:
    print('You are free......YOU win!!!')
    break
    


 
