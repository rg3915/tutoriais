from myproject.core.models import Category

CATEGORY_LIST = ['ação', 'animação',
                 'aventura', 'comedia', 'guerra', 'suspense']
obj = [Category(category=val) for val in CATEGORY_LIST]
Category.objects.bulk_create(obj)
