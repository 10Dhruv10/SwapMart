from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import displaForm
from .models import displa
from django.shortcuts import render, redirect

def delete_displa(request, displa_id):
	displa_instance=displa.objects.get(pk=displa_id)
	displa_instance.delete()
	return redirect('list-display')


def all_display(request):
	displa_list = displa.objects.all()
	return render(request, 'display/displa_list.html',
		{'displa_list':displa_list})

def add_displa(request):
    if not request.user.is_authenticated:
        return redirect('register_user')  # Redirect to the registration page if the user is not authenticated
    
    submitted = False
    if request.method == 'POST':
        form = displaForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  # Associate the user with the form submission
            form.save()
            return redirect('list-display')
    else:
        form = displaForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'display/add_displa.html', {'form': form, 'submitted': submitted})

def update_displa(request, displa_id):
	displa_instance = displa.objects.get(pk=displa_id)
	form = displaForm(request.POST or None, instance = displa_instance)
	if form.is_valid():
		form.save()
		return redirect('list-display')

	return render(request, 'display/update_displa.html',
		{'displa_instance': displa_instance,
		'form': form})

def home(request):
	return render(request, 'display/home.html', {})

def search_results(request):
	material_query = request.GET.get('material', '')
	results = displa.objects.filter(material__icontains=material_query)
	return render(request, 'display/search_results.html', {'results': results, 'query': material_query})

def access_denied(request):
    return render(request, 'display/access_denied.html')

def delete_displa(request, displa_id):
	displa_instance = displa.objects.get(pk=displa_id)
	if request.user.is_authenticated and request.user.username == displa_instance.name:
		displa_instance.delete()
		return redirect('list-display')
	else:
		return render(request, 'display/access_denied.html')

def contact_view(request):
    return render(request, 'display/contact.html', {})