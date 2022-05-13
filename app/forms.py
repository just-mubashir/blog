from pyexpat import model
from django import forms
from app.models import Contact,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'