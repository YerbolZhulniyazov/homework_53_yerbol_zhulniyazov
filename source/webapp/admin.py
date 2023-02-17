from django.contrib import admin

from webapp.models import TODO


# Register your models here.
class TODOAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'detailed_description', 'status', 'completion_date')
    list_filter = ('id', 'title', 'description', 'detailed_description', 'status', 'completion_date')
    search_fields = ('title', 'status')
    fields = ('title', 'description', 'detailed_description', 'status', 'completion_date')
    readonly_fields = ('id',)


admin.site.register(TODO, TODOAdmin)
