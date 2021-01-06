from django.contrib import admin
from .models import Post
''' c models.py импортирую класс Post'''

""" то что было изнчально
admin.site.register(Post)
 Регистрирую свою модель """

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

"""1  list_display позволяет перечислить поля модели, которые мы хотим отображать на странице списка
@admin.register() выполняет те же действия, что и функция admin.site.register() регистрирует декорируемый класс
наследний ModelAdmin

2 list_display    это дополнительные информация в поле где сделан наш пост увидеть автора, дату публикации
3 list_filter     это фильтр справа в админке от нас
4 search_fields  это поиск в админке
5 prepopulated_fields словарь в котором ключ slug связан с полем title!!!!!!!!!
 предварительно заполняемые поля, получается когда указываю название Post в title slug автоматом
подтягивает если кирилица то переводит в латиницу
6 raw_id_fields
7 date_hierarchy иерархия даты над полем Action можем по дата публикациям смотреть
8  ordering  сортировка статей по полю status 

"""



