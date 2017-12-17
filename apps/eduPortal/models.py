from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

# Create your models here.
# Name_regex = re.compile(r'^[a-zA-Z]\w+$')
emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = []
        if len(postData['name']) < 3:
            errors.append('Name cannot be fewer than 3 characters')
        email = self.filter(email=postData['email'])
        if len(email):
            errors.append("email already used")
        if not emailRegex.match(postData["email"]):
            errors.append("Enter a valid email") 
        if len(postData['password']) < 5:
            errors.append('Password should be atleast 5 characters long')
        if not (postData['password'] == postData['confirm_password']):
            errors.append('Passwords do not match')
        if not errors:
            hashing = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(10))
            user = User.objects.create(
                name=postData['name'],
                email=postData['email'],
                password=hashing,
                role=postData['role'],
            )
            return user
        return errors
    
    def validate_login(self, postData):
        errors = []
        email = self.filter(email=postData['email'])
        if len(email):
            if bcrypt.checkpw(postData['password'].encode(),email[0].password.encode()):
                return email[0]
            else:
                errors.append("Incorrect Password")
                return errors
        else:
            errors.append("Incorrect Email")
            return errors

    def getUser(self):
        print "inside database, before call, dashboard two"
        users = self.filter()
        print "inside database, dashboard two", users
        return users

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    topics = [models.CharField(max_length=255)]
    time = {
        "sunday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "monday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "tuesday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "wednesday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "thursday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "friday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]],
        "saturday" : [[models.CharField(max_length=255), models.CharField(max_length=255)]]
    }
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()