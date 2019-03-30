from django import forms

class AddLinkForm(forms.Form):
	link_input = forms.CharField(label="Add a link: ", max_length=50)

class EditLinkForm(forms.Form):
	new_link_title = forms.CharField(label="New link title: ", max_length=50)