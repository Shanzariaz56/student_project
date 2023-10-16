from django.urls import path
from .views import *
urlpatterns = [
    path("get", getAllStudent,name="getAllStudent"),
    path("get/<str:id>",getById,name="getById"),
    path("post",addStudent,name="addStudent"),
    path("put/<str:id>",updateStudent,name="updateStudent"),
    path("delete/<str:id>",deleteStudent,name="deleteStudent"),
]
