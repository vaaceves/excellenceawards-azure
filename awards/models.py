from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from django_countries.fields import CountryField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    today = datetime.now()
    today_path = today.strftime("%Y/%m/%d")
    return '{0}/{1}/{2}'.format(today_path,
                                instance.slug,
                                filename
                                )


# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=144)
    slug = models.SlugField(max_length=144)
    description = models.TextField(max_length=600)
    image_cover = models.ImageField(upload_to=user_directory_path, null=True)
    nominator = models.CharField(max_length=144)
    nomination_comments = models.TextField(max_length=1200)
    country = CountryField()
    site = models.CharField(max_length=144, default='GLS')
    interviewee = models.CharField(max_length=144)
    interviewee_contact = models.EmailField(max_length=144)
    question = models.CharField(max_length=144)
    file_id = models.CharField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    featured = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def _get_unique_slug(self):
        slug_string = self.name
        slug = slugify(slug_string)
        unique_slug = slug
        num = 1
        while Award.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=Award)
# def convert_video(sender, instance, **kwargs):
#     enqueue(tasks.convert_all_videos,
#             instance._meta.app_label,
#             instance._meta.model_name,
#             instance.pk)
