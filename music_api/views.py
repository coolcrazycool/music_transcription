from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from hyper_music.settings import MEDIA_ROOT

# Own views are here
from .forms import MelodyForm, CreateUserForm
from .serializers import MelodySerializer
from app_code.models import Notes, CodeMelody
from music_api.models import Melody


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profilePage(request):
    melodys = Melody.objects.filter(user=request.user.id)
    return render(request, 'accounts/profile.html', {'melodys': melodys})


@login_required(login_url='login')
def upload(request):
    form = MelodyForm()
    if request.method == 'POST':
        form = MelodyForm(request.POST, request.FILES)
        # try:
        mel = str(request.FILES['melody'])
        if form.is_ok(mel):
            melody_pr = form.save(commit=False)
            melody_pr.melody = request.FILES['melody']
            melody_pr.name = request.POST['name']
            melody_pr.user = request.user
            melody_pr.status = 'Uploaded'
            form.save()
            obj = Melody.objects.latest('id')
            obj.status = 'Uploaded'
            obj.save()
            return redirect('profile')
        # except Exception as e:
        # raise forms.ValidationError('Can not identify file type')
        else:
            messages.info(request, 'Invalid data type. Only wav')

    return render(request, 'upload.html', {'form': form})

def converte(request, pk):
    melody = get_object_or_404(Melody, pk=pk)
    NOTES = CodeMelody(f'{MEDIA_ROOT}/{melody.melody}')
    data = NOTES.data
    PDF = Notes(data)
    pdf = PDF.converteToPdf(f'{melody.melody}'.split('/')[-1].split('.')[0])
    melody.pdf.name = f'pdf/{pdf}.pdf'
    melody.status = 'Converted'
    melody.save()
    return redirect('profile')


class MelodyView(APIView):
    def get(self, request):
        melodys = Melody.objects.all()
        serializer = MelodySerializer(melodys, many=True)
        return Response({"melodys": serializer.data})
