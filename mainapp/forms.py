from django import forms
from .models import Vote, VoteSubject


class VoteForm(forms.ModelForm):
	class Meta:
		model = Vote
		fields = (
			'dong',
			'ho',
			'name',
			'tel1',
			'voting',
			'signature'
		)

	def __init__(self, *args, **kwargs):
		super(VoteForm, self).__init__(*args, **kwargs)
		self.fields['dong'].widget.attrs = {'class': 'mdb-select md-form'}
		self.fields['ho'].widget.attrs = {'autocomplete': 'off', 'class': 'form-control'}
		self.fields['name'].widget.attrs = {'autocomplete': 'off', 'class': 'form-control'}
		self.fields['tel1'].widget.attrs = {'autocomplete': 'off', 'class': 'form-control'}
		self.fields['voting'].widget.attrs = {'autocomplete': 'off', 'class': 'form-check-input'}