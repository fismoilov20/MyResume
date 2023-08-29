from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify              # for slug
from ckeditor.fields import RichTextField                      # for ckeditor


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills/')
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)             # The related_name for a OneToOneField in Django is by default the name of the model in lowercase. In our case - 'userprofile'.
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar/')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv/')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact Profile'
        verbose_name_plural = 'Contact Profiles'
        ordering = ['-timestamp']

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    thumbnail = models.ImageField(blank=True, null=True, upload_to='testimonials/')
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Media(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media/')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ['name']
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio/')
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/portfolio/{self.slug}/"
    

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog Profiles'
        ordering = ['timestamp']
    
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog/')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
    

class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name