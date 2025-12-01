from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    user_name = models.CharField(unique=True)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель'),
    )
    role = models.CharField(max_length=34, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.category_name}'

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subcategory_name}'

class Course(models.Model):
    course_name = models.CharField(max_length=34)
    description = models.TextField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='category_course')
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )
    level = MultiSelectField(max_length=64, choices=LEVEL_CHOICES, null=True, blank=True)
    price = models.PositiveSmallIntegerField()
    created_by = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.course_name}'

class Lesson(models.Model):
    title = models.CharField(max_length=34)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lesson')

    def __str__(self):
        return f'{self.title}'

class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_assignment')
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Exam(models.Model):
    title = models.CharField(max_length=34)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.title}'

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_questions')
    questions_name = models.CharField(max_length=64)
    passing_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.questions_name}'

class Option(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='option_question')
    OPTION_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    option = models.CharField(max_length=12, choices=OPTION_CHOICES)
    bool = models.BooleanField()

    def __str__(self):
        return f'{self.option}'

class Certificate(models.Model):
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.URLField()


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=4)

    def __str__(self):
        return f'{self.cart}, {self.course}'


