from django.contrib import admin
from polls.models import Question, Choice, Member
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(Question)
admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    # 显示多个字段
    list_display = ('question_text', 'pub_date', 'parent')
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)


class MemberAdmin(admin.ModelAdmin):
    # 显示多个字段
    list_display = ('name', 'recommender')
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['first_name', 'last_name', 'create_at', 'update_at', 'mobile', 'recommender']
    search_fields = ['first_name', 'last_name', 'active', 'mobile']


admin.site.register(Member, MemberAdmin)