from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr="year")  # эгер year DateField болсо .year пайдалануу керек
    year_after = filters.DateFilter(field_name="year", lookup_expr="gte")
    year_before = filters.DateFilter(field_name="year", lookup_expr="lte")
    director = filters.CharFilter(field_name="director__name", lookup_expr="icontains")
    country = filters.CharFilter(field_name="country__country_name", lookup_expr="icontains")
    genre = filters.CharFilter(field_name="genre__name", lookup_expr="icontains")

    class Meta:
        model = Movie
        fields = ["year", "director", "country", "genre"]
