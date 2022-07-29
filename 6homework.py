


'''
with open('dataforrle.txt', 'r') as f: 
    dataforrle=f.readline()
def encoding(data):
 count = 1
 res = ''
 for i in range(len(data)-1):
  if i<= len(data):
    if data[i]==data[i+1]:
       count += 1
    else:
     res = res + str(count) + data[i]
     count = 1
  print(res)
  return res
print(encoding(dataforrle))

with open('dataforre2.txt','r')as f11:
    dataforrle11=f11.readline()

def decoding(data): 
    res = '' 
    count = '' 
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else: 
            res = res + symbol * int(count) 
            count = ''
    return res
print(decoding(dataforrle11))


print( ' tic tac toe ')

zone = list(range(1,10))

def draw_zone(zone):
   print('-' * 13)
   for i in range(3):
      print('|', zone[0+i*3], '|', zone[1+i*3], '|', zone[2+i*3], '|')
      print('-' * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input('your turn' + player_token+'? ')
      try:
         player_answer = int(player_answer)
      except:
         print('input number 1-9?')
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(zone[player_answer-1]) not in 'XO'):
            zone[player_answer-1] = player_token
            valid = True
         else:
            print('already occupited')
      else:
        print('incorret number')

def check_win(zone):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if zone[each[0]] == zone[each[1]] == zone[each[2]]:
          return zone[each[0]]
   return False

def main(zone):
    counter = 0
    win = False
    while not win:
        draw_zone(zone)
        if counter % 2 == 0:
           take_input('X')
        else:
           take_input('O')
        counter += 1
        if counter > 4:
           tmp = check_win(zone)
           if tmp:
              print(tmp, 'win!')
              win = True
              break
        if counter == 9:
            print('friendsip win')
            break
    draw_zone(zone)
main(zone)

input('enter to go out')


x=input()
print(eval(x))
'''