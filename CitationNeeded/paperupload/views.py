from django.shortcuts import render, redirect
from .forms import PaperUploadForm


def model_form_upload(request):
    if request.method == 'POST':
        form = PaperUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PaperUploadForm()
    return render(request, 'paperupload/model_form_upload.html', {
        'form': form
    })
