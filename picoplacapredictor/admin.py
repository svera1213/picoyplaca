from django.contrib import admin

from .models import PicoyplacaConfiguration, PicoyplacaPause, PicoyplacaDay


class PicoyplacaConfigurationAdmin(admin.ModelAdmin):
    search_fields = ['code', 'id']
    list_display = ['id', 'code', 'start_time', 'end_time']


admin.site.register(PicoyplacaConfiguration, PicoyplacaConfigurationAdmin)


class PicoyplacaPauseAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'base_configuration_id', 'start_time', 'end_time']


admin.site.register(PicoyplacaPause, PicoyplacaPauseAdmin)


class PicoyplacaDayAdmin(admin.ModelAdmin):
    search_fields = ['day', 'id']
    list_display = ['id', 'base_configuration_id', 'day', 'plate_key']


admin.site.register(PicoyplacaDay, PicoyplacaDayAdmin)
