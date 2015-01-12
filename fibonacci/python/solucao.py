#*-* coding: utf-8 *-*

"""
Imprima os primeiros números da série de Fibonacci até passar de 100. A série de Fibonacci é a seguinte: 0, 1, 1, 2, 3, 5, 8, 13, 21, etc... Para calculá-la, o primeiro elemento vale 0, o segundo vale 1, daí por diante, o n-ésimo elemento vale o (n-1)-ésimo elemento somado ao (n-2)-ésimo elemento (ex: 8 = 5 + 3).

Esperado
>>> fib()
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


"""

def fib():

    f = [0, 1]
    i = 2
    while f[len(f)-1] < 102:
        
        f.append(f[i-1] + f[i-2])
        i = i + 1

    return f

def _doctest():

    import doctest
    doctest.testmod()        

if __name__ == '__main__':

    _doctest()
    
