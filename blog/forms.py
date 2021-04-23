from django import forms
from .models import Post


class FileForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['file']