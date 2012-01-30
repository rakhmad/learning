from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Projects, Tasks
from .forms import ProjectForm, TaskForm

# Create your views here.

def index(request):
    title = 'Home'
    template = "kata/home.html"
    context = {
        'title' : title
    }
    return render_to_response(template, context)

def list_project(request):
    projects = Projects.objects.all()
    title = "Project List"
    msg = "Project List"
    template = "kata/index.html"
    context = {
        'projects': projects,
        'title': title,
        'msg': msg,
        }
    return render_to_response(template, context)


def detail_project(request, id):
    project = Projects.objects.get(id=id)
    title = 'Project Details'
    msg = 'Project Details for ' + project.name

    data = {
        'project': project,
        'title': title,
        'msg': msg,
        }
    template = "kata/detail.html"
    return render_to_response(template, data)


def edit_project(request):
    pass


def add_project(request):
    data = {}
    msg = ''
    if request.method == 'POST':
        title = 'Create new project'
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Projects()
            project.name = form.cleaned_data['name']
            project.desc = form.cleaned_data['desc']
            project.start = form.cleaned_data['start']
            project.end = form.cleaned_data['end']
            project.leader = form.cleaned_data['leader']
            project.save()
            project = Projects.objects.get(name=form.cleaned_data['name'])
            project.members = form.cleaned_data['members']
            project.save()
            msg = 'New Project created successfully.'
    else:
        form = ProjectForm()
        msg = 'Create New Project'
        title = 'New Project'

    data = {
        'form': form,
        'msg': msg,
        'title': title,
    }

    template = 'kata/add.html'
    return render_to_response(template, data, context_instance=RequestContext(request, {}))

def add_task(request, id):
    data = {}
    msg = 'Creating new Task'
    title = 'New Task'
    project = Projects.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            msg = 'Task Created Successfully'
            task = Tasks()
            task.name = form.cleaned_data['name']
            task.desc = form.cleaned_data['desc']
            task.reporter = form.cleaned_data['reporter']
            task.assignee = form.cleaned_data['assignee']
            task.priority = form.cleaned_data['priority']
            task.tType = form.cleaned_data['tType']
            task.bugType = form.cleaned_data['bugType']
            task.status = form.cleaned_dta['status']
            task.start = form.cleaned_data['start']
            task.expected = form.cleaned_data['expected']
            task.project = project
            task.save()
    else:
        form = TaskForm()

    data = {
        'form': form,
        'title': title,
        'msg': msg,
        }

    template = "kata/new_task.html"

    return render_to_response(template, data, context_instance=RequestContext(request, {}))

def edit_task(request):
    pass