from django.shortcuts import render
from .forms import UploadFileForm
from .controller import home_controller, upload_controller
from django.core.files.storage import FileSystemStorage


def index(request):
    context = {}
    results = home_controller.get_registers()
    context["results"] = results
    return render(request, 'home.html',context)


def upload_file(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES['csv_file']
        fs = FileSystemStorage()
        name = fs.save(file.name,file)
        context['url'] = fs.url(name)
        context['name'] = name
        upload_controller.read_csv(file,name)
        # return HttpResponseRedirect('/success')
    else:        
        form = UploadFileForm()
        context['form'] = form
    return render(request, 'upload.html', context)
