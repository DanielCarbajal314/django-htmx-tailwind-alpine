from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.shortcuts import render
from .models import Task
from django.forms import ModelForm, TextInput


class DateInput(TextInput):
    input_type = "date"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["description", "schedule_at"]
        widgets = {
            "description": TextInput(
                attrs={"class": "w-full border rounded py-2 px-3"}
            ),
            "schedule_at": DateInput(
                attrs={"class": "w-full border rounded py-2 px-3"}
            ),
        }


class TaskView(TemplateView):
    template_name = "task.html"


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy("index")
    template_name = "task_update_form.html"
    form_class = TaskForm

    def form_valid(self, form):
        self.object = form.save()
        context = {"object": self.object}
        return render(self.request, "task_row.html", context)


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm

    def form_valid(self, form):
        print("hola")
        self.object = form.save()
        context = {"object": self.object}
        return render(self.request, "task_row.html", context)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("success_url")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({"message": "Item deleted successfully."})
