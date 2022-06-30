from rest_framework import  serializers
import re
from .models import Todo
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todo
        # fields = "__all__" # when displayed all the field in api the use this
        fields =["todo_title","todo_description","is_done","uid"]
        #exclude =["todo_title"] Exclude key word use to not displayed the field

    #Data Validation
    def validate_todo_title(self,data):
        if data:
            todo_title = data
            if len(todo_title) < 5:
                raise serializers.ValidationError("todo_title must be greater than 5 character")
            regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:\[\]]')
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError("todo_title cannot contain special character !")
        return data
    #Alternate way data Validation
    # def validate(self,validate_data):
    #     if validate_data.get("todo_title"):
    #         todo_title =validate_data["todo_title"]
    #         if len(todo_title) < 5:
    #             raise serializers.ValidationError("todo_title must be greater than 5 character")
    #         regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:\[\]]')
    #         if not regex.search(todo_title)==None:
    #             raise serializers.ValidationError("todo_title cannot contain special character !")
    #     return validate_data