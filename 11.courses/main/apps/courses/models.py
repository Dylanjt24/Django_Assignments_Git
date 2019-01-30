from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['name']) < 6:
            errors.append("Name must be morethan 5 characters.")
        if len(form_data['description']) < 16:
            errors.append("Description must be more than 15 characters.")
        return errors
    
    def create_course(self, form_data):
        self.create(
            name=form_data['name'],
            description=form_data['description']
        )

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()