import random

moves_a=[14,11,25]
pyraminx=['R','L','U','B']
c3x3=[['F','B'],['R','L'],['U','D']]



while True:
    count=0
    choice=input('\n1 - pyraminx\n2 - 2x2\n3 - 3x3\n"X" to stop\n\npuzzle: ')
    if choice=='X':
        break
    if choice in [str(i) for i in range(1,4)]:
        choice=int(choice)
    else:
        print('\nerror...\n\n')
        continue
    
    print('- A={} moves'.format(moves_a[choice -1]))
    cin=input('moves: ')
    if cin=='A':
        n_turn=moves_a[choice -1]
    else:
        try:
            n_turn=int(cin)
        except ValueError:
            print('\nerror...\n')
            continue


    while True:

        scramble=[]
    
    #####pyraminx#####
        
        if choice==1:

            for i in range(random.choice(range(1,5))):
                scramble.append(random.choice([e for e in pyraminx if e.lower() not in [k[0] for k in scramble]]).lower()+random.choice(['',"'"]))
                repeat=''
                while len(scramble)<n_turn:
                    repeat=random.choice([e for e in pyraminx if e != repeat])
                    scramble.append(repeat+random.choice(['',"'"]))
    
    #####2x2#####

        if choice == 2 :
                
            ind = random.choice(range(3))
            while len(scramble) < n_turn :
                scramble.append (random.choice(c3x3[ind]) + random.choice(['', "'", '2']))
                ind = random.choice ([i for i in range(3) if i != ind])
              
    #####3x3#####      

        if choice==3:

            nottorepeat=[]
            
            while len(scramble)<n_turn:
                list=random.choice(c3x3)
                mossa=random.choice(list)
                if mossa in nottorepeat:
                    continue
                scramble.append(mossa+random.choice(['',"'",'2']))        
                
                if len(nottorepeat)==1 and nottorepeat[0] in list:
                    nottorepeat.append(mossa)
                else:
                    nottorepeat=[mossa]

    #####end#####

        count+=1
        n=0
        print('\nscramble {}:'.format(count) )
        while n < n_turn:
            print(' '.join(scramble[n:(n+7 if n+7<= n_turn else -1 )]) )
            n+=7
        if input()=='C':
            print(''.join(['\n' for i in range(2)]))
            break
