Take a look at the code we wrote. We started with this:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

And refactored the code to look like this:

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]

soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)


############################
DON'T REPEAT YOURSELF (DRY)
############################

We don't want too much of our code doing the same thing. When code is duplicated, it leads to many potential problems. In our example, let's pretend the soldier dictionary changed, and now the key that stores the "damage" value is called dmg.

In the first example, we would need to update two lines of code. In the second example, we only need to make the change in one place.

It's not a big deal when two lines are the same and exist right next to each other. However, imagine if we had done this several hundred times in ten or twenty different code files! All of a sudden, it makes a lot of sense to stop repeating yourself and write more reusable functions. We call that DRY code.


Question 1 (mult. choice):

DRY stands for

[ ]...Don't shave yaks   
[X]...Don't repeat yourself   
[ ]...Don't do drugs   
[ ]...Do repeat yourself


Question 2 (mult. choice):

DRY code does NOT...

[ ]...make your code shorter and easier to read   
[X]...make your code run faster   
[ ]...make your code easier to update   
[ ]...make fixing bugs faster, you only fix them in one place   
