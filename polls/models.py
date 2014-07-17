from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.

# Poll model
class Poll (models.Model):
    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    
# Choice model
class Choice(models.Model):
    
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text
    
    