from django.http import HttpResponse, JsonResponse
from django.db.models.expressions import RawSQL
from rest_framework import status
from django.db import connections
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from master.models import *
from master.serializer import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from .renderers import CustomRenderer
from rest_framework.decorators import action

class AreaViewSets(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(id=kwargs['pk']).first()
        print(instance)
        if not instance:
            return Response({'message': 'Object not found'}, status=404)
        serializer = self.get_serializer(instance)
        # Implement your custom logic here
        response_data = {
            'status': 'success',
            'message': 'Area update successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED,}
        return Response(response_data)

    def update(self, request, pk=None):
        area = self.get_object()

        # Update the country object based on the data in the request
        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'status': 'success',
            'message': 'Area update successfully',
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
            'message': 'Area added successfully',
            'data': serializer.data,
            'status_code':status.HTTP_201_CREATED

        }
        return Response(response_data, status=status.HTTP_201_CREATED)


from rest_framework import routers
from rest_framework.decorators import action

class AreaGetData(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    # queryset = Area.objects.raw('''
    #         SELECT a.id,a.areacode,a.areaname, b.countryname,c.statename
    #         FROM master_area a
    #         INNER JOIN master_country b ON a.countrycode_id = b.id
    #         INNER JOIN master_state c ON a.statecode = c.id''')
    serializer_class = AreaSerializer

    # @action(detail=True, methods=['get'])

    # # def retrieve(self, request, pk=None):
    # #     result = Area.objects.select_related('model_b').select_related('model_c').values('field1', 'field2', 'model_b__field3', 'model_c__field4')
    # #     queryset = self.queryset.filter(statecode=pk)
    # #     serializer = self.serializer_class(queryset, many=True)
    # #     response_data={
    # #         'data': serializer.data,
    # #         'status_code':status.HTTP_200_OK
    # #     }
    # #     return Response(response_data,status=status.HTTP_200_OK)

    # def get_data(self, request, pk=None):
    #     connection = connections['default']
    #     area_id = pk
    #     query = """
    #         SELECT master_area.areaname, master_country.countryname,master_state.statename
    #         FROM master_area a
    #         INNER JOIN master_country b ON a.countrycode = b.id
    #         INNER JOIN master_state c ON a.statecode = c.id
    #         WHERE master_area.id = %s
    #     """
    #     # query = """
    #     #     SELECT master_area.areaname, master_country.countryname, master_state.statename,master_state.
    #     #     FROM master_area
    #     #     INNER JOIN master_country ON master_area.countrycode = master_country.id
    #     #     INNER JOIN master_state ON master_country.id = master_state.countrycode
    #     #     WHERE master_area.id = %s
    #     # """
    #     with connection.cursor() as cursor:
    #         cursor.execute(query, [area_id])
    #         rows = cursor.fetchall()
    #     data = [[row[0], row[1], row[2]] for row in rows]
    #     return Response({'data': data})





# class AreaGetData(viewsets.ModelViewSet):
#     queryset = Area.objects.all()
#     serializer_class = AreaSerializer
#     print("serializer_class----------------------",serializer_class)
#     def retrieve(self, request, pk=None):
#         connection = connections['default']
#         areacode = kwargs.get('pk')
#         print("areacode",areacode)
#         query="""
#                 SELECT master_area.areaname,master_country.countryname,master_state.statename
#                 FROM master_area 
#                 INNER JOIN master_country
#                 ON master_area.countrycode = master_country.id
#                 INNER JOIN master_state
#                 ON master_area.statecode = master_state.id
#             """
#         #data = Area.objects.raw(query)
#         #serializer = AreaSerializer(data, many=True)
#         with connection.cursor() as cursor:
#             cursor.execute(query)
#             rows = cursor.fetchall()
#         data = []
#         data = [[row[0], row[1], row[2]] for row in rows]
#         # for row in rows:
#         #     data.append([row[0], row[1], row[2]])
#         # serializer = AreaSerializer(data, many=True)
#         # serializer.is_valid()
#         #print("data",serializer)
#         return Response({'data': data})


# use where condiion example
# class AreaGetData(viewsets.ModelViewSet):
#     queryset = Area.objects.all()
#     serializer_class = AreaSerializer
#     print("serializer_class----------------------",serializer_class)
#     def retrieve(self, request, *args, **kwargs):
#         connection = connections['default']
#         areacode = kwargs.get('pk')
#         print("areacode",areacode)
#         query="""
#                 SELECT master_area.areaname,master_country.countryname,master_state.statename
#                 FROM master_area 
#                 INNER JOIN master_country
#                 ON master_area.countrycode = master_country.id
#                 INNER JOIN master_state
#                 ON master_area.statecode = master_state.id
#                 WHERE master_area.id = %s
#             """
#         with connection.cursor() as cursor:
#             cursor.execute(query,[areacode])
#             data = cursor.fetchall()
#         data_dict = list(data)
#         #print("data",data)
#         return Response({'data': data_dict})