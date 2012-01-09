from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from .models import Projects
from .forms import ProjectForm

# Create your views here.

def index(request):
	projects = Projects.objects.all()
	title = "Daftar Project"
	msg = "Selamat Datang"
	template = "kata/index.html"
	context = {
		'projects' : projects,
		'title' : title,
		'msg' : msg,
	}
	return render_to_response(template, context)
	
def detail(request):
	pass

def edit(request):
	pass

def add(request):
	data = {}
	msg = ''
	
	if request.method == 'POST':
		title = 'Tambah Proyek'
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = Projects()
			project.name = form.cleaned_data['name']
			project.desc = form.cleaned_data['desc']
			project.start = form.cleaned_data['start']
			project.end = form.cleaned_data['end']
			project.leader = form.cleaned_data['leader']
			project.save()
			project = Projects.objects.get(name = form.cleaned_data['name'])
			project.members = form.cleaned_data['members']
			project.save()		
			msg = 'Sukses Menambahkan Proyek Baru'		
	else:
		form = ProjectForm()
		msg = 'Menambahkan Proyek Baru'
		title = 'Tambah Proyek'
		data = {
			'form' : form,
			'msg' : msg,
			'title' : title,
		}
		
	template = 'kata/add.html'
	return render_to_response(template, data, context_instance=RequestContext(request))

@csrf_exempt
def task_add(request):
	pass

def task_edit(request):
	pass