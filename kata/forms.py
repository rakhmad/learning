from datetime import datetime
from django import forms
from kata.models import KataUser

class ProjectForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    start = forms.DateField(initial=datetime.now)
    end = forms.DateField(initial=datetime.now)
    leader = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False), empty_label="Choose Team Leader")
    members = forms.ModelMultipleChoiceField(queryset=KataUser.objects.filter(is_staff=False))


class TaskForm(forms.Form):
    TASK_PRIORITIES = (
        (u'Normal', 'Normal'),
        (u'Immediate', 'Immediate'),
        (u'Urgent', 'Urgent'),
        (u'Critical', 'Critical'),
    )

    TASK_TYPES = (
        (u'Feature', 'Feature'),
        (u'Bug', 'Bug'),
        (u'Enhancement', 'Enhancement'),
        )

    BUG_TYPES = (
        (u'Minor', 'Minor'),
        (u'Normal', 'Normal'),
        (u'Major', 'Major'),
        (u'Critical', 'Critical'),
        (u'Blocking', 'Blocking'),
    )

    TASK_STATUS = (
        (u'Closed', 'Closed'),
        (u'Open', 'Open'),
        (u'Resolved', 'Resolved'),
        (u'Wont Fix', 'Wont Fix'),
        (u'Reopen', 'Reopen'),
    )

    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    reporter = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False))
    assignee = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False))
    priority = forms.ChoiceField(choices=TASK_PRIORITIES)
    tType = forms.ChoiceField(choices=TASK_TYPES)
    bugType = forms.ChoiceField(choices=BUG_TYPES)
    status = forms.ChoiceField(TASK_STATUS)
    start = forms.DateField(initial=datetime.today)
    expected = forms.DateField(initial=datetime.today)


    