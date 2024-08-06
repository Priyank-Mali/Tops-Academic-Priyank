from rest_framework.decorators import api_view
from .models import globalNote
from .serializers import GlobalNoteSeralizer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def globaleNotesList(request):
    try:
        if request.method=="GET":
            queryset = globalNote.objects.all()
            serializer = GlobalNoteSeralizer(queryset,many=True)
            data = {
                "data" : serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        elif request.method=="POST":
            jsondata = request.data
            serializer = GlobalNoteSeralizer(data=jsondata)
            if serializer.is_valid():
                serializer.save()
                data = {
                    "data" : serializer.data
                }
                return Response(data,status=status.HTTP_201_CREATED)
            else:
                data = {
                    "error" : serializer.errors
                }
                return Response(data,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        data = {
            "error" : str(e)
        }
        return Response(data,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def globaleNotesDetails(request,note_id):
    try:
        queryset = globalNote.objects.get(id=note_id)
    except globalNote.DoesNotExist:
        data = {
            "error" : "Note Not Found"
        }
        return Response(data,status.HTTP_204_NO_CONTENT)
    if request.method=="GET":
        serializer = GlobalNoteSeralizer(queryset)
        data = {
            "data" : serializer.data
        }
        return Response(data,status.HTTP_200_OK)
    elif request.method=="PUT":
        jsondata = request.data
        serializer = GlobalNoteSeralizer(instance=queryset,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            data = {
                "data" : serializer.data,
                "message" : "Student Comment Change Successfully (All Data)"
            }
            return Response(data,status.HTTP_202_ACCEPTED)
        else:
            data = {
                "error" : serializer.errors
            }
            return Response(data,status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="PATCH":
        jsondata = request.data
        serializer = GlobalNoteSeralizer(instance=queryset,data=jsondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "data" : serializer.data,
                "message" : "Student Comment Change Successfully (Partially Change)"
            }
            return Response(data,status.HTTP_202_ACCEPTED)
        else:
            data = {
                "error" : serializer.errors
            }
            return Response(data,status.HTTP_400_BAD_REQUEST)
    else:
        queryset.delete()
        data = {
            "message" : "Comment Deleted Successfully"
        }
        return Response(data,status.HTTP_204_NO_CONTENT)
    
@api_view()
def studentGlobaleNote(request,student_id):
    queryset = globalNote.objects.filter(student_id=student_id)
    if request.method=="GET":
        if queryset:
            serializer = GlobalNoteSeralizer(queryset,many=True)
            data = {
                "data" : serializer.data
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = {
                "error" : "Note Not Found"
            }
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    else:
        data = {
            "error" : "Something Went Wrong"
        }
        return Response(data,status=status.HTTP_400_BAD_REQUEST)
            