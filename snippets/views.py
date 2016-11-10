from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer, OrderStatusSerializer, WorkEffortsSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from .soapclient import SoapClient
from rest_framework.views import APIView

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class OrderStatusView(APIView):
    def get(self, request, orderId):
        soapClient = SoapClient()
        orderStatus = soapClient.getOrderStatus(orderId)
        serializer = OrderStatusSerializer(orderStatus)
        return Response(serializer.data)

class WorkEffortsView(APIView):
    def get(self, request):
        soapClient = SoapClient()
        workEfforts = soapClient.getWorkEfforts()
        serializer = WorkEffortsSerializer(workEfforts, many=True)

        return Response(serializer.data)

