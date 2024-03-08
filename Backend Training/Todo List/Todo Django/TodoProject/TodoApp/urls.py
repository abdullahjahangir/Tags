from django.urls import path
from .views import (
    todo_list,
    todo_update,
    todo_delete,
)
from .views import (
    TodoList,
    TodoUpdate,
    TodoDelete,
)

from .views import (
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoTemplateView,
)

# from .views import todo_list, todo_detail

# Function Base View
# urlpatterns = [
#     path("", todo_list, name="todo_list"),
#     path("update/<int:pk>/", todo_update, name="todo_update"),
#     path("delete/<int:pk>/", todo_delete, name="todo_delete"),
# ]

# Class Base View
# urlpatterns = [
#     # Class Base View
#     path("", TodoList.as_view(), name="todo_list"),
#     path("update/<int:pk>/", TodoUpdate.as_view(), name="todo_update"),
#     path("delete/<int:pk>/", TodoDelete.as_view(), name="todo_delete"),
# ]

# Generic Class Base View
urlpatterns = [
    path("", TodoTemplateView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
