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
# from rest_framework_simplejwt.authentication import JWTAuthentication


class UserinformationViewSets(viewsets.ModelViewSet):
    queryset = Userinformation.objects.all()
    serializer_class = UserinformationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(id=kwargs['pk']).first()
        print(instance)
        if not instance:
            return Response({'message': 'Object not found'}, status=404)
        serializer = self.get_serializer(instance)
        # Implement your custom logic here
        response_data = {
            'status': 'success',
            'message': 'Userinformation update successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED,}
        return Response(response_data)

    def update(self, request, pk=None):
        Userinformation = self.get_object()

        # Update the Userinformation object based on the data in the request
        serializer = UserinformationSerializer(Userinformation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'status': 'success',
            'message': 'Userinformation update successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED,}
            return  Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'status': 'success',
            'message': 'Userinformation added successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED

        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']

        user=Userinformation.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("user not faound.")
        if not user.check_password(password):
            raise AuthenticationFailed("Inccorect Password")
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.datetime(minutes=60),
            'iat':datetime.datetime.utcnow()

        }

        token=jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        response=Response()
        response.set_cookie=(key:='jwt',value:=token, httponly:=True)
        response.data={
            'jwt':token
        }
        return response
    

    def get_extra_actions(self):
        extra_actions = super().get_extra_actions()
        extra_actions.append({
            'url_path': 'login',
            'method': 'post',
            'func': self.login_action,
            'name': 'login'
        })
        return extra_actions

