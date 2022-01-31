from django.contrib import admin
from home.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(AllQuizes)
admin.site.register(QuizFinal)

admin.site.register(UserContainer)
admin.site.register(Student)
admin.site.register(QuestionFinal)
admin.site.register(StudentFinal)

class QuestionFinalAdmin(ImportExportModelAdmin):
    list_display= ('tutor', 'que', 'number', 'op1', 'op2', 'op3','op4','ans')




