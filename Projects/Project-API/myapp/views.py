from rest_framework.decorators import api_view
from .models import globalNote
from .serializers import GlobalNoteSeralizer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def studentList(request):
    try:
        if request.method=="GET":
            queryset = globalNote.objects.all()
            serializer = GlobalNoteSeralizer(queryset,many=True)
            return Response({
                "status_code" : status.HTTP_200_OK,
                "payload" : serializer.data
            })
        elif request.method=="POST":
            jsondata = request.data
            serializer = GlobalNoteSeralizer(data=jsondata)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status_code" : status.HTTP_201_CREATED,
                    "payload" : serializer.data
                })
            else:
                return Response({
                    "status_code" : status.HTTP_400_BAD_REQUEST,
                    "error" : serializer.errors
                })
    except Exception as e:
        return Response({
            "status_code" : status.HTTP_400_BAD_REQUEST,
            "error" : str(e)
        })

@api_view(['GET','PUT','PATCH','DELETE'])
def studentDetails(request,student_id):
    try:
        queryset = globalNote.objects.get(student_id = student_id)
    except globalNote.DoesNotExist:
        return Response({
            "status_code" : status.HTTP_204_NO_CONTENT,
            "message" : "Student Not Exists"
        })
    if request.method=="GET":
        serializer = GlobalNoteSeralizer(instance=queryset)
        return Response({
            "status_code" : status.HTTP_200_OK,
            "payload" : serializer.data
        })
    elif request.method=="PUT":
        jsondata = request.data
        serializer = GlobalNoteSeralizer(instance=queryset,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code" : status.HTTP_202_ACCEPTED,
                "payload" : serializer.data,
                "message" : "Student Comment Change Successfully (All)"
            })
        else:
            return Response({
                "status_code" : status.HTTP_400_BAD_REQUEST,
                "error" : serializer.errors
            })
        
    elif request.method=="PATCH":
        jsondata = request.data
        serializer = GlobalNoteSeralizer(instance=queryset,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status_code" : status.HTTP_202_ACCEPTED,
                "payload" : serializer.data,
                "message" : "Student Comment Change Successfully (Partially)"
            })
        else:
            return Response({
                "status_code" : status.HTTP_400_BAD_REQUEST,
                "error" : serializer.errors
            })
    else:
        queryset.delete()
        return Response({
            "status_code" : status.HTTP_410_GONE,
            "message" : "Comment Deleted Successfully"
        })
