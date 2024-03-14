from django.urls import path
from . import views
from .views import view_all_entries

urlpatterns = [
    path('time-entry/', views.time_entry, name='time_entry'),
    path('delete-entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('all-entries/', view_all_entries, name='all_entries'),
    # Ensure other URL patterns are correctly defined here as well
]

