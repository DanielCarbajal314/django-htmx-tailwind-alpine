from django.db.models import Model, CharField, DateField, DateTimeField


class Task(Model):
    description = CharField()
    schedule_at = DateField()
    created_at = DateTimeField(auto_now_add=True, blank=True)
