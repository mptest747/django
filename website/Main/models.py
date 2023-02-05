from django.db import models




STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    parent_cat= models.CharField(max_length=50)
    child_cat= models.CharField(max_length=50)

    number_10_title=models.CharField(max_length=100,default='')
    number_10_img=models.ImageField(upload_to='thumbnail/',default='parent_cat/1.png')
    number_10_desc=models.CharField(max_length=500,default='')
    

    number_09_title=models.CharField(max_length=100,default='')
    number_09_img=models.ImageField(upload_to='thumbnail/',default='parent_cat/1.png')
    number_09_desc=models.CharField(max_length=500,default='')
    


    number_08_title=models.CharField(max_length=100,default='')
    number_08_img=models.ImageField(upload_to='thumbnail/',default='parent_cat/1.png')
    number_08_desc=models.CharField(max_length=500,default='')
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name #self.parent_cat+'-'+self.child_cat+'-'+self.name