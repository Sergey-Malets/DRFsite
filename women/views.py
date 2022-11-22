from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer



class WomenAPIListPagination(PageNumberPagination):
    page_size = 3  #дефолтное кол-во записей на странице
    page_size_query_param = 'page_size'  #возможность пользователю чрез get запрос выбрать сколько отобразится на странице
    max_page_size = 10000  #это максимально допустимое значение page_size

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination

class WomenAPIUpdate (generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all() # мы как будто выбираем все записи, но UpdateAPIView выбирет только одну конкретную
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )  # авторизация только по токенам

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )

