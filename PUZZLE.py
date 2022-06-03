#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import random
piece=()
move = 0
empty_space=()
list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


random.shuffle(list1)

print('\n'*2)


matrix=[]
while list1 !=[]:
    matrix.append(list1[:4])
    list1 = list1[4:]



for x in range (len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 0:
            empty_space = (x,y)




print()


while True:
    print('\n|-----------------|')

    for x in range (len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:

                print('|00' , end='  ')
            else:
                 print('|' + '{:02d}' .format(matrix[x][y]), end='  ') 

        print('\n|-----------------|')       
    
    num = input('\n type the number to move : ( q ) to quit  ')
    if num in ['q','Q']:
        break
    num = int(num)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)

    if num > 15:
        print('illegal move  ')
    else:

        if(empty_space==(piece[0]-1,piece[1]))           or(empty_space==(piece[0]+1,piece[1]))           or(empty_space==(piece[0],piece[1]-1))           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=num
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print()
            print('you have made ',move , 'moves so far ')
            print(2*'\n')
        else:
            print('illegal move , try again ')

print('game over  ')


# In[ ]:




