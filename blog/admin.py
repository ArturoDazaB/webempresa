from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # SE ESPECIFICAN QUE COLUMNAS MOSTRAR 
    list_display = ('title', 'author', 'published', 'post_categories')
    # SE ESPECIFICA COMO ORGANIZAR CADA REGISTRO DE LAS ENTRADAS (POST)
    ordering = ('author', 'published')
    # FORMULARIO DE BUSQUEDA DE REGISTROS DE ENTRADAS
    search_fields = ('title','content', 'author__username', 'categories__name')
    # JERARQUIA DE FECHAS (FILTRO DE FECHAS)
    date_hierarchy = 'published'
    # FILTRADO POR USUARIO
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

