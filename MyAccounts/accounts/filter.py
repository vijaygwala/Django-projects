import django_filters
from django_filters import DateFilter, CharFilter
from accounts.models import *
class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="From", lookup_expr='gte')
	end_date = DateFilter(field_name="To", lookup_expr='lte')
	


	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']