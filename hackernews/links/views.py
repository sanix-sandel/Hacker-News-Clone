from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LinkForm
from .models import Link

def home(request):
    links=Link.objects.all()
    return render(request, 'links/welcome.html', {'links':links})

@login_required
def link_submit(request):
    if request.method=='POST':
        form=LinkForm(data=request.POST)
        
        if form.is_valid():
            
            newlink=form.save(commit=False)
            newlink.submitted_by=request.user
            newlink.save()
    else:
        form=LinkForm(request.GET) 
    return render(request, 'links/submission.html',
                 {'form':LinkForm})  


def link_view(request, id):
    link=get_object_or_404(Link, id=id)
    return render(request, 'links/link_view.html', {'link':link})

# Create your views here.
