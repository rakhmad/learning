from django.db import models

from django.contrib.auth.models import User

class KataUser(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.full_name()

    def full_name(self):
        return self.first_name + " " + self.last_name


class Projects(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    ## Project Details    
    name = models.CharField(max_length=200, verbose_name='Nama')
    desc = models.TextField(verbose_name='Deskripsi')
    ## Project's Date
    start = models.DateField(verbose_name='Tanggal Mulai')
    end = models.DateField(verbose_name='Tanggal Selesai')

    ## Project Members
    leader = models.ForeignKey('KataUser', verbose_name='Team Leader', limit_choices_to={'is_staff': False})
    members = models.ManyToManyField('KataUser', related_name='+', verbose_name='Anggota Tim',
        limit_choices_to={'is_staff': False})

    def __unicode__(self):
        return self.name

    def get_team_members(self):
        return self.members.all()


class Tasks(models.Model):
    class Meta:
        verbose_name_plural = 'Tasks'

    ## Choices

    TASK_PRIORITIES = (
        (u'Normal', 'Normal'),
        (u'Immediate', 'Immediate'),
        (u'Urgent', 'Urgent'),
        (u'Critical', 'Critical'),
        )
    TASK_TYPES = (
        (u'Feature', 'Feature'),
        (u'Bug', 'Bug'),
        (u'Enhancement', 'Enhancement'),
        )
    BUG_TYPES = (
        (u'Minor', 'Minor'),
        (u'Normal', 'Normal'),
        (u'Major', 'Major'),
        (u'Critical', 'Critical'),
        (u'Blocking', 'Blocking'),
        )
    TASK_STATUS = (
        (u'Closed', 'Closed'),
        (u'Open', 'Open'),
        (u'Resolved', 'Resolved'),
        (u'Wont Fix', 'Wont Fix'),
        (u'Reopen', 'Reopen'),
        )

    #Fields
    tName = models.CharField(max_length=200, verbose_name='Nama')
    tDesc = models.TextField(verbose_name='Deskripsi')
    reporter = models.ForeignKey('KataUser', related_name='+', limit_choices_to={'is_staff': False})
    assignee = models.ForeignKey('KataUser', related_name='+', limit_choices_to={'is_staff': False})
    tPriority = models.CharField(max_length=15, choices=TASK_PRIORITIES, verbose_name='Prioritas')
    tType = models.CharField(max_length=15, choices=TASK_TYPES, verbose_name='Tipe')
    tBugType = models.CharField(max_length=15, choices=BUG_TYPES, verbose_name='Jenis Laporan')
    tStatus = models.CharField(max_length=15, choices=TASK_STATUS, verbose_name='Status')
    tStart = models.DateField(verbose_name='Mulai Pekerjaan')
    tExpected = models.DateField(verbose_name='Ekspektasi')
    project = models.ForeignKey(Projects)

    #Methods
    def __unicode__(self):
        return self.tName
