Complete the Archer class.  

Constructor  
The constructor should take the following parameters in order and set them as properties:  

name  
health  
num_arrows  
get_shot method  
Complete the get_shot method. It doesn't take any parameters.  

If the current archer has health left, remove one health from the current archer. Then, if the archer's health is 0, raise the exception: {} is dead where {} is the archer's name.  

shoot method  
Finish the shoot method. It takes an Archer instance as the target input.  

If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name. Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer. Next, call the target's get_shot() method.  
