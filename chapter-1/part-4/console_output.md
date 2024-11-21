---------------------------------
fight_soldiers inputs: {'damage': 10, 'attacks_per_second': 3}, {'damage': 20, 'attacks_per_second': 1}
expecting: soldier 1 wins
actual: soldier 1 wins
Pass
---------------------------------
fight_soldiers inputs: {'damage': 50, 'attacks_per_second': 1}, {'damage': 50, 'attacks_per_second': 2}
expecting: soldier 2 wins
actual: soldier 2 wins
Pass
---------------------------------
fight_soldiers inputs: {'damage': 100, 'attacks_per_second': 1}, {'damage': 1, 'attacks_per_second': 200}
expecting: soldier 2 wins
actual: soldier 2 wins
Pass
---------------------------------
fight_soldiers inputs: {'damage': 100, 'attacks_per_second': 1}, {'damage': 50, 'attacks_per_second': 2}
expecting: both soldiers die
actual: both soldiers die
Pass
---------------------------------
fight_soldiers inputs: {'damage': 1, 'attacks_per_second': 1}, {'damage': 2, 'attacks_per_second': 1}
expecting: soldier 2 wins
actual: soldier 2 wins
Pass
---------------------------------
fight_soldiers inputs: {'damage': 100, 'attacks_per_second': 10}, {'damage': 100, 'attacks_per_second': 10}
expecting: both soldiers die
actual: both soldiers die
Pass
---------------------------------
fight_soldiers inputs: {'damage': 100, 'attacks_per_second': 2}, {'damage': 50, 'attacks_per_second': 4}
expecting: both soldiers die
actual: both soldiers die
Pass
============= PASS ==============
7 passed, 0 failed
