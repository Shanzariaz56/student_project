import django_filters
from .models import *

class studentFilter(django_filters.FilterSet):
    class Meta:
        name = django_filters.CharFilter("name",lookup_expr='icontain') 
        model = Student
        fields="__all__"
