from django.db import models

class Variant(models.Model):
    #question_id = models.ForeignKey(Question, default=False)
    var_text = models.CharField(max_length=60, default=False)

    def __unicode__(self):
        return self.var_text

class Question(models.Model):
    #survey_id = models.ForeignKey(Survey, default=False)
    q_text = models.TextField(default=False)
    answers_number = models.IntegerField(default=1)
    variants = models.ForeignKey(Variant, default=False)

    def __unicode__(self):
        return self.q_text

class Survey(models.Model):
    name = models.CharField(max_length=40, unique=True, default=False)
    author = models.CharField(max_length=20, default='Admin')
    date_published = models.DateTimeField(auto_now_add=True)
    questions = models.ForeignKey(Question, default=False)

    def __unicode__(self):
        return self.name


class Respondent(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    name = models.CharField(max_length=20, default='Anonimus')
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

    def __unicode__(self):
        return '%s %s' %(self.name, self.last_name)


class Result(models.Model):
    pass

class Answer(models.Model):
    pass