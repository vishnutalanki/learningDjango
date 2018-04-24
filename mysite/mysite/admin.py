from django.contrib import admin
 
# Register your models here.
from mysite.notes.models import Note
 
class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note
 
admin.site.register(Note,NoteAdmin)
