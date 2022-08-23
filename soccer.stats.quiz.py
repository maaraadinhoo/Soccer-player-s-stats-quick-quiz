print('welcome to the quiz game press 1 and enter')
print()
score = 0
enter = input()
if enter == '1':
  print('Welcome to the quiz game')
  print("-"*50)
  
  
else:
  print('Bye bye')
  quit()
print()
print("-"*50)
print()
answer = input('how many goals does C.Ronaldo have in his career? in (8/22/2022) ')
if answer == '814':
  print('Bravo!')
  score +=1

else:
  print('sorry wrong anwer')
  score = 0
print()
print("-"*50)
print()
answer = input('how many goals does Neymar Jr have in his career? in (8/22/2022)')
if answer == '420':
  print('Bravo!')
  score +=1
  
else:
  print('sorry wrong anwer')
  score = 0
print()
print("-"*50)
print()
answer = input('how many goals does L.Messi have in his career? in (8/22/2022)')
if answer == '773':
  print('Bravo!')
  score +=1

else:
  print('sorry wrong anwer')
  score = 0
print('-'*50)
print('congrats you earned ' + str(score) + ' points today')
