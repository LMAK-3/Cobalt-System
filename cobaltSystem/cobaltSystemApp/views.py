from django.shortcuts import render, redirect
from .models import add_user
from .forms import Model_Add_U

# Create your views here.
def home(request):
	add_user_ = add_user.objects.all()
	if request.method=="POST":
		form=Model_Add_U(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request, 'home.html', {'add_user': add_user_, 'forme':Model_Add_U})

def eliminar(request, person_id):
	person= add_user.objects.get(id=person_id)
	person.delete()
	return redirect('home')

def editar(request, person_id):
	user=add_user.objects.get(id=person_id)
	if request.method=="POST":
		form=Model_Add_U(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=Model_Add_U(instance=user)
	context={'form': form}
	return render(request, 'editar.html', context)

