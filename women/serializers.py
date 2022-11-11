import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content  = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True) #read_only чтобы не было ошибки обязательности ввода
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data) #передаём распакованный словарь validated_data

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance

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
