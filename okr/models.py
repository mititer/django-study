from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Projects(models.Model):
    """
    项目表
    """
    name = models.CharField(verbose_name=_('project name'), max_length=255)
    description = models.TextField(verbose_name=_('project description'), blank=True, null=True)
    homepage = models.CharField(verbose_name=_('project homepage'), max_length=255, blank=True, null=True)
    """
    is_pubic: redmine is integer type
    """
    is_public = models.BooleanField(verbose_name=_('is public'), default=0)
    parent_id = models.IntegerField(verbose_name=_('parent project'), blank=True, null=True)
    created_on = models.DateTimeField(verbose_name=_('created time'), blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name=_('updated time'), blank=True, null=True)
    # project code
    identifier = models.CharField(verbose_name=_('project identifier'), max_length=255, blank=True, null=True)
    # project status
    status = models.IntegerField(verbose_name=_('project status'))
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    inherit_members = models.IntegerField(verbose_name=_('inherit members from project'))
    default_version_id = models.IntegerField(verbose_name=_('default version'), blank=True, null=True)
    default_assigned_to_id = models.IntegerField(verbose_name=_('default project owner'), blank=True, null=True)


class ProjectsTrackers(models.Model):
    """
    项目跟踪标签关系表
    每个项目内容标签唯一
    """
    project_id = models.IntegerField(verbose_name=_('project id'))
    tracker_id = models.IntegerField(verbose_name=_('tracker id'))

    class Meta:
        unique_together = (('project_id', 'tracker_id'),)


class IssueCategories(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=60)
    assigned_to_id = models.IntegerField(blank=True, null=True)


class IssueRelations(models.Model):
    """
    问题关系表
    """
    issue_from_id = models.IntegerField(verbose_name=_('issue from'))
    issue_to_id = models.IntegerField(verbose_name=_('issue to'))
    relation_type = models.CharField(verbose_name=_('relation type'), max_length=255)
    delay = models.IntegerField(verbose_name=_('delay'), blank=True, null=True)

    class Meta:
        unique_together = (('issue_from_id', 'issue_to_id'),)


class IssueStatuses(models.Model):
    """
    问题状态表
    """
    name = models.CharField(verbose_name=_('issue status name'), max_length=30)
    is_closed = models.BooleanField(verbose_name=_('关闭'))
    position = models.IntegerField(verbose_name=_('顺序'), blank=True, null=True)
    default_done_ratio = models.IntegerField(blank=True, null=True)


class Issues(models.Model):
    """
    问题表
    """
    tracker_id = models.IntegerField(verbose_name=_('tracker'))
    project_id = models.IntegerField(verbose_name=_('project'))
    subject = models.CharField(verbose_name=_('subject'), max_length=255)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    due_date = models.DateField(verbose_name=_('due date'), blank=True, null=True)
    category_id = models.IntegerField(verbose_name=_('category'), blank=True, null=True)
    status_id = models.IntegerField(verbose_name=_('status'))
    assigned_to_id = models.IntegerField(verbose_name=_('issue owner'), blank=True, null=True)
    priority_id = models.IntegerField(verbose_name=_('priority'))
    fixed_version_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(verbose_name=_('creator'))
    lock_version = models.IntegerField()
    created_on = models.DateTimeField(verbose_name=_('created time'), blank=True, null=True)
    updated_on = models.DateTimeField(verbose_name=_('updated time'), blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    done_ratio = models.IntegerField(verbose_name=_('done ratio'))
    estimated_hours = models.FloatField(verbose_name=_('estimated hours'), blank=True, null=True)
    parent_id = models.IntegerField(verbose_name=_('parent issues'), blank=True, null=True)
    root_id = models.IntegerField(verbose_name=_('root issue'), blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    is_private = models.IntegerField(verbose_name=_('private'))
    closed_on = models.DateTimeField(verbose_name=_('closed date'), blank=True, null=True)
