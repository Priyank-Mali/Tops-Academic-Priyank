from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SnippetsSerializer
from .models import Snippets
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def snippet_list(request):
    if request.method=='GET':
        snippetsQueryset = Snippets.objects.all()
        serializer = SnippetsSerializer(snippetsQueryset,many=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "payload" : serializer.data
        })
    
    elif request.method=='POST':
        serializer = SnippetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status" : status.HTTP_201_CREATED,
                "payload" : serializer.data,
                "message" : "Data will created successfully"
            })
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "error" : serializer.errors
        })
    

@api_view(['GET','PUT','DELETE','PATCH'])
def snippet_details(request,id):
    try:
        snippetQueryset = Snippets.objects.get(id=id)
    
        if request.method=='GET':
            serializer = SnippetsSerializer(snippetQueryset)
            return Response({
                "status" : status.HTTP_200_OK,
                "payload" : serializer.data
            })

        elif request.method=='PUT':
            serializer = SnippetsSerializer(snippetQueryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "payload" : serializer.data,
                    "message" : "Data Updated Successfully"
                })
            
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "error" : serializer.errors
            })
        
        elif request.method=='PATCH':
            serializer = SnippetsSerializer(snippetQueryset,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : status.HTTP_200_OK,
                    'payload': serializer.data,
                    'message': "Data Updated Successfully"
                })
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST,
                "error" : serializer.errors
            })
        
        elif request.method=='DELETE':
            snippetQueryset.delete()
            return Response({
                "status" : status.HTTP_204_NO_CONTENT,
                "message" : "Data Deleted Successfully"
            })
        else:
            return Response({
                "status" : status.HTTP_400_BAD_REQUEST
            })
        
    except Snippets.DoesNotExist:
        return Response({
            "status" : status.HTTP_400_BAD_REQUEST,
            "error" : "Data not Exists"
        })
