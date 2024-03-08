from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}- {self.content[0:10]} {self.checked}"
