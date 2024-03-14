from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeEntry
from .forms import TimeEntryForm
from django.contrib.auth.decorators import login_required, permission_required
from collections import defaultdict
from datetime import timedelta

@login_required
@permission_required('timemanagement.can_view_all_entries', raise_exception=True)
def view_all_entries(request):
    entries_by_user = TimeEntry.objects.select_related('user').order_by('user', '-date')
    
    return render(request, 'timemanagement/all_entries.html', {'entries_by_user': entries_by_user})

def delete_entry(request, entry_id):
    if request.method == 'POST':
        entry = get_object_or_404(TimeEntry, id=entry_id, user=request.user)  # Ensure user owns the entry
        entry.delete()
        return redirect('time_entry')
    else:
        # Handle case for non-POST request or show an error message
        return redirect('time_entry')
    
def time_entry(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.user = request.user
            time_entry.save()
            return redirect('time_entry')
    else:
        form = TimeEntryForm()

    # Fetch all entries for the logged-in user
    time_entries = TimeEntry.objects.filter(user=request.user).order_by('-date')

    # Group entries by the Monday of their week
    weeks = defaultdict(list)
    for entry in time_entries:
        # Calculate the Monday of the current entry's week
        monday = entry.date - timedelta(days=entry.date.weekday())
        weeks[monday].append(entry)

    # Sort weeks by Monday's date (newest first)
    sorted_weeks = sorted(weeks.items(), key=lambda x: x[0], reverse=True)

    return render(request, 'timemanagement/time_entry.html', {'form': form, 'weeks': sorted_weeks})
