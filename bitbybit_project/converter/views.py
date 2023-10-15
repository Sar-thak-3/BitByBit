from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render, redirect
from .models import UploadFile
from .forms import UploadFileForm
# from .handlefiles import handle_uploaded_file
from .convert import convert_file

# def home(request):
    # return render(request, "basics/main.html")

def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            convert_file()
            return redirect('down')
    else:
        form = UploadFileForm()
    
    return render(request, 'converter/upload_main.html', {
        'form': form
    })

def download_page(request):
    return render(request, 'converter/download_main.html')


def download(request):

    path = "output.docx.docx"
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    UploadFile.objects.all().delete()
    os.remove(os.path.join(settings.MEDIA_ROOT, "input.html"))

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    
    raise "Http404"
     