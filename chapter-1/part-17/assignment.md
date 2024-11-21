Some lazy code that's managed by another development team is causing some bugs in our team's class. We can fix it by using instance variables instead of class variables.

In the main() function (that our team isn't responsible for), a line like Dragon.element = "fire" should not affect our existing dragon instances! We want our users to specify each dragon's element type when they create a new dragon with the constructor.

Update the Dragon class. Remove the element class variable and instead use an instance variable that's configurable via the constructor.  
