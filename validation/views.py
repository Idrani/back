from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from validation.models import VAL
from validation.serializers import ValidationSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def ValApi(request,id=0):   

    if request.method=='GET':
        valof = VAL.objects.all()
        val_serializer = ValidationSerializer(valof, many=True)
        return JsonResponse(val_serializer.data, safe=False)

    elif request.method=='POST':
        val_data=JSONParser().parse(request)
        val_serializer = ValidationSerializer(data=val_data)
        if val_serializer.is_valid():
            val_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        val_data = JSONParser().parse(request)
        valof=VAL.objects.get(NumOF=val_data['NumOF'])
        val_serializer=ValidationSerializer(valof,data=val_data)
        if val_serializer.is_valid():
            val_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='PATCH':
        val_data = JSONParser().parse(request)
        valof=VAL.objects.get(NumOF=val_data['NumOF'])
        val_serializer=ValidationSerializer(valof,data=val_data)
        if val_serializer.is_valid():
            val_serializer.save()
            return JsonResponse("PATCHED Successfully!!", safe=False)
        return JsonResponse("Failed to PATCH.", safe=False)

    elif request.method=='DELETE':
        faborder=VAL.objects.get(NumOF=id)
        faborder.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
