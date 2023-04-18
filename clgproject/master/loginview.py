from django.http import HttpResponse, JsonResponse
from django.db.models.expressions import RawSQL
from rest_framework import status
import json
import jwt,datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from master.models import Userinformation
from master.serializer import UserinformationSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from .renderers import CustomRenderer
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication




class LoginView(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']

        user=Userinformation.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("user not faound.")
        if not user.check_password(password):
            raise AuthenticationFailed("Inccorect Password")
        return response({"massage":"success"})
        
    #     payload={
    #         'id':user.id,
    #         'exp':datetime.datetime.utcnow() + datetime.datetime(minutes=60),
    #         'iat':datetime.datetime.utcnow()

    #     }

    #     token=jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
    #     response=Response()
    #     response.set_cookie=(key:='jwt',value:=token, httponly:=True)
    #     response.data={
    #         'jwt':token
    #     }
    #     return response
    

    # def get_extra_actions(self):
    #     extra_actions = super().get_extra_actions()
    #     extra_actions.append({
    #         'url_path': 'login',
    #         'method': 'post',
    #         'func': self.login_action,
    #         'name': 'login'
    #     })
    #     return extra_actions

