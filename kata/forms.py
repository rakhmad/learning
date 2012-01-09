from django import forms
from django.forms import extras
from myweb.kata.models import KataUser

class ProjectForm(forms.Form):
	name = forms.CharField()
	desc = forms.CharField(widget=forms.Textarea)
	sdw = forms.extras.widgets.SelectDateWidget()
	start = forms.DateField(widget=sdw)
	end = forms.DateField(widget=sdw)
	leader = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False), empty_label="Pilih Ketua")
	members = forms.ModelMultipleChoiceField(queryset=KataUser.objects.filter(is_staff=False), widget=forms.CheckboxSelectMultiple)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		start = cleaned_data.get('start')
		end = cleaned_data.get('end')
		if start > end:
			raise forms.ValidationError('Tanggal berakhir proyek tidak boleh lebih dulu dibandingkan tanggal mulai')
		
		return cleaned_data
	
	
class TaskForm(forms.Form):
	name = forms.CharField()
	desc = forms.CharField(widget=forms.Textarea)
	reporter = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False))
	assignee = forms.ModelChoiceField(queryset=KataUser.objects.filter(is_staff=False))
	priority = forms.ChoiceField()
	tType = forms.ChoiceField()
	bugType = forms.ChoiceField()
	status = forms.ChoiceField()
	start = forms.DateField()
	expected = forms.DateField()
	
	