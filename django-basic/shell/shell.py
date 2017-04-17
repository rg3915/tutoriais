from myproject.core.models import Distributor, Category, Movie
import datetime

# Podemos criar uma instância do objeto e depois salvar.
obj = Distributor(distributor='Paramount Pictures')
obj.save()

# Veja um exemplo de como criar um Distributor diretamente.
Distributor.objects.create(distributor='Universal Pictures')
Distributor.objects.create(distributor='Walt Disney Pictures')

CATEGORY_LIST = ['ação', 'animação',
                 'aventura', 'comedia', 'guerra', 'suspense']
# Usando um List Comprehension podemos definir todos os objetos a serem
# inseridos no Django
obj = [Category(category=val) for val in CATEGORY_LIST]
# O comando bulk_create é muito rápido!
Category.objects.bulk_create(obj)

# O comando get "pega" um objeto
category = Category.objects.get(category='ação')
distributor = Distributor.objects.get(distributor__istartswith='Warner')
Movie.objects.create(
    movie='O Exterminador do Futuro',
    category=category,  # para ser usado aqui
    distributor=distributor,
    raised=1.756,
    release=datetime.date(1984, 10, 26)
)

category = Category.objects.get(category='aventura')
distributor = Distributor.objects.get(distributor='Lionsgate')
Movie.objects.create(
    movie='Jogos Vorazes',
    category=category,
    distributor=distributor,
    raised=2.308,
    release=datetime.date(2012, 3, 23)
)

q = Movie.objects.all()  # listando todos os filmes
q.count()
q
q.values()  # dicionario
q.values_list()  # lista

for i in q.values():
    print(i)

# Experimente
for i in q:
    i.movie, i.category, i.raised

dir(q)  # veja todas as opções do objeto.

# Exemplos de filtro
Movie.objects.filter(category='ação')  # retorna erro
Movie.objects.filter(category__category='ação')
Movie.objects.filter(distributor__distributor__icontains='gate')

# Exemplo de update
Movie.objects.filter(movie__icontains='Exterminador').update(
    movie='O Exterminador do Futuro: Gênesis', release=datetime.date(2015, 7, 1))

# Exemplo de delete
Movie.objects.filter(id=1).delete()
# Customer.objects.all().delete() # perigoso
t = Movie.objects.get(movie='Titanic')
t
t.id
Movie.objects.filter(id=t.id).delete()
Movie.objects.filter(movie='Titanic')
Movie.objects.filter(movie='Titanic').count()

Movie.objects.filter(release__year=2012).count()
# Movie.objects.filter(release__year__gte=2000).count()  # filmes > 2000

# Filme de maior bilheteria
from django.db.models import Max
q = Movie.objects.all().aggregate(Max('raised'))
q
Movie.objects.filter(raised=q['raised__max'])
