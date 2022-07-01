from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .serializer import *
from .models import Todo
#class based View class
from rest_framework.views import APIView

from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
#End

@api_view(["GET","POST","PATCH"])
def home(request):
    if request.method =="GET":
        return Response({'message':"DjangoRest Get Api working !","status":200})
    elif request.method =="POST":
        return Response({'message':"DjangoRest POST Api working !","status":200})
    elif request.method =="PATCH":
        return Response({'message':"DjangoRest PATCH Api working !","status":200})
    else:
        return Response({'message':"Invalid Method not working !","status":400})



#Function Based View For Rest API
@api_view(["GET"])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = ToDoSerializer(todo_objs,many=True)#more than one object therefore retun many =True
    return Response({"status":True,"message":"Fetched data","data":serializer.data})

@api_view(["POST"])
def post_todo(request):
    try:
        data = request.data
        seriallzer = ToDoSerializer(data=data)
        if seriallzer.is_valid():
            # print(seriallzer.data)
            seriallzer.save()
            return Response({ "status": True,'message':"Success Data !",'data':seriallzer.data})
        return Response({ "status": False,'message': "Invalid Data !",'data':seriallzer.errors})
    except Exception as e:
        print(e)
        return Response({'message': "Something went Wrong!", "status": False})

@api_view(["PATCH"])
def patch_todo(request):
    import pdb
    # pdb.set_trace()
    try:
        data = request.data
        if not data.get('uid'):
            return Response({"status": False, 'message': "Uid is required !", 'data': {}})
        obj = Todo.objects.get(uid = data.get('uid'))
        # print('2222222222'+obj)
        serializer = ToDoSerializer(obj , data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, 'message': "PATCH Updated !", 'data': serializer.data})

        return Response({'message': "Invalid data !", "status": False,'data':serializer.errors})
    except Exception as e:
        print(e)
        return Response({'message': "Invalid Uid !", "status": False,'data':{}})


#End


#Class Based View For Rest API
#Convert above Function Based api to below class based api

class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            data["user"] = request.user.id
            seriallzer = ToDoSerializer(data=data)
            if seriallzer.is_valid():
                # print(seriallzer.data)
                seriallzer.save()
                return Response({"status": True, 'message': "Success Data !", 'data': seriallzer.data})
            return Response({"status": False, 'message': "Invalid Data !", 'data': seriallzer.errors})
        except Exception as e:
            print(e)
            return Response({'message': "Something went Wrong!", "status": False})

    def get(self,request):
        print(request.user)
        todo_objs = Todo.objects.filter(user = request.user)
        # todo_objs = Todo.objects.all()
        serializer = ToDoSerializer(todo_objs, many=True)  # more than one object therefore retun many =True
        return Response({"status": True, "message": "Fetched data", "data": serializer.data})

    def patch(self,request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({"status": False, 'message': "Uid is required !", 'data': {}})
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = ToDoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, 'message': "PATCH Updated !", 'data': serializer.data})

            return Response({'message': "Invalid data !", "status": False, 'data': serializer.errors})
        except Exception as e:
            print(e)
            return Response({'message': "Invalid Uid !", "status": False, 'data': {}})
    def put(self,request):
        return Response({'message': "DjangoRest PUT Api working !", "status": 200})
    def delete(self,request):
        return Response({'message': "DjangoRest Delete Api working !", "status": 200})

#End Class View set api

#Model ViewSet

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    #For Custom Method Work with action module of rest_framework
    @action(detail=False,methods=["post"])
    def add_custom_date_to_todo(self,request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, 'message': "Success Data !", 'data': serializer.data})
            return Response({"status": False, 'message': "Invalid Data !", 'data': serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status": False, 'message': "Invalid Key !", 'data': {}})

    @action(detail=False,methods=["GET"])
    def get_custom_timing_data_todo(self,request):
        try:
            objs = TimingTodo.objects.all()
            serializer = TimingTodoSerializer(objs,many=True)
            return Response({"status":True,"message":"Timing todo data Fetched","data":serializer.data})
        except Exception as e:
            print(e)




