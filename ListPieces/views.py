from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ListPieces.models import LIST_PIECES
from ListPieces.serializers import LISTSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def ListPiecesApi(request,id=0):
    if request.method=='GET':
        listpie = LIST_PIECES.objects.all()
        list_serializer = LISTSerializer(listpie, many=True)
        return JsonResponse(list_serializer.data, safe=False)

    elif request.method=='POST':
        list_data=JSONParser().parse(request)
        list_serializer = LISTSerializer(data=list_data)
        if list_serializer.is_valid():
            list_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PATCH':
        list_data = JSONParser().parse(request)
        listpieces=LIST_PIECES.objects.get(id_piéce=list_data['id_piéce'])
        list_serializer=LISTSerializer(listpieces,data=list_data)
        if list_serializer.is_valid():
            list_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        listpieces=LIST_PIECES.objects.get(id_piéce=id)
        listpieces.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

def list_detail(request, pk):
    tutorial = LIST_PIECES.objects.get(pk=pk)
 
    if request.method == 'GET': 
        tutorial_serializer = LISTSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 

@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)        