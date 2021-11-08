from django.urls import path
from .views import home, todoList, todoListCreate, toDo_list, todoListUpdate, todoListDelete, toDo_detail


urlpatterns = [
    path('', home),
    path('list/', todoList), 
    path('create/', todoListCreate),   
    path('todo/', toDo_list), 
    path('update/<int:pk>/', todoListUpdate),  
    path('delete/<int:pk>/', todoListDelete),    
    path('detail/<int:pk>/', toDo_detail),  
    
]
