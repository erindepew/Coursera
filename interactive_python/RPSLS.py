#Rock-Paper-Lizard-Scissors-Spock

def number_to_name(number):
    #(int) -> (string) 
    #takes a number and converts it into the corresponding RPLS variable.
    if number == 0 : 
        number = 'rock'; 
        return number; 
    elif number == 1 :
        number = 'Spock'; 
        return number;  
    elif number == 2 :
        number = 'paper'; 
        return number; 
    elif number == 3 :
        number = 'lizard'; 
        return number;  
    elif number == 4 :
        number = 'scissors'; 
        return number;  
    else :
        return 'invalid input';  
    
def name_to_number(name):
    # (string) -> (int)
    # takes a RPLS variable and converts into the corresponding number.
    if name == 'rock' : 
        name = 0; 
        return name; 
    elif name == 'Spock' :
        name = 1; 
        return name;  
    elif name == 'paper' :
        name = 2; 
        return name;  
    elif name == 'lizard' :
        name = 3; 
        return name;  
    elif name == 'scissors' :
        name = 4; 
        return name;    
    else :
        return 'invalid input'; 
    

def rpsls(name): 
    # (string) -> (string)
    # takes player's choice and plays game of RPLS against computer's randomly generated choice. Displays winner.
     import random; 
    
     player_number = name_to_number(name);
    
     comp_number = random.randrange(0,5); 
     
     print "Player chooses " + name; 
     print "Computer chooses " + number_to_name(comp_number); 
    
     result = (player_number - comp_number)%5;
    
     if result <= 2 and result != 0: 
        print 'Player wins!\n'; 
     elif result > 2: 
        print 'Computer wins!\n'; 
     elif result == 0:
         print "It's a tie!\n"; 

    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
