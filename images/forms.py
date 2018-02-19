from django import forms

from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')

        # We override the default widget of the url field to use
        # a HiddenInput widget
        widgets = {
            'url': forms.HiddenInput,
        }

        def clean_url(self):
            url = self.cleaned_data['url']
            valid_extensions = ['jpg', 'jpeg']
            extension = url.rsplit('.', 1)[1].lower()
            print(extension)
            if extension not in valid_extensions:
                raise forms.ValidationError('The given URL does not' \
                                                        'match valid image extensions')
            return url


        # Method save overrided
        def save(self, force_insert=False,
                                force_update=False,
                                commit=True):

            # Creates a new image instance by calling the save() method
            # with commit=False
            image = super(ImageCreateForm, self).save(commit=False)
            image_url = self.cleaned_data['url']
            image_name = '{}.{}'.format(slugify(image.title),
                 image_url.rsplit('.', 1)[1].lower())

            # Download image from the given URL
            response = request.urlopen(image_url)

            # We call the save() method of the image field.
            # In this way we save the file to the media directory of our project
            # but with save=False to avoid saving the object to db yet.
            image.image.save(image_name, ContentFile(response.read()),
                 save=False)
            if commit:
                image.save()
            return image
