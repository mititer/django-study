from django.db import models
from django.contrib.admin import ModelAdmin
from django.utils import timezone
import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(verbose_name=_('first name'), max_length=30)
    last_name = models.CharField(verbose_name=_('last name'), max_length=30)
    mobile = models.CharField(verbose_name=_('mobile'), max_length=11)
    active = models.IntegerField(verbose_name=_('active'))
    sex = models.CharField(verbose_name=_('sex'), max_length=2)
    recommender = models.IntegerField(verbose_name=_('recommender'))
    create_at = models.DateTimeField(verbose_name=_('create time'), auto_created=True, auto_now=False)
    update_at = models.DateTimeField(verbose_name=_('update time'), auto_created=False, auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = verbose_name

class Question(models.Model):
    question_text = models.CharField(verbose_name=_('question'), max_length=200)
    pub_date = models.DateTimeField(verbose_name=_('published date'))
    parent = models.ForeignKey('self', verbose_name=_('parent question'), on_delete=models.NOT_PROVIDED, null=True, blank=True)

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