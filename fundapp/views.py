from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
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
            response = {
                'message': f'Fund retrieval failed due to {e}'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
