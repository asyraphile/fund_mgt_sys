from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .serializers import FundSerializer
from .models import Fund
"""
TASK 2: REST API Development Using Python and a web framework of your choice (e.g., Flask or Django), create a RESTful API to
manage investment funds.
"""

@api_view(['GET'])
def get_all(request):
    funds = Fund.objects.all()
    serializer = FundSerializer(funds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_fund(request, id):
    try:
        fund = Fund.objects.get(id=id)
        serializer = FundSerializer(fund, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Fund.DoesNotExist:
        return Response({'message': f'Fund with id {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_fund(request):
    try:
        serializer = FundSerializer(data=request.data)
        # validate serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Fund created successfully',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)
    except ValidationError as ve:
        return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['PUT'])
def update_performance_by_id(request, id):
    try:
        fund = Fund.objects.get(id=id)
        # filter for performance in request data
        if 'performance' not in request.data:
            raise Exception('Incorrect parameter given.')
        # raise exception if there are more than one key in request data
        elif len(list(request.data.keys())) > 1:
            raise Exception('Only performance parameter will be accepted.')
        else:
            serializer = FundSerializer(fund, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except ValidationError as ve:
        return Response({'message': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
    except Fund.DoesNotExist:
        return Response({'message': f'Fund with id {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['DELETE'])
def delete_fund_by_id(request, id):
    try:
        fund = Fund.objects.get(id=id)
        fund.delete()
        response = {
            'message': 'Fund deleted successfully',
        }
        return Response(response, status=status.HTTP_200_OK)
    except Fund.DoesNotExist:
        return Response({'message': f'Fund with id {id} not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)