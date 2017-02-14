# Introdução ao Python

# Ementa

* [Instalação](#instalação)
* [Python é interpretado](#python-é-interpretado)
* [Python tem tipagem forte e dinâmica](#python-tem-tipagem-forte-e-dinâmica)
* [strings](#strings)
* [replace](#replace)
* [slices](#slices)
* [listas](#listas)
* [tuplas](#tuplas)
* [split](#split)
* [while](#while)
* [for](#for)
* [if else](#if-else-condições)
* [list comprehensions](#list-comprehensions)
* [type(), help(), dir()](#type-help-dir)
* [atribuições múltiplas](#atribuições-múltiplas)
* [Dicionários](#dicionários)
* [Funções](#funções)
* [Lambda](#lambda)
* [Módulos](#módulos)
* [Testes](#testes)
* [Try/except](#tryexcept)
* [Random](#random)
* [I/O](#io)
* [Orientação a Objetos](#orientação-a-objetos)
* [Conexão com Banco de Dados](#conexão-com-banco-de-dados)

## Instalação

Para quem usa Windows vá em [www.python.org/downloads/](https://www.python.org/downloads/) e baixe Python 3.5.2. Ao instalar não esqueça de marcar o check 'Add Python 3.5 to PATH'.

Para quem usa Linux ou Mac sugiro este [tutorial de instalação com pyenv](https://github.com/rg3915/django-experience/wiki/Instalando-o-pyenv).

```bash
python -V
```

### IPython

```bash
sudo -H pip install ipython
```


## Python é interpretado

O que são os `*.pyc`?

Contém os bytecodes compilados a partir do arquivo `.py`.

Python é uma linguagem interpretada. Mas também compila. Leia mais [aqui](http://henriquebastos.net/diferencas-entre-linguagem-compilada-e-linguagem-interpretada/).

O Python também pode gerar um `.exe` para Windows. Veja [py2exe](http://www.py2exe.org/).


## Python tem tipagem forte e dinâmica

### Tipagem Forte

O Python não transforma um tipo em outro implicitamente.

Exemplo, '1' + 1 em Python dá erro. Em outras linguagens dá '11'.

### Tipagem Dinâmica

A identificação do tipo acontece em Runtime. Em oposição à tipagem estática quando você define o tipo no código fonte como em C, por exemplo.

Exemplo:

```python
>>> a = 42
>>> type(a)
<class 'int'>
>>> b = 3.14
>>> type(b)
<class 'float'>
>>> t = 'palavra'
>>> type(t)
<class 'str'>
```


## O interpretador Python

```bash
$ python
Python 3.5.0 (default, Dec  8 2015, 01:17:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Executando programas Python direto pelo terminal.

```bash
$ python -c "print(40 + 2)"
```

#### Indo além do hello word

```python
from datetime import datetime
from time import sleep

while True:
    hora = datetime.now()
    print(hora.strftime('%H:%M:%S'))
    sleep(1)
```

#### Eu quero ir para

```python
for i in range(1, 11):
    j = i * i
    print(i, j)

print('fim')
```

#### Mão na massa

```python
# lanches.py
import sys
from random import choice

lanches = ['Hot-Dog', 'X-Salada', 'Tapioca', 'Pizza', 'Batata Frita']
bebidas = ['Coca-Cola', 'Fanta', 'Guaraná', 'Suco de Laranja', 'Cerveja']
numero = input('Digite um número de 0 a 4: ')


if int(numero) > 4:
    print('O número digitado está fora do intervalo.')
    # Experimente digitar -5 e -6
    sys.exit(1)


def bebida():
    return choice(bebidas)


for i in range(3):
    if i == 0:
        print('Primeira refeição: %s + %s' % (lanches[int(numero)], bebida()))
    elif i == 1:
        print('Segunda refeição: %s + %s' % (lanches[int(numero)], bebida()))
    else:
        print('Terceira refeição: %s + %s' % (lanches[int(numero)], bebida()))
```

O módulo principal do Python

```python
def hello():
    print('Hello World')


if __name__ == '__main__':
    print('Oi')
```

O segredo de um código pythônico

```python
'''
Um comentário de múltiplas linhas.
Também conhecido como Docstring.
'''
import os


def main():
    print('Hello world!')
    print("O'Relly")
    print('O\'Relly')

    my_sum(5, 10)

    print('=' * 10)
    text = 'O diretório atual é '
    print(text + os.getcwd())

    foods = ['maçãs', 'laranjas', 'bananas']

    for food in foods:
        print('Eu gosto de', food)

    print('Contando até dez:')
    for i in range(1, 11):
        print(i)


def my_sum(a, b):
    value = a + b

    print('%s mais %s é igual a %s' % (a, b, value))

    if value < 50:
        print('foo')
    elif (value >= 50) and \
         ((a == 42) or (b == 24)):
        print('bar')
    else:
        print('moo')

    return value  # comentário de uma linha


if __name__ == '__main__':
    main()
```

Importando sua própria biblioteca

```python
# mycapitalize.py
def _capitalize(texto):
    return texto.capitalize()


# palavras.py
from mycapitalize import _capitalize

palavras = 'joaquim josé da silva xavier'
nome = []

for palavra in palavras.split():
    print(_capitalize(palavra))
    nome.append(_capitalize(palavra))

print(' '.join(nome))
```

## Operadores

```python
(2 ** 10 + 3 * 2) / (48 - 46 + 1976 / 2 + 40)

7 / 3

7 // 3

7 % 3
```

Operadores

`+ - * / ** % //`

```python
bin(4)
bin(7)
```


```python
import math
math.sqrt(25)
math.log(100,10)
math.log(27,3)
math.sin(math.pi/2)
math.pi
from math import radians, pi
radians(180)
radians(180) == pi
```

**Exercício 01:** Um jogo de futebol foi programado para ser realizado com duração normal: 2 tempos de 45 minutos, com um intervalo de 15 minutos. O jogo começou pontualmente às 9:00 horas.

Um repórter cronometrou 6 jogadas que considerou as mais importantes a partir do início do jogo e registrou suas marcas da seguinte maneira:

| Jogada    | Tempo desde o início do jogo |
| --------- | ---------------------------- |
| Falta A   | 590 s                        |
| Pênalti   | 785 s                        |
| Gol I     | 1350 s                       |
| Gol II    | 2690 s                       |
| Falta B   | 4332 s                       |
| Bicicleta | 5960 s                       |

A partir das informações acima, assinale a afirmativa correta.

(A) A falta A aconteceu exatamente às 9h e 9 minutos.

(B) O primeiro gol ocorreu no tempo cravado de 22 minutos e 30 segundos do 1º tempo.

(C) A bicicleta surpreendeu o público aos 39 minutos e 20 segundos do 1º tempo.

(D) O pênalti aconteceu aos 22 minutos e 5 segundos do 1º tempo.

(E) O segundo gol aconteceu no segundo tempo.



## Strings

```python
'k' * 5
'Guido' + ' Van' + ' Rossum'
'Av. ' + str(23) + ' de Maio'
```

```python
nome = 'joaquim josé da silva xavier'
nome.capitalize()
nome.lower()
nome.split()
nome.title()
nome.upper()
```

## Replace

```python
nome.replace('a','4')
```

## Slices

```python
palavra = 'paralelepípedo'
len(palavra)
palavra[0]
palavra[0:3]
palavra[:3]
palavra[4:8]
palavra[8:]
palavra[1:10:2]
palavra[1::2]
palavra[-1]
palavra[:-1]
palavra[::-1]

# Exercício
p1 = 'filho'
p2 = 'de'
p3 = 'algo'
# fidalgo

p4 = 'vinho'
p5 = 'acre'
# vinagre
```

**Exercício 02:** Escreva os textos a seguir capitalizados, exceto as preposições `'da', 'de', 'di', 'do', 'du', 'para'`.


```
'joaquim josé da silva xavier'
'pedro de souza'
'fui para são paulo'
```

**Exercício 03:** Faça um programa que troque o texto 1 pelo texto 2, conforme segue:

texto 1: `'Regis da Silva Santos'`

texto 2: `'R3g15 d4 S1lv4 S4nt05'`

**Exercício 04:** Refaça o exercício 2 de forma genérica para qualquer outro texto obedecendo as mesmas regras.


**Exercício 05:** (*removetags.py*) - Dado o arquivo a seguir retire todas as tags e retorne uma lista contendo todas as palavras.

```html
<html>
<head>
  <title>Título</title>
</head>
<body>
  <div>
    <h1>Bem-vindo(a)</h1>
  </div>
  <div>
    <ul>
      <li>Linux</li>
      <li>Python</li>
      <li>Django</li>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </div>
</body>
</html>
```

## Listas

Toda lista é mutável

```python
lista = [42, 'palavra', 3.14, 2 + 3j, [1, 2, 3]]
for i in lista: print(i)

lista[0]
lista[-1]
lista[-1][-1]
lista.append('mais')
lista.remove('palavra')

L = [100, 2, 80, 7, -5, 42]
L
L.sort()
L

N = [30, 10, 20]
sorted(N)
N
```

### Pilhas com lista

```
a = ['zero', 'um', 'dois', 'três']
a.append('quatro')
a
a.append('cinco')
a
a.pop()
a
a.pop(2)
a
```

## Tuplas

São objetos imutáveis.

```python
t = (1, 2, 3)
type(t)
```

```python
# uma tupla de tuplas
posicoes = ((1, 2), (2, 2), (5, 2), (0, 3))

# um jeito de percorrer
for pos in posicoes:
    i, j = pos
    print(i, j)

print('-' * 10)

# outra forma de percorrer
for i, j in posicoes:
    print(i, j)
```

## Split

```python
palavras = 'joaquim josé da silva xavier'
palavras.split()
```


## While

```python
n = 1
while(n < 11):
    print('n =', n)
```

```python
n = 1
while(n < 11):
    print('n =', n)
    n = n + 1

print('Fim do loop')
```

**Exercício 06:** Imprima a sequência de Fibonacci até 1.000.000 usando while.

**Exercício 07:** Par ou ímpar. Escreva uma função com um parâmetro n que retorne Verdadeiro caso n seja par e Falso caso seja ímpar.

**Exercício 08:** Nota da prova. Escreva uma função que diga a situação do aluno após a prova, baseado nas seguintes regras:

* Se a nota for menor do que 4 --> "Reprovado"
* Se a nota for maior ou igual a 4 e menor do que 7 --> "Recuperação"
* Se a nota for maior ou igual a 7 --> "Aprovado"


**Exercício 09:** Média final. A partir do exercício anterior calcule a média aritmética de três provas e retorne a situação do aluno.

**Exercício 10:** Escreva um programa 'factors.py' que inclua uma função para calcular todos os números inteiros que são divisores de um número dado. Exemplo:

```python
>>>
Digite um número inteiro: 12
1 é um divisor de 12
2 é um divisor de 12
3 é um divisor de 12
4 é um divisor de 12
6 é um divisor de 12
12 é um divisor de 12
```

**Dica:** Use módulo e laço.

**Exercício 11:** Encontre todos os números primos até 120.


## for

```python
for n in range(1, 5):
    print('n =', n)

print('Fim do loop')
```

```python
for n in range(5):
    for j in ['a', 'b', 'c']:
        print('n =', n, 'e j =', j, '--> ', str(n) + ',' + str(j))
```

```python
letters = 'Python'
for letter in letters:
    print(letter)
```

```python
lista = ['', 'Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
for idx, item in enumerate(lista):
    print(idx, item)
```


## if else (condições)

```python
a > b
a < b
a >= b
a <= b
a != b
a == b
```

#### Tabela verdade

```python
True and True
True and False
False and True
False and False
True or True
True or False
False or True
False or False
```

```python
not True
not False
```

```python
if 2 + 2 == 4:
    print('Ok')
else:
    print('Errado')
```

```python
if True:
    print('Verdadeiro')
else:
    print('Falso')
```

Coloque o `not` no exemplo anterior e veja o resultado.

```python
if 3 % 2:
    print('Três é impar')
```

```python
notas = [7, 4, 3.9]
for nota in notas:
    if nota >= 7:
        print('Aprovado')
    elif nota >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
```

**Exercício 12:** Par ou ímpar. Escreva uma função com um parâmetro n que retorne Verdadeiro caso n seja par e Falso caso seja ímpar.


## List Comprehensions

```python
[x ** 2 for x in range(10)]
```

Soma de vetores

```python
a = [1, 2]
b = [9, 18]

c = []
for i in range(len(a)):
    c.append((a[i], b[i]))

for x, y in c: print(x + y)

for i in range(len(a)): print(a[i] + b[i])
[x + y for x, y in zip(a,b)]
list(map(sum, zip(a, b)))
```

Multiplicação por escalar

```python
vec = [1, 2, 3]
[x * 2 for x in vec]
```

```python
def vogal(c):
    return c.lower() in 'aeiou'

print(vogal('a'))
print(vogal('b'))

palavra = 'abacaxi'
vogais = [letra for letra in palavra if vogal(letra)]
print(vogais)
```

**Exercicio 12:** Gerar uma lista de números pares de -10 a 10 usando list comprehensions, e imprimir esta lista.

## type(), help(), dir()

```python
lista = [3, 2, 1]
type(lista)
help(lista)
dir(lista)
type(3.14)
type('palavra')
dir('palavra')
```


## atribuições múltiplas

```python
a, b = 0, 1
a
b
c, d, e = range(3)
c
d
e
vars = ('A', 2, 'C')
a, b, c = vars
```

**Exercício:** Refaça a sequencia de Fibonacci.

## Dicionários

São coleções de valores identificados por chaves únicas.

`{'chave': valor}`

```python
uf = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
```

```python
uf['SP']
uf['RJ']
uf['PR']
uf['PR'] = 'Paraná'
```

```python
for chave in uf:
    print(chave)
```

```python
for chave, valor in uf.items():
    print(chave, valor)
```

```python
for chave, valor in sorted(uf.items()):
    print(chave, valor)
```

* As chaves são sempre únicas
* As chaves têm que ser objetos imutáveis
* Qualquer objeto pode ser um valor
* A ordem de armazenamento das chaves é indefinida
* Dicionários são otimizados para acesso direto a um item pela chave, e não para acesso sequencial em determinada ordem.

### Dicionários: operações básicas

Criar um dicionário vazio

```python
d = {}
d = dict()
```

Acessar um item do dicionário

```python
print(d[chave])
```

Adicionar ou sobrescrever um item

```python
d[chave] = valor
```

Remover um item

```python
del d[chave]
```

Verificar a existência de uma chave

```python
d.has_key(c)
c in d
```

Obter listas de chaves, valores e pares

```python
d.keys()
d.values()
d.items()
```

Acessar um item que talvez não exista

```python
d.get(chave) # retorna None ou default
```

```python
for nome in uf.values():
    print(nome)
```

```python
for nome in sorted(uf.values()):
    print(nome)
```


## Funções

```python
def message():
    pass
```

```python
def message():
    return 'Hello World'
```

```python
def soma(a, b):
    return a + b
```

### Argumentos Posicionais

```python
def func(a, b, c):
    print(a, b, c)

if __name__ == '__main__':
    func(a=1, c=2, b=3)
```

#### Valores padrão

```python
def func(a, b=4, c=42):
    print(a, b, c)

if __name__ == '__main__':
    func(1)
    func(b=5, a=7, c=9)
    func(40, c=9)
```

```python
def func(*args):
    print('Positional:', args)

if __name__ == '__main__':
    lista = [-1, 100, 0, 2, 3, 4]
    func(lista)
    func(*lista)
```

```python
def func(*args):
    print('Positional:', args)

if __name__ == '__main__':
    lista = [-1, 100, 0, 2, 3, 4]
    func(lista)
    func(*lista)
```

Argumentos Posicionais Variáveis

```python
'''
>>> minimum(1, 3, -7, 9)
-7
'''


def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        return mn

if __name__ == '__main__':
    lista = [1, 3, -7, 9]
    print(minimum(*lista))
```

```bash
python -m doctest minimum.py
```

### Argumentos Nomeados

```python
def func(**kwargs):
    print('Keywords:', kwargs)

if __name__ == '__main__':
    func(a=1, b=42)
    dic = {'a': 1, 'b': 42}
    func(**dic)
```

### Tudo misturado

```python
def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    for i in args:
        print(i)
    print('kwargs:', kwargs)
    for k in kwargs:
        print(k, kwargs[k])

if __name__ == '__main__':
    func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
```

```bash
python function_all.py
```


## Lambda

São funções anônimas.

```python
l = lambda x: x * 2
print(l(3))

for i in range(11):
    l = lambda x: x * i
    print(l(3))
```

### Programação funcional e lambda

```python
# Números ímpares gerado com programação funcional e lambda.
nums = range(1,11)
print(list(filter(lambda x: x % 2, nums)))
```


## Módulos

```python
# gen_random_values.py
from datetime import date, datetime, timedelta
from random import randint, random


def gen_number():
    return randint(1, 10)


def gen_date(min_year=1900, max_year=datetime.now().year):
    # gera um date no formato yyyy-mm-dd
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random()


def convert_date(d):
    # converte data no formato mês, dia, ano.
    return d.strftime('%m/%d/%Y')
```

Abra o interpretador Python

```python
>>> from gen_random_values import gen_number, gen_date, convert_date
>>> gen_number()
>>> gen_date()
>>> convert_date(gen_date())
```

## Testes

### Doctest

```python
'''
>>> square(2)
4
>>> square(3)
9
>>> square(4)
16
'''


def square(n):
    return n ** 2

print(square(2))
print(square(3))
print(square(4))
```

```bash
python -m doctest square.py
```


### Teste simples

```python
def test_par():
    assert par(0) == True
    assert par(1) == False

if __name__ == '__main__':
    test_par()
```

```bash
python par.py
```

**Definição:** Seja P o conjunto dos números inteiros pares, então:

P = {x \in \Z | x = 2y, y \in \Z}

Número par é todo número que ao ser dividido por dois deixa resto zero.

P = {x \in \Z | x mod 2 = 0}

Arrumando o código temos:

```python
def par(n):
    if n % 2 == 0:
        return True
    return False


def test_par():
    assert par(0) == True
    assert par(1) == False
    assert par(2) == True
    assert par(4) == True
    assert par(42) == True

if __name__ == '__main__':
    test_par()
```

Existe uma outra solução para este problema:

```python
def par(n):
    return n % 2 == 0
```

### Unittest

[unittest](https://docs.python.org/3/library/unittest.html)

```python
import unittest


class EvenNumberTest(unittest.TestCase):

    def test_par(self):
        self.assertTrue(par(0))
        self.assertFalse(par(1))
        # self.assertTrue(par(2))
        # self.assertTrue(par(4))
        # self.assertTrue(par(42))

if __name__ == '__main__':
    unittest.main()
```

```bash
python par2.py
```

Agora separamos os testes colocando um `assert` por teste.

```python
import unittest


def par(n):
    pass


class EvenNumberTest(unittest.TestCase):

    def test_0(self):
        self.assertEqual(par(0), True)

    def test_1(self):
        self.assertEqual(par(1), False)

    def test_2(self):
        self.assertEqual(par(2), True)

    def test_4(self):
        self.assertEqual(par(4), True)

    def test_42(self):
        self.assertEqual(par(42), True)


if __name__ == '__main__':
    unittest.main()
```

Vendo o resultado de todos os `asserts`.

```bash
python par3.py -v
```

## Try/except

```python
def divide(n, d):
    return n / d

if __name__ == '__main__':
    n = int(input('Digite um numerador:'))
    d = int(input('Digite um denominador:'))
    divide(n, d)
```

Arrumando

```python
def divide(n, d):
    try:
        result = n / d
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('O resultado é:', result)
        return result

if __name__ == '__main__':
    n = int(input('Digite um numerador:'))
    d = int(input('Digite um denominador:'))
    divide(n, d)
```

## Random

```python
from random import randint, random, randrange, choice
colors = ['azul', 'amarelo', 'rosa', 'verde', 'laranja', 'cinza', 'preto', 'branco', 'marrom']
for i in range(1,11): print(i, choice(colors))

randint(10,20)
random()
randrange(0,100,10)
```

## I/O

[Ler/Escrever CSV](https://github.com/rg3915/django-experience/blob/master/io/csv/read_write_csv.md)

### Escrever

```python
import csv

with open('file.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([1, 'Um', 'One'])
    extra_rows = [[2, 'Dois', 'Two'], [3, 'Três', 'Three']]
    csv_writer.writerows(extra_rows)
```

### Ler

Considere o CSV a seguir:

```
id,username,email
1,admin,admin@example.com
2,regis,regis@example.com
3,pedro,pedro@example.com
4,aline,aline@example.com
5,bianca,bianca@example.com
```

```python
import csv

with open('users.csv') as f:
    users_reader = csv.reader(f)
    for row in users_reader:
        print(row)
```

Resultado dos `print` do bloco anterior:

```
['id', 'username', 'email']
['1', 'admin', 'admin@example.com']
['2', 'regis', 'regis@example.com']
['3', 'pedro', 'pedro@example.com']
['4', 'aline', 'aline@example.com']
['5', 'bianca', 'bianca@example.com']
```

Note que cada `row` é uma **lista** de strings. Para retornar um **dicionário** podemos fazer:

```python
import csv

with open('users.csv') as f:
    users_reader = csv.DictReader(f)
    for row in users_reader:
        print(row['id'], row['username'], row['email'])
```

Resultado dos `print` do bloco anterior:

```
1 admin admin@example.com
2 regis regis@example.com
3 pedro pedro@example.com
4 aline aline@example.com
5 bianca bianca@example.com
```

### JSON

todo

## Orientação a Objetos

Abra o interpretador ipython e digite:

### TV

```python
class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisao()
tv_sala = Televisao()
tv_quarto.ligada
tv_quarto.canal
tv_sala.ligada = True
tv_sala.canal = 5
tv_sala.ligada
tv_sala.canal
```

Agora crie um programa chamado `tv.py`.

```python
class Televisao():

    def __init__(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


if __name__ == '__main__':
    tv = Televisao()
    print('Canal inicial:', tv.canal)

    print('Ligada:', tv.ligada)

    tv.ligada = True
    tv.canal = 5

    print('Ligada:', tv.ligada)
    print('Canal inicial:', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal -', tv.canal)
```

### Veículos

```python
class Veiculo(object):

    def __init__(self):
        self.porta = 0
        self.roda = 2
 
class VeiculoMotorizado(Veiculo):

    def __init__(self):
        Veiculo.__init__(self)
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True




if __name__ == '__main__':
    bicicleta = Veiculo()
    print('Bicicleta:')
    print('Porta:' ,bicicleta.porta)
    print('Roda:' ,bicicleta.roda)

    triciclo = Veiculo()
    print('Triciclo:')
    triciclo.roda = 3
    print('Porta:' ,triciclo.porta)
    print('Roda:' ,triciclo.roda)

    moto = VeiculoMotorizado()
    print('Moto:')
    print('Porta:' ,moto.porta)
    print('Roda:' ,moto.roda)
    print('Motor:' ,moto.ligado)

    moto.ligar_motor()
    print('Motor:' ,moto.ligado)

    carro = VeiculoMotorizado()
    carro.porta = 4
    carro.roda = 4
    carro.ligar_motor()
    print('Carro:')
    print('Porta:' ,carro.porta)
    print('Roda:' ,carro.roda)
    print('Motor:' ,carro.ligado)
```

Veículos melhorado

```python
class Veiculo(object):

    def __init__(self, porta=0, roda=2):
        super(Veiculo, self).__init__()
        self.porta = porta
        self.roda = roda


class VeiculoMotorizado(Veiculo):

    def __init__(self, porta=0, roda=2, ligado=False):
        super(VeiculoMotorizado, self).__init__(porta, roda)
        Veiculo.__init__(self)
        self.ligado = ligado

    def ligar_motor(self):
        self.ligado = True


if __name__ == '__main__':
    bicicleta = Veiculo()
    print('Bicicleta:')
    print('Porta:', bicicleta.porta)
    print('Roda:', bicicleta.roda)

    triciclo = Veiculo()
    print('Triciclo:')
    triciclo.roda = 3
    print('Porta:', triciclo.porta)
    print('Roda:', triciclo.roda)

    moto = VeiculoMotorizado()
    print('Moto:')
    print('Porta:', moto.porta)
    print('Roda:', moto.roda)
    print('Motor:', moto.ligado)

    moto.ligar_motor()
    print('Motor:', moto.ligado)

    carro = VeiculoMotorizado()
    carro.porta = 4
    carro.roda = 4
    carro.ligar_motor()
    print('Carro:')
    print('Porta:', carro.porta)
    print('Roda:', carro.roda)
    print('Motor:', carro.ligado)
```

## Conexão com Banco de Dados

todo


## Livros

* Python para Desenvolvedores - Luiz Eduardo Borges - Ed. Novatec
* Pense em Python - Allen B. Downey - Ed. Novatec
* Python Fluente - Luciano Ramalho - Ed. Novatec

## Links

http://tableless.com.br/por-que-python/

https://www.python.org/

[Python 3.5.2 documentation](https://docs.python.org/3/)

[Python Shell online](https://www.python.org/shell/)

[A forma como você programa, faz toda a diferença](http://henriquebastos.net/a-forma-como-voce-programa-faz-toda-a-diferenca/) by [@henriquebastos](http://henriquebastos.net/)


[Por que Python?](http://www.slideshare.net/spjuliano/por-que-python-vamos-conhecer-vamos-aprender) by @julianoatanazio

http://pythonclub.com.br/

[test first](https://github.com/rg3915/test-first)

https://github.com/rg3915/python-experience

[Pense Python](https://panda.ime.usp.br/pensepy/static/pensepy/)

https://realpython.com/

[Reserved Words Python](http://pentangle.net/python/handbook/node52.html)

[pythontutor](http://pythontutor.com/)

[unittest](https://docs.python.org/3/library/unittest.html)

[Ler/Escrever CSV](https://github.com/rg3915/django-experience/blob/master/io/csv/read_write_csv.md)

[CSV](https://docs.python.org/3.5/library/csv.html)

[Melhorando o nosso construtor](https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html#melhorando-o-nosso-construtor)

[Python para Zumbis no YouTube](https://www.youtube.com/watch?v=6La690qlH5w&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc)

[eXcript Curso de Python](https://www.youtube.com/watch?v=j94IGZmwtYI&list=PLesCEcYj003QxPQ4vTXkt22-E11aQvoVj)

[Dojo Gameplay - Happy Numbers](https://www.youtube.com/watch?v=9gokU36gZTY)



