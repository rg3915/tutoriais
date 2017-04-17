from myproject.core.models import Distributor

DISTRIBUTOR_LIST = ['20th Century Fox',
                    'Warner Bros.',
                    'New Line Cinema',
                    'Sony Pictures',
                    'Universal Studios',
                    'DreamWorks',
                    'Columbia',
                    'Lionsgate',
                    'Summit Entertainment']

obj = [Distributor(distributor=val) for val in DISTRIBUTOR_LIST]
Distributor.objects.bulk_create(obj)
