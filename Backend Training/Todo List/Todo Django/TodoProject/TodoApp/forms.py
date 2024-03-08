from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["content", "checked"]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data["content"]
        if len(content) < 5:
            self.add_error("content", "content length is less than 5")


class TodoContentForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["content"]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data["content"]
        if len(content) < 5:
            self.add_error("content", "content length is less than 5")
