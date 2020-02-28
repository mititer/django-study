from django.contrib import admin
from polls.models import Question, Choice, Member
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(Question)


class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ['choice_text', 'question_id__question_text']


admin.site.register(Choice, ChoiceAdmin)


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 0


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['choice_text']
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    """
    设置Form的样式
    """
    # 调整显示顺序
    # fields = ['pub_date', 'question_text']
    # fieldsets = [
    #     ('Question Information', {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    fieldsets = [
        ('Question Information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    """
    设置列表样式
    """
    # 显示多个字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)


class MemberAdmin(admin.ModelAdmin):
    # 显示多个字段
    list_display = ('first_name', 'last_name', 'colored_name', 'colored_first_name')
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['first_name', 'last_name', 'create_at', 'update_at', 'mobile', 'recommender']
    search_fields = ['first_name', 'last_name', 'active', 'mobile']


admin.site.register(Member, MemberAdmin)