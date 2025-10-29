from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
import requests

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer

    # Example third-party API integration:
    # GET /api/items/fetch-external/
    @action(detail=False, methods=['get'])
    def fetch_external(self, request):
        """Fetch sample posts from JSONPlaceholder and return them."""
        try:
            r = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=5', timeout=10)
            r.raise_for_status()
            return Response(r.json())
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_502_BAD_GATEWAY)

    # Simple reporting endpoint: totals aggregated
    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_items = Item.objects.count()
        total_quantity = Item.objects.aggregate(total=models.Sum('quantity'))['total'] or 0
        total_value = Item.objects.aggregate(total=models.Sum(models.F('quantity') * models.F('price')))['total'] or 0
        return Response({
            'total_items': total_items,
            'total_quantity': total_quantity,
            'total_value': float(total_value),
        })
