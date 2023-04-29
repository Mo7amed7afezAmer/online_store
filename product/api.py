from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import BasePermission
from .serializers import ProductSerializer
from django.http import JsonResponse
from chartjs.views.lines import BaseLineChartView
from .models import Product
from cart.models import CheckOut
import calendar
from datetime import datetime



class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
    

class ProductCrreateApi(CreateAPIView):
    serializer_class   = ProductSerializer
    permission_classes = [IsStaff]


class ProductDeleteApi(DestroyAPIView):
    serializer_class   = ProductSerializer
    permission_classes = [IsStaff]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Product.objects.all()
        return Product.objects.filter(created_by = user)
        






class LineChartJSONView(BaseLineChartView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return super().get(self, request, *args, **kwargs)
        return JsonResponse({'permission':'denied'} ,status=403)

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        now = datetime.now().month # month number from 1 - 12
        months = calendar.month_name[now+1:13] + calendar.month_name[1:now+1] # arranged list of months
        return months[6:]

    def get_providers(self):
        """Return names of datasets."""
        return ["sales", "revenue"]

    def get_data(self):
        """Return 2 datasets to plot."""

        user = self.request.user
        qs = CheckOut.objects.filter(orders__product__created_by = user)
        orders = []
        for i in qs:
            for j in i.orders.all():
                orders.append(j)
        quant = sum([i.quantity for i in orders])
        price = sum([i.get_price for i in orders])
        print('qs :')
        print(qs)
        print('orders :')
        print(orders)
        print('quant :')
        print(quant)
        print('price :')
        print(price)

        return [[35, 44, 25, 11, 44, 16, 35],
                [17, 21, 12, 3, 22, 13, 12]]

