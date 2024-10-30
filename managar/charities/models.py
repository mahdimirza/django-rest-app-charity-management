from django.db import models
from accounts.models import User
from django.db.models import Q


class Benefactor(models.Model):
    # id  = models.AutoField()

    exp_choices = (
        (0, 'beginner'),
        (1, 'average'),
        (2, 'specialist'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default=0, choices=exp_choices)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    # id = models.AutoField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user__username=user.username)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user__username=user.username)

    def all_related_tasks_to_user(self, user):
        return self.filter(Q(charity__user__username=user.username) |
                                   Q(assigned_benefactor__user__username=user.username) |
                                   Q(state='P'))




class Task(models.Model):
    # id = models.AutoField(primary_key=True)

    gender_choice = (
        ('F', 'female'),
        ('M', "male"),
    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(choices=gender_choice, max_length=1, blank=True, null=True)
    
    state_choices = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )

    state = models.CharField(choices=state_choices, default='P', max_length=1)
    title = models.CharField(max_length=60)

    objects = TaskManager()





