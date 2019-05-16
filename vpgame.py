def test():
    global test_case
    '''global no_of_players
    global strength_of_villain
    global strength_of_players'''


   


def vpgame():
    
    
    
    
    test_case=int(input("Enter test case value:- "))
    #if test_case >=1 and test_case <=10:
    if test_case in range(1,10):
        print("The no of total no. of players will be equal as villains and players")
        no_of_players=int(input("Enter the no. of total players, it should be less than 1000: "))
        if no_of_players in range(1,1000):
            no_of_villains=no_of_players
            print("Number of players given by you",no_of_players,"Villains against your players ", no_of_villains,"created")
            for i in range(no_of_villains):
                strength_villains=input("Enter villain strength values:- ")
                if(strength_villains<=100000):
                    strength_of_villains.append(strength_villains)
                else:
                    i-=1
            for i in range(no_of_players):
                
                energy_players=input("Enter villain strength values:- ")
                if(energy_players >=1):
                    energy_of_players.append(energy_players)
        test()
    else:
        print("Please enter valid number of player (from 1 to 1000):-")
vpgame()