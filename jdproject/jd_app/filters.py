from django_filters import FilterSet
from .models import Product

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,

class ProductFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
       model = Product
       # В fields мы описываем по каким полям модели будет производиться фильтрация.
       fields = {
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',
               'gt',
           ],
       }
