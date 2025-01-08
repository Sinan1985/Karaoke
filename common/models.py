from django.db import models

class Song(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically sets to current time on creation
    user_name = models.CharField(max_length=22, default="Unknown")  # User's name as a plain text field
    # sing_name = models.CharField(max_length=255)  # Song name with a character limit
    sing_name = models.URLField(max_length=2000)
    def __str__(self):
        return f"{self.sing_name} by {self.user_name}"
