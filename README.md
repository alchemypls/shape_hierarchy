# Shape Hierachy
For this assignment I used mostly this [Real Python](https://realpython.com/python-super/) , after it was the 2nd search on google.
and used gemini to learn how to invoke/call/use the functions.

#.super()
I think I kinda understand(?) how .super() works. but in this case it was only taking the color of the Shape class and making sure it was in the rest of the childern classes, at first I was thinking you could put all the auguments in the King(current word for the parent class in my head) and only pick which .super(length) to take, but it's prob better to have each child class create their own.

# my troubles~~~

```bash
triangle = Triangle("blue", 3, 4, 5)
    rectangle = Rectangle("red", 5, 10)
    circle = Circle("green", 4)

    shapes = [triangle, rectangle, circle]
```

This part gave me the most trouble, so if I want to use this style of programming I also need to morp the data I have into a format that the class structure can read/understand. 
More of a 2 step problem then i was thinking.

