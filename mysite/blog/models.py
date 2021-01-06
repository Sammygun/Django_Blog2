from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    """Создаем своего менеджера вместо стандартного objects """
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, 
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager()           # менеджер по умолчанию
    published = PublishedManager()       # наш новый менеджер


    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    ''' title это поле заголовка статьи опеределено как Charfield, который сооотвествует VARCHAR в базе данных '''
    """ slug поле для формирования URL'ов, нужно для построения семантических url для статаей, параметр unique_for_date
    позволяет формировать дату публикаций статей slug используется для создания уникальных url  """
    ''' author поле которое говорит о том, что у каждой статьи есть свой автор, параметр on_delete говорит о том, что
    если мы удалим все пользователя, автора  то тогда все статьи будут удалены '''
    '''body основное содержание статьи текстовое поле котрое будет сохранено в столбце с типом TEXT в sql базе данных ''' 
    '''' publish поле даты, которое сохраняет дату публикации статьи. Параметр timezone.now. Она возвращает текущие дату 
    и время при написании статьи'''
    '''created указывает дату создания статьи auto_now_add дата будет сохраняться автоматически при создании объекта'''
    '''updated дата и время, указывающая период когда статья была отредактирована'''
    ''' status статус статьи '''
    ''' https://docs.djangoproject.com/en/2.0/ref/models/fields/'''
    ''' META порядок статей по убыванию -publish, только что опубликованные статьи будут первыми'''
    ''' __str__()  возвращает отображение понятное человеку '''

