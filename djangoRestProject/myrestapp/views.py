from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
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
