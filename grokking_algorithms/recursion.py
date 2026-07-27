# Recursion is the act of uses the functions inside the function, in this case i'm using recursion and call stack to make this fatorial function
# in this case i used the fatorial concept for high school

def fat(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)
    