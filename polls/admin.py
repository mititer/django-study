from django.contrib import admin
from polls.models import Question, Choice
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(Question)
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    # 显示多个字段
    list_display = ('question_txt', 'pub_date', 'parent')
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['question_txt', 'pub_date']
    search_fields = ['question_txt', 'pub_date']

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = verbose_name

admin.site.register(Question, QuestionAdmin)