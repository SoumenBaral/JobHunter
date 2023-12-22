from django.contrib import admin
from  . import models

# Register your models here.
class jobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','date','salary')
    list_filter = ('date','salary')
    # search_fields = ['title']
    search_fields = ('title',)
    search_help_text = 'Search here to find you wanted Job'
    # fields = ('title',('description','expire'))
    # exclude = ('title',)
    fieldsets = (
        ("Basic Information", {
            "fields": (
                'title','description'
            ),
        }),
        ("More  Information", {
            "classes":('collapse',),
            "fields": (
                ('expire','salary'),'slug'
            ),
        }),
        
    )
#    'wide' 

admin.site.register(models.jobPost)
admin.site.register(models.Author)
admin.site.register(models.Location)
admin.site.register(models.skills)

