from django.http import HttpResponse, JsonResponse
from django.db.models.expressions import RawSQL
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from master.models import State
from master.serializer import StateSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from .renderers import CustomRenderer
from rest_framework.decorators import action

class StateViewSets(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(id=kwargs['pk']).first()
        print(instance)
        if not instance:
            return Response({'message': 'Object not found'}, status=404)
        serializer = self.get_serializer(instance)
        # Implement your custom logic here
        response_data = {
            'status': 'success',
            'message': 'State update successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED,}
        return Response(response_data)

    def update(self, request, pk=None):
        state = self.get_object()

        # Update the State object based on the data in the request
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'status': 'success',
            'message': 'State update successfully',
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
            'message': 'State added successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED

        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class StateDataByCountry(viewsets.ViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def retrieve(self, request, pk=None):
        queryset = self.queryset.filter(countrycode=pk)
        serializer = self.serializer_class(queryset, many=True)
        response_data={
            'data': serializer.data,
            'status_code':status.HTTP_200_OK
        }
        return Response(response_data,status=status.HTTP_200_OK)