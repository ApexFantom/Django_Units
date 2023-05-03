from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Unitsdb, CustomUser

# class UnitModel:
#     def __init__(self, name, fr, type, short_des, des, img, img_bck):
#         self.name = name
#         self.fr = fr
#         self.type = type
#         self.short_des = short_des
#         self.des = des
#         self.img = img
#         self.img_bck = img_bck
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unitsdb
        #fields = ('name','fr','type','short_des','des','data_create','data_update','img','img_bck')
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}