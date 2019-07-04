from django.shortcuts import render, redirect

from mainapp.forms import VoteForm
from mainapp.models import VoteSubject, Vote


def listview(request):
	lists = VoteSubject.objects.filter(status=True)
	context = {
		'lists': lists
	}
	return render(request, 'mainapp/listview.html', context)


def detail(request, pk):
	subject = VoteSubject.objects.get(pk=pk)
	if request.method == 'POST':
		form = VoteForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.which = pk
			post.save()
			return redirect('list')
	else:
		form = VoteForm()

	context = {
		'subject': subject,
		'form': form,
	}
	return render(request, 'mainapp/detail.html', context)