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
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer = SnippetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def snippet_details(request,pk):

    try:
        snippetQueryset = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serializer = SnippetsSerializer(snippetQueryset)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    elif request.method=='PUT':
        serializer = SnippetsSerializer(snippetQueryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer':serializer,'profile':snippetQueryset})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        snippetQueryset.delete()
        return Response(status=status.HTTP_410_GONE)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

