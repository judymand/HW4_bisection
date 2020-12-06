from decimal import Decimal
import math


def bisection_Method(func,a, b,eps):
    if (func(a) * func(b) > 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    i = 0
    while ((b - a) > eps):

        i += 1
        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (-eps< func(c) <eps):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("number of iterations: ", i)
    return c





'''
 f = function
 eps = epsilon
 g = the derivative function
'''


def roots(f,g,beg,end,step,eps):

    root=[]

    a = beg
    b = a + step

    while b <= end:

        x = f(a)
        y = f(b)
        if -eps < x < eps:
            root.append(a)

        if x * y < 0.0:
            root.append(bisection_Method(f,a,b,eps))



        elif g(a) * g(b) < 0.0:

            res = bisection_Method(g, a, b, eps)
            if -eps < f(res) < eps:
                root.append(res)

        a += step
        b += step


    return root


if __name__ == "__main__":

    eps = 0.0001
    start = float(input('Enter a start range value: '))
    end = float(input('Enter a end range value: '))
    step = float(input('Insert a number of sections: '))
    print(roots(lambda x:4*x**3-48*x+5, lambda x:12*x**2-48, start, end, step, eps))






