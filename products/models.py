from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=20)
    description = models.TextField(_('description'),blank=True,max_length=50)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    create_time = models.DateTimeField(_('create time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update time'),auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'),max_length=20)
    description = models.TextField(_('description'),blank=True,max_length=50)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    categories = models.ManyToManyField(Category,verbose_name=_('categories'),blank=True)
    create_time = models.DateTimeField(_('create time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update time'),auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        
    def __str__(self):
        return self.title
    

class File(models.Model):
    File_Audio = 1
    File_Video = 2
    File_Pdf = 3
    File_Types =(
        (File_Audio,_('Audio')),
        (File_Video,_('Video')),
        (File_Pdf,_('Pdf'))
    )
    product = models.ForeignKey('Product',related_name='files',verbose_name=_('product'),on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=20)
    file_type = models.PositiveSmallIntegerField(_('file type'),choices=File_Types)
    file = models.FileField(_('file'),upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    create_time = models.DateTimeField(_('create time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update time'),auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
        
    def __str__(self):
        return self.title