from django.shortcuts import render
from django.views.generic import TemplateView
# from app_code.models import Melody, Notes

from music_api.models import Melody
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # array = Melody(uploaded_file)
        # array.dataToArray()
        # pdf = Notes(array).converteToPdf()
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')
