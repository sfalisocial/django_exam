from django.db import models
import bcrypt
import re
PASS_REGEX = re.compile(r'[a-zA-Z]')
# Create your models here.
class UserManager(models.Manager):
    def login(self, post):
        user_list = self.filter(username=post['username'])
        if user_list:
            user = user_list[0]
            if bcrypt.hashpw(post['password'].encode(), user.password.encode()) == user.password:
                return user
        return None


    def register(self, post):
        encrypted_password= bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())

        user = self.create(name=post['name'], username=post['username'], password= encrypted_password)


    def validate_user_info(self, post):
        errors = []
        if len(post['name']) == 0:
            errors.append("Name is required")
        elif len(post['name']) < 3:
            errors.append("Name must be at least 2 characters")
        elif not post['name'].isalpha():
            errors.append("Name must consist of letters only")

        if len(post['username']) == 0:
                errors.append("Username is required")
        elif len(post['username']) < 3:
            errors.append("Username must be at least 2 characters")
        elif not post['username'].isalpha():
            errors.append("Username must consist of letters only")

        if len(post['password'])<8:
            errors.append("Error: Password cannot be empty OR less than 8 characters")
        elif not PASS_REGEX.match(post['password']):
            errors.append("Error: Password must contain a letter")
        elif post['password'] != post['passconf']:
            errors.append("Error: Password doesn't match!")

        if len(self.filter(username=post['username'])) > 0:
            errors.append("Username unavailable!")
        return errors
