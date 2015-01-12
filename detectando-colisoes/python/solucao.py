#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Escreva um programa que, dados dois retângulos, determine se eles se interceptam ou não.
Entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). Cada caso de teste contém duas linhas. Cada linha contém quatro inteiros (x0, y0, x1, y1, sendo 0 ≤ x0 < x1 ≤ 1.000.000 e 0 ≤ y0 < y1 ≤ 1.000.000) separados por um espaço em branco representando um retângulo. Os lados do retângulo são sempre paralelos aos eixos x e y.
Saída

Seu programa deve imprimir, na saída padrão, uma única linha para cada caso de teste, contendo o número 0 (zero) caso não haja interseção ou o número 1 (um) caso haja.

>>> detect([0, 0, 1, 1], [0, 0, 1, 1]) 
1

>>> detect([0, 0, 2, 2], [1, 1, 3, 3])
1

>>> detect([0, 0, 1, 1], [2, 2, 3, 3])
0

=======================================

>>> detect([5, 5, 7, 7], [7, 5, 9, 7])
1

>>> detect([5, 5, 7, 7], [7, 7, 9, 9])
1

>>> detect([5, 5, 7, 7], [5, 7, 7, 9])
1

>>> detect([5, 5, 7, 7], [3, 5, 5, 7])
1

>>> detect([5, 5, 7, 7], [5, 3, 7, 5])
1

>>> detect([5, 5, 7, 7], [3, 7, 5, 9])
1

>>> detect([5, 5, 7, 7], [3, 3, 5, 5])
1

>>> detect([5, 5, 7, 7], [7, 3, 9, 5])
1

>>> detect([5, 5, 7, 7], [6, 6, 8, 8])
1

>>> detect([5, 5, 7, 7], [4, 6, 6, 8])
1

>>> detect([5, 5, 7, 7], [4, 4, 6, 6])
1

>>> detect([5, 5, 7, 7], [6, 4, 8, 6])
1

>>> detect([5, 5, 7, 7], [3, 6, 8, 8])
1

>>> detect([5, 5, 7, 7], [6, 4, 8, 8])
1

>>> detect([5, 5, 7, 7], [3, 4, 8, 6])
1

>>> detect([5, 5, 7, 7], [4, 4, 6, 8])
1


========================================

>>> detect([4, 4, 6, 8], [5, 5, 7, 7])
1

>>> detect([3, 4, 8, 6], [5, 5, 7, 7])
1

>>> detect([6, 4, 8, 8], [5, 5, 7, 7])
1

>>> detect([3, 6, 8, 8], [5, 5, 7, 7])
1

>>> detect([6, 4, 8, 6], [5, 5, 7, 7])
1

>>> detect([4, 4, 6, 6], [5, 5, 7, 7])
1

>>> detect([4, 6, 6, 8], [5, 5, 7, 7])
1

>>> detect([6, 6, 8, 8], [5, 5, 7, 7])
1

>>> detect([7, 3, 9, 5], [5, 5, 7, 7])
1

>>> detect([3, 3, 5, 5], [5, 5, 7, 7])
1

>>> detect([3, 7, 5, 9], [5, 5, 7, 7])
1

>>> detect([5, 3, 7, 5], [5, 5, 7, 7])
1

>>> detect([3, 5, 5, 7], [5, 5, 7, 7])
1

>>> detect([5, 7, 7, 9], [5, 5, 7, 7])
1

>>> detect([7, 7, 9, 9], [5, 5, 7, 7])
1

>>> detect([7, 5, 9, 7], [5, 5, 7, 7])
1

"""

desenv = True

def detect(ret_a, ret_b):
    
    if ( ret_b[0] <= ret_a[2] <= ret_b[2] ) or ( ret_a[0] <= ret_b[2] <= ret_a[2] ):
        
        if ret_a[1] <= ret_b[1] <= ret_a[3] or ret_a[1] <= ret_b[3] <= ret_a[3]:
           return 1

        if ret_a[1] <= ret_b[1] <= ret_a[3] and ret_a[1] <= ret_b[3] <= ret_a[3]:
            return 1

        if ret_b[1] <= ret_a[1] <= ret_b[3] and ret_b[1] <= ret_a[3] <= ret_b[3]:
            return 1

    return 0

def _doctest():
    
    import doctest
    doctest.testmod()
    
if desenv:
    if __name__ == "__main__":      
        
        _doctest()

else:
    line_a = raw_input()
    ret_a = map(int, list(line_a.replace(" ", "")))

    line_b = raw_input()
    ret_b = map(int, list(line_b.replace(" ", "")))

    print detect(ret_a, ret_b)
    
