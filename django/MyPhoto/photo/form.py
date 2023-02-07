from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        # image -> imagefile 변경
        model = Photo
        fields = ('title', 'author' ,
                  'imagefile' ,
                  'description' , 'price')
        