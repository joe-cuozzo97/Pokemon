from django.db import models
from django.urls import reverse



MOVES = (
    ('T', 'Tackle'),
    ('S', 'Scratch'),
    ('B','Bite'),
)



# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()

   
    
    def __str__(self):
        return self.name
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})


class Attack(models.Model):
    levelLearned= models.IntegerField()
    move= models.CharField(
        max_length=100,
            choices=MOVES,
            default=MOVES[0][0]
    )
    
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)  
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_move_display()} on {self.levelLearned}"

   