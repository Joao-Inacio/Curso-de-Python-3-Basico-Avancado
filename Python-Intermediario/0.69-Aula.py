"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    global x  # Força a variável a ser global
    x = 10
    def outra_funcao():
        global x
        y = 2
        print(x)
        print(y)
    outra_funcao()
    print(locals())
    print(x)
    print(globals())


escopo()
print(x)
