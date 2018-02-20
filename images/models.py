from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Image(models.Model):

    # A user can post multiple images, but each image is posted by a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='images_created')

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)

    url =models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)

    # auto_now_add, this datetime is automatically set when the object is created
    # db_index=True, Django creates an index in the db for this field
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    # A user might like multiple images and each image can be liked by
    # multiple users.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='images_liked', blank=True)


    def __str__(self):
        return self.title

    # Overrided method save()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
