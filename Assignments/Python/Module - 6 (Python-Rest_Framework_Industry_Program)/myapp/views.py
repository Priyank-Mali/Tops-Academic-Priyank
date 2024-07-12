from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def book_list(request):
    if request.method=='GET':
        bookqueryset = Book.objects.all()
        serializer = BookSerializer(bookqueryset,many=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "payload" : serializer.data
        })
    
    elif request.method=='POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "payload" : serializer.data,
                "message" : "Data Created Successfully"
            })
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "error" : serializer.errors
        })


@api_view(['GET','PUT','PATCH','DELETE'])
def book_details(request,pk):
    try:
        bookqueryset = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "mesage" : "Data not Exists"
        })
    
    if request.method=='GET':
        serializer = BookSerializer(bookqueryset)
        return Response({
            "status" : status.HTTP_200_OK,
            "payload" : serializer.data
        })
    
    #  The PUT method is used to update a resource completely. It requires the entire object to be updated.
    elif request.method=='PUT':
        serializer = BookSerializer(bookqueryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "payload" : serializer.data,
                "message" : "Data Updated Successfully"
            })
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "error" : serializer.errors
        })
    
    # The PATCH method is used to update a resource partially. It allows you to send only the fields that need to be updated.
    elif request.method=='PATCH':
        serializer = BookSerializer(bookqueryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "payload" : serializer.data,
                "message" : "Data updated partially successfully"
            })
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "error" : serializer.errors
        })
    
    elif request.method=='DELETE':
        bookqueryset.delete()
        return Response({
            "status" : status.HTTP_410_GONE,
            "message" : "Data deleted Successfully"
        })