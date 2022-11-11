import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content  = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("title","content","cat")  #__all__ если хотим все поля

# def encode():
#     model = WomenModel('Angel','Content: Angel')
#     #пропускаем объект model через сериализатор
#     model_sr = WomenSerializer(model) #представляет объект сериализации а не json строку
#     print(model_sr.data,type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data) #преобразует объект сериализации в байтовую json строку
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angel","content":"Content: Angel"}') #имитация поступление запроса от клиента
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data) #декодирование
#     serializer.is_valid() #проверяет корректность принятых данных
#     print(serializer.validated_data)
