from django.db import models

class CoursesManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors["name"] = "Name should be more than 5 characters"
        if len(postData['description']) <= 15:
            errors["description"] = "Description should be more than 15 characters"
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()

    def __repr__(self):
        return f"Courses: {self.id}, {self.name}, {self.description}"