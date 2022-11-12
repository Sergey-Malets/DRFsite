from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdate (generics.UpdateAPIView):
    queryset = Women.objects.all() # мы как будто выбираем все записи, но UpdateAPIView выбирет только одну конкретную
    serializer_class = WomenSerializer

class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self,request):
#         w = Women.objects.all()
#         return Response({'posts':WomenSerializer(w, many=True).data}) #many говорит о том что сериализатор должен обрабатывать список записей
#
#     def post(self,request):
#         serializer = WomenSerializer(data=request.data) #создаём сериал. на основе данных кот поступили с ПОСТ запросом
#         serializer.is_valid(raise_exception=True) #делаем проверку корректность принятых данных
#         serializer.save() #автоматически вызывает метод create из сериализ.
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() #изза того что создаётся объект с 2мя парам. data и instance, save вызывает метод update
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         instance.delete()
#
#         return Response({"post": "delete post "+ str(pk)})
