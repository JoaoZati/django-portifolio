from django.db import models
from ordered_model.models import OrderedModel
from applications.models import Application


# Create your models here.
class FrontApp(OrderedModel):
    title = models.TextField()
    subtitle = models.TextField(blank=True)
    content = models.TextField()
    img = models.ImageField(upload_to='images')
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title
