from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['first_name']) < 3:
            errors.append("First name must be at least 3 letters.")
        if len(form_data['last_name']) < 1:
            errors.append("Last name cannot be empty.")
        if len(form_data['email']) < 1:
            errors.append('Email cannot be empty.')
        return errors
    
    def create_user(self, form_data):
        self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email']
        )

    def update_user(self, form_data, user_id):
        user = self.get(id=user_id)
        
        user.first_name = form_data['first_name']
        user.last_name = form_data['last_name']
        user.email = form_data['email']
        user.save()

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
