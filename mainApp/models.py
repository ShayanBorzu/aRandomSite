from django.db import models

# Create your models here.
class Contact(models.Model):
    """Model for storing contact form submissions"""
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(
        max_length=25, 
        blank=True, 
        default='',  
        verbose_name="Phone Number"
    )
    subject = models.CharField(
        max_length=25, 
        verbose_name="Subject"
    )
    message = models.TextField(verbose_name="Message")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent At")
    is_read = models.BooleanField(default=False, verbose_name="Read Status")
    
    class Meta:
        ordering = ['-sent_at'] 
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        indexes = [
            models.Index(fields=['-sent_at']),
            models.Index(fields=['is_read']),
        ]
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"
