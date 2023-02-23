from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

class Like(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes_sent')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes_received')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

class Match(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='matches_1')
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='matches_2')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='messages_received')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

class Block(models.Model):
    blocker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocks_sent')
    blocked = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocks_received')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocker', 'blocked')

