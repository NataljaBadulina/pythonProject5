from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, CharFilter
from .models import Product
from django.forms import DateInput


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,


class ProductFilter(FilterSet):
    product_name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Product name',
    )

    class Meta:
        model = Product
        fields = {
            'quantity': ['gt'],
            'price': ['lt', 'gt', ],
        }
