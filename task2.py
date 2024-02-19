import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.color("blue")

    order = int(input("Enter the order of the Koch snowflake: "))
    size = 300
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    main()
