#Imprima os primeiros números da série de Fibonacci até passar de 100. A série de Fibonacci é a
# seguinte: 0, 1, 1, 2, 3, 5, 8, 13, 21, etc... Para calculá-la, o primeiro elemento vale 0, o segundo
# vale 1, daí por diante, o n-ésimo elemento vale o (n-1)-ésimo elemento somado ao (n-2)-ésimo elemento
# (ex: 8 = 5 + 3).

#Esperado: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def fib(max)

	f = [0,1]
	
	until f.last > max
		f << f[f.count - 2] + f.last
	end
	
	f
		
end

puts fib(100)

