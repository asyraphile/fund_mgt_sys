from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import FundSerializer
from .models import Fund
"""
TASK 2: REST API Development Using Python and a web framework of your choice (e.g., Flask or Django), create a RESTful API to
manage investment funds.
"""

class FundViewset(viewsets.ViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    # Endpoint to retrieve a list of all funds 
    def list(self):
        queryset = self.queryset
        try:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            response = {'message': f'Fund retrieval failed due to {e}'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    # Endpoint to create a new fund 
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response = {
                'message': 'Fund created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {'message': f'Fund creation failed due to {e}'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
            
    # Endpoint to retrieve details of a specific fund using its ID     
    def retrieve(self, request, pk=None):
        try:
            queryset = self.queryset.filter(pk=pk).first()
            if len(queryset) < 1:
                raise ValidationError(f"Fund with id {str(pk)} not found.")
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except ValidationError as ve:
            return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {'message': f'Fund retrieval failed due to {e}'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    # Endpoint to update the performance of a fund using its ID     
    def update(self, request, id):
        try:
            if 'fund_performance' not in request.data:
                raise ValidationError("The 'fund_performance' field is required.")
            instance = self.queryset.filter(pk=id).first()
            if len(instance) < 1:
                raise ValidationError(f"Fund with id {str(id)} not found.")
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {'message': f'Fund update failed due to {e}'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    # Endpoint to delete a fund using its ID    
    def destroy(self, request, pk=None):
        queryset = self.queryset
        try:
            queryset.filter(pk=pk).delete()
            response = {'message': 'Fund delete successfully'}
            return Response(response)
        except Exception as e:
            response = {'message': 'Fund deletion failed', 'data': f'{e}'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
