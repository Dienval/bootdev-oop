---------------------------------
Robin has 2 health and 2 arrows
Sheriff has 2 health and 2 arrows
Robin shoots Sheriff
Sheriff has 1 health and 2 arrows
Sheriff shoots Robin
Robin has 1 health and 1 arrows
Sheriff has 1 health and 1 arrows

Expected Result: ('Robin', 1, 1), ('Sheriff', 1, 1)
Actual Result: ('Robin', 1, 1), ('Sheriff', 1, 1)
Pass
---------------------------------
Friar Tuck has 1 health and 0 arrows
Prince John has 1 health and 0 arrows

Expected Exception: Friar Tuck can't shoot
Actual Exception: Friar Tuck can't shoot
Pass
---------------------------------
King Richard has 1 health and 1 arrows
Prince John has 2 health and 1 arrows
King Richard shoots Prince John
Prince John has 1 health and 1 arrows
Prince John shoots King Richard

Expected Exception: King Richard is dead
Actual Exception: King Richard is dead
Pass
---------------------------------
Robin has 2 health and 2 arrows
Sheriff has 3 health and 1 arrows
Robin shoots Sheriff
Sheriff has 2 health and 1 arrows
Sheriff shoots Robin
Robin has 1 health and 1 arrows
Robin shoots Sheriff
Sheriff has 1 health and 0 arrows

Expected Exception: Sheriff can't shoot
Actual Exception: Sheriff can't shoot
Pass
---------------------------------
Marian has 3 health and 2 arrows
Little John has 3 health and 3 arrows
Marian shoots Little John
Little John has 2 health and 3 arrows
Little John shoots Marian
Marian has 2 health and 1 arrows
Marian shoots Little John
Little John has 1 health and 2 arrows
Little John shoots Marian
Marian has 1 health and 0 arrows
Little John has 1 health and 1 arrows

Expected Result: ('Marian', 1, 0), ('Little John', 1, 1)
Actual Result: ('Marian', 1, 0), ('Little John', 1, 1)
Pass
---------------------------------
Robin has 2 health and 2 arrows
Prince John has 2 health and 1 arrows
Robin shoots Prince John
Prince John has 1 health and 1 arrows
Prince John shoots Robin
Robin has 1 health and 1 arrows
Robin shoots Prince John

Expected Exception: Prince John is dead
Actual Exception: Prince John is dead
Pass
---------------------------------
Little John has 4 health and 3 arrows
Sheriff has 3 health and 2 arrows
Little John shoots Sheriff
Sheriff has 2 health and 2 arrows
Sheriff shoots Little John
Little John has 3 health and 2 arrows
Little John shoots Sheriff
Sheriff has 1 health and 1 arrows
Sheriff shoots Little John
Little John has 2 health and 1 arrows
Little John shoots Sheriff

Expected Exception: Sheriff is dead
Actual Exception: Sheriff is dead
Pass
============= PASS ==============  
7 passed, 0 failed  
