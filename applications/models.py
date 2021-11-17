from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse


class ApplicationType(OrderedModel):
    title = models.CharField(max_length=64)
    description = models.TextField()
    online_app = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='images')

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('applications:description', kwargs={'slug': self.slug})


class Application(OrderedModel):
    title = models.CharField(max_length=64)
    content = models.TextField()
    slug = models.SlugField()
    link_github = models.TextField()
    link_site = models.TextField()
    application_type = models.ForeignKey('ApplicationType', on_delete=models.CASCADE)
    order_with_respect_to = 'application_type'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('applications:project', kwargs={'slug': self.slug})
