from django.db import models
from django.utils import timezone
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Create your models here.


class MemberType(models.Model):
    name = models.CharField(verbose_name=_('member type name'), max_length=20)
    create_at = models.DateTimeField(verbose_name=_('create time'), auto_created=True, auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(verbose_name=_('update time'), auto_created=True, auto_now_add=False, auto_now=True)


class Member(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=60, default="")
    name2 = models.CharField(verbose_name=_('name'), max_length=60, default="")
    first_name = models.CharField(verbose_name=_('first name'), max_length=30)
    last_name = models.CharField(verbose_name=_('last name'), max_length=30)
    color_code = models.CharField(max_length=6, default="")
    mobile = models.CharField(verbose_name=_('mobile'), max_length=11)
    active = models.IntegerField(verbose_name=_('active'))
    sex = models.CharField(verbose_name=_('sex'), max_length=2)
    recommender = models.IntegerField(verbose_name=_('recommender'))
    create_at = models.DateTimeField(verbose_name=_('create time'), auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(verbose_name=_('update time'), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )

    def colored_first_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color_code,
            self.first_name,
        )

    colored_first_name.admin_order_field = 'first_name'

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = verbose_name


class Question(models.Model):
    question_text = models.CharField(verbose_name=_('question'), max_length=200)
    pub_date = models.DateTimeField(verbose_name=_('published date'))
    parent = models.ForeignKey('self', verbose_name=_('parent question'), on_delete=models.NOT_PROVIDED, null=True, blank=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    """
    以下3个属性用于设置was_published_recently()方法在admin界面中作为列表的列时的显示问题
    """
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Published recently ?')

    def __str__(self):
        return self.question_text

    # def parent(self):
    #     if self.parent is None:
    #         return _('None')
    #     return self.parent.question_text

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = verbose_name


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='调研问题', on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='答案', max_length=200)
    votes = models.IntegerField(verbose_name='已投票', default=0)

    def __str__(self):
        return f'[{self.question_id}]-' + self.choice_text

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = verbose_name