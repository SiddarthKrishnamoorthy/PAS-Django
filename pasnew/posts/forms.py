from django import forms

from pagedown.widgets import PagedownWidget
from django.utils import timezone
from .models import Post
from .models import Program_Department_Relationship
from .models import Department
from .models import Program



class PostForm1(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    checkbox = forms.ModelMultipleChoiceField(
        queryset=Program_Department_Relationship.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Post
        fields = [
            "title",
            "salary",
            "file",
        ]

class PostForm2(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            "experience_required",
            "draft",
            "publish",
        ]

class PostForm3(forms.ModelForm):
    experience_required = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",  
        ]
