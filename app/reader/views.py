from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UploadFileForm
from .crud import csv_reader
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name: str = 'home.html'


def index(request):
    # HttpResponse("ola mundo, eu sou o javier")
    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        fs = FileSystemStorage()
        fs.save(file.name,file)
        print(file.name)
        print(file.size)
        csv_reader.read_csv(file)
        return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
