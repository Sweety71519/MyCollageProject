from django.http import HttpResponse, JsonResponse
from django.db.models.expressions import RawSQL
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from master.models import Employee
from master.serializer import EmployeeSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from .renderers import CustomRenderer
from rest_framework.decorators import action

class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(id=kwargs['pk']).first()
        print(instance)
        if not instance:
            return Response({'message': 'Object not found'}, status=404)
        serializer = self.get_serializer(instance)
        # Implement your custom logic here
        response_data = {
            'status': 'success',
            'message': 'Employee update successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED,}
        return Response(response_data)

    def update(self, request, pk=None):
        Employee = self.get_object()

        # Update the Employee object based on the data in the request
        serializer = EmployeeSerializer(Employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'status': 'success',
            'message': 'Employee update successfully',
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
            'message': 'Employee added successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED

        }
        return Response(response_data, status=status.HTTP_201_CREATED)


# class EmployeeDataByCountry(viewsets.ViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def retrieve(self, request, pk=None):
#         queryset = self.queryset.filter(countrycode=pk)
#         serializer = self.serializer_class(queryset, many=True)
#         response_data={
#             'data': serializer.data,
#             'status_code':status.HTTP_200_OK
#         }
#         return Response(response_data,status=status.HTTP_200_OK)