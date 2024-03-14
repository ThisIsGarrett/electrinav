from django.db import models
from django.contrib.auth.models import User

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    project_name = models.CharField(max_length=100)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.project_name} on {self.date} by {self.user.username}"

    class Meta:
        ordering = ['date']
        permissions = (("can_view_all_entries", "Can view all entries"),)
