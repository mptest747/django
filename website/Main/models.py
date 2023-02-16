from django.db import models




STATUS = ((0, "Draft"),(1,"Reviewd"),(2, "Published"))

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    parent_cat= models.CharField(max_length=50)
    child_cat= models.CharField(max_length=50)
    is_affiliate=models.BooleanField(default=False)
    


    title_number_10=models.CharField(max_length=100,default='')
    img_number_10=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_10=models.CharField(max_length=500,default='')

    title_number_9=models.CharField(max_length=100,default='')
    img_number_9=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_9=models.CharField(max_length=500,default='')

    title_number_8=models.CharField(max_length=100,default='')
    img_number_8=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_8=models.CharField(max_length=500,default='')

    title_number_7=models.CharField(max_length=100,default='')
    img_number_7=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_7=models.CharField(max_length=500,default='')

    title_number_6=models.CharField(max_length=100,default='')
    img_number_6=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_6=models.CharField(max_length=500,default='')

    title_number_5=models.CharField(max_length=100,default='')
    img_number_5=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_5=models.CharField(max_length=500,default='')

    title_number_4=models.CharField(max_length=100,default='')
    img_number_4=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_4=models.CharField(max_length=500,default='')

    title_number_3=models.CharField(max_length=100,default='')
    img_number_3=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_3=models.CharField(max_length=500,default='')
    
    title_number_2=models.CharField(max_length=100,default='')
    img_number_2=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_2=models.CharField(max_length=500,default='')

    title_number_1=models.CharField(max_length=100,default='')
    img_number_1=models.ImageField(upload_to='post_images/',default='post_images/default.jpg')
    desc_number_1=models.CharField(max_length=500,default='')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name 