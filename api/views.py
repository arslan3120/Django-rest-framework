from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def EmployeeListView(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees , many=True)
        
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        jsondata = JSONParser().parse(request)
        print(jsondata) 
        serializer = EmployeeSerializer(data = jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False) 
        
        


def UserListView(request):
    users = User.objects.all()
    serializers = UserSerializer(users , many=True)
    
    return JsonResponse(serializers.data, safe=False)