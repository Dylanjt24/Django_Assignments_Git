from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(form_data['first_name']) < 2:
            errors.append('First name must be at least 2 characters.')
        elif not form_data['first_name'].isalpha():
            errors.append('First name must include only letters.')
        if len(form_data['last_name']) < 2:
            errors.append('Last name must be at least 2 characters.')
        elif not form_data['last_name'].isalpha():
            errors.append('Last name must include only letters.')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('Email is invalid.')
        if len(form_data['password']) < 8:
            errors.append('Password must be at least 8 characters.')
        if form_data['confirm_pw'] != form_data['password']:
            errors.append('Passwords must match.')
        
        existing_users = self.filter(email=form_data['email'])
        if existing_users:
            errors.append('Email already in use.')
        return errors

    def create_user(self, form_data):
        pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            pw_hash=pw_hash
        )

    def validate_login(self, form_data):
        errors = []

        user = self.get(email=form_data['email'])
        if user:
            if not bcrypt.checkpw(form_data['password'].encode(), user.pw_hash.encode()):
                errors.append('Sorry, email or password were incorrect.')
                return errors
        else:
            errors.append('Sorry, email or password were incorrect, sir.')
            return errors

class MessageManager(models.Manager):
    def create_message(self, form_data, user_id):
        user = User.objects.get(id=user_id)
        self.create(
            message=form_data['message'],
            message_creator=user
        )

class CommentManager(models.Manager):
    def create_comment(self, form_data, user_id):
        message = Message.objects.get(id=form_data['message_id'])
        user = User.objects.get(id=user_id)
        self.create(
            comment=form_data['comment'],
            parent_message=message,
            comment_creator=user
        )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    message_creator = models.ForeignKey(User, related_name="created_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    parent_message = models.ForeignKey(Message, related_name="attached_comments")
    comment_creator = models.ForeignKey(User, related_name="created_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()