from django.db import models

# Create your models here.
class Workout(models.Model):
    workout_name=models.CharField(max_length=30)
    class Meta:
        db_table='workout_list'
    def __str__(self):
        return self.workout_name
    

class ExercisedBody(models.Model):
    body_part=models.CharField(max_length=30)
    workout=models.ForeignKey(Workout, on_delete = models.CASCADE)
    class Meta:
        db_table='exercised_part'
    def __str__(self):
        return self.body_part

class Post(models.Model):
    #username = models.ForeignKey(User, on_delete=models.CASCADE)#
    Reps = models.IntegerField(default=0)
    perReps= models.IntegerField(default=0)
    content = models.CharField(max_length=4000)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Workout, on_delete=models.SET_NULL, blank=True, null=True)
    deloading = models.BooleanField(default=False)
    RPE=models.IntegerField(default=0)
    RIR=models.IntegerField(default=0)

    def __str__(self):
        return self.category.workout_name

class Static(models.Model):
    Number=models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.Number

