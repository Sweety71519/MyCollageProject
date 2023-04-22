from rest_framework import serializers
from .models import * #Product,Snippet,Country,Zone,State,Areamaster
from rest_framework import status
from django.contrib.auth.hashers import make_password

# class TourplanhdSerializer(serializers.ModelSerializer):
#     class Meta:
#         models=Product
#         fields ='__all__'

from rest_framework import serializers
from master.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields ='__all__' #['id', 'title', 'code', 'linenos', 'language', 'style']



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields ='__all__' 
    



class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields ='__all__' 


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields ='__all__' 

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields ='__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields ='__all__' 


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields ='__all__'

class MenumasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menumaster
        fields ='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields ='__all__'

class TehsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tehsi
        fields ='__all__'


class ModelmasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelmaster
        fields ='__all__'


class UserAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthorization
        fields ='__all__'


class UserinformationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserinformationSerializer, self).create(validated_data)

    class Meta:
        model = Userinformation
        fields ='__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'





