from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Unitsdb
from django.contrib import admin
from .models import CustomUser
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Unitsdb)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("name", 'fr', 'type', 'preview',)
    readonly_fields = ["preview"]
    summernote_fields = ('des',)

    def preview(self, obj):
        return mark_safe(f"<img src=\"{obj.img.url[6:]}\" style=\"width:30px; height:30px; border-radius: 20px;\" >") #onclick=\"window.location=\"{{/units/{<int:pk> object.id}}}\";\"

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email",'first_name','last_name','is_active','is_staff','is_superuser',)
    search_fields = ('email', 'first_name')
    #readonly_fields = ('date_joined', 'last_login')

    #admin.site.register(Unitsdb)