from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# class NewTaskForm(inherit from): 
class NewTaskForm(forms.Form):
    # inside of this class I need to define all of the fields 
    # I would like for this form to have
    # all of the inputs that I would like the user to provide.
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# # add a new task:
# def add(request):
#     # Check if method is POST
#     if request.method == "POST":
#         # Take in the data the user submitted and save it as form
#         form = NewTaskForm(request.POST)
        
#         # Check if form data is valid ( server-side )
#         if form.is_valid():
#             # Isolate the task from the 'cleaned' version of form data
#             task = form.cleaned_data["task"]
#             # Add the new task to our list of tasks
#             tasks.append(task)
#             # Redirect user to list of tasks
#             return HttpResponseRedirect(reverse("tasks:index"))
    
#     else: 
#         # If the form is invalid, re-render the page with existing information.
#         return render(request, "tasks/add.html", {
#             "form": form
#             # we pass in the form that they sumitted so that they
#             # can see all of the errors they made.
#             # They can make modifications to their own form submission 
#             # if they'd like to.
#         })
#     return render(request, "tasks/add.html", {
#         "form": NewTaskForm()
#     })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # request.session["tasks"].append(task) NOT WORKING LIKE THAT
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })