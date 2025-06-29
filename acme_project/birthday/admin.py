from django.contrib import admin

from .models import Birthday


class BirthdayInline(admin.StackedInline):
    model = Birthday
    extra = 0


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )

    search_fields = ('first_name',)
    list_filter = ('first_name',)
    list_display_links = ('first_name',)


admin.site.register(Birthday, BirthdayAdmin)

admin.site.empty_value_display = 'Не задано'
