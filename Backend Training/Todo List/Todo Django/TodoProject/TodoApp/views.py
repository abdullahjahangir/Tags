from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .forms import TodoForm, TodoContentForm
from .models import Todo


# # Function Base Views
def todo_list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        form = TodoContentForm()
        return render(
            request, "TodoApp/home.html", context={"todos": todos, "form": form}
        )
    elif request.method == "POST":
        form = TodoContentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todo_list"))
        return HttpResponseRedirect(reverse("todo_list"))


def todo_update(request, pk):
    if request.method == "GET":
        todo = Todo.objects.get(id=pk) if Todo.objects.filter(id=pk).exists() else None
        if todo:
            form = TodoForm(instance=todo)
            return render(
                request, "TodoApp/update.html", context={"todo": todo, "form": form}
            )
        else:
            return HttpResponseRedirect(reverse("todo_list"))
    elif request.method == "POST":
        todo = Todo.objects.get(pk=pk) if Todo.objects.filter(pk=pk).exists() else None
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        else:
            return render(
                request, "TodoApp/update.html", context={"todo": todo, "form": form}
            )
        return HttpResponseRedirect(reverse("todo_list"))


def todo_delete(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(id=pk) if Todo.objects.filter(id=pk).exists() else None
        if todo:
            todo.delete()
        return HttpResponseRedirect(reverse("todo_list"))


# Class Base Views
class TodoList(View):
    def get(self, request):
        todos = Todo.objects.all()
        form = TodoContentForm()
        return render(
            request, "TodoApp/home.html", context={"todos": todos, "form": form}
        )

    def post(self, request):
        form = TodoContentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todo_list"))
        todos = Todo.objects.all()
        return render(
            request, "TodoApp/home.html", context={"todos": todos, "form": form}
        )


class TodoUpdate(View):
    def get(self, request, pk):
        todo = Todo.objects.get(id=pk) if Todo.objects.filter(id=pk).exists() else None
        if todo:
            form = TodoForm(instance=todo)
            return render(
                request, "TodoApp/update.html", context={"todo": todo, "form": form}
            )
        else:
            return HttpResponseRedirect(reverse("todo_list"))

    def post(self, request, pk):
        todo = Todo.objects.get(pk=pk) if Todo.objects.filter(pk=pk).exists() else None
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        else:
            return render(
                request, "TodoApp/update.html", context={"todo": todo, "form": form}
            )
        return HttpResponseRedirect(reverse("todo_list"))


class TodoDelete(View):
    def post(self, request, pk):
        todo = Todo.objects.get(id=pk) if Todo.objects.filter(id=pk).exists() else None
        if todo:
            todo.delete()
        return HttpResponseRedirect(reverse("todo_list"))


# Generic Class Base Views
class TodoTemplateView(TemplateView):
    template_name = "TodoApp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        context["form"] = TodoContentForm()
        return context


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoContentForm
    success_url = reverse_lazy("todo_list")
    template_name = "TodoApp/home.html"
    context_object_name = "todos"

    def form_invalid(self, form):
        context = self.get_context_data()
        context["form"] = form
        context["todos"] = Todo.objects.all()
        return self.render_to_response(context)


class TodoUpdateView(UpdateView):
    model = Todo
    # fields = ["content", "checked"]
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")
    template_name = "TodoApp/update.html"


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


# =========================================
# # Function Base Views
# def todo_list(request):
#     if request.method == "POST":
#         content = request.POST.get("content")
#         if content:
#             new_todo = Todo(content=content)
#             new_todo.save()
#     todos = Todo.objects.all()
#     return render(request, "TodoApp/home.html", context={"todos": todos})


# def todo_detail(request, pk):
#     if request.method == "GET":
#         todo = Todo.objects.get(id=pk) if Todo.objects.filter(id=pk).exists() else None
#         if todo:
#             return render(request, "TodoApp/update.html", context={"todo": todo})
#         else:
#             return HttpResponseRedirect(reverse("todo_list"))
#     elif request.method == "POST":
#         content = request.POST.get("content")
#         is_checked = request.POST.get("is_checked")
#         delete_btn = request.POST.get("delete_btn")
#         todo = get_object_or_404(Todo, pk=pk)
#         if todo and delete_btn:
#             todo.delete()
#         elif todo and content:
#             todo.content = content
#             todo.checked = True if is_checked == "on" else False
#             todo.save()
#         return HttpResponseRedirect(reverse("todo_list"))
