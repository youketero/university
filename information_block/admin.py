from django.contrib import admin

# Register your models here.
from information_block.models import Articles, Partner, future_conference_anonce,Info


class article_fil(admin.ModelAdmin):
    list_display = ["title", 'date']
    list_filter = ['date']

    class Meta:
        model = Articles


admin.site.register(Articles, article_fil)
admin.site.register(Partner)
admin.site.register(future_conference_anonce)
admin.site.register(Info)