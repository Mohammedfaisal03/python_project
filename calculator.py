def add(x,y):
    return x+y
def subs(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

operation={
    "+":add,
    "-":subs,
    "*":mul,
    "/":div,
}
def calculator():
    x=float(input("enter first number \n"))
    should_continue=False
    for i in operation:
        print(i)
    while not should_continue:
        direction = input("choose an opreator \n")
        y=float(input("enter the second the number \n"))
        calling_funcion=operation[direction]
        answer=calling_funcion(x,y)

        print(f"the answers is {x} {direction} {y} = {answer} ")

        go_with=input(f"type y to continue with {answer} or n to start with new number ")
        if go_with=="y":
           x=answer
        else:
            should_continue=True
            calculator()

calculator()


