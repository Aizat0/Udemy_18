from .models import (UserProfile, Category, Course, Lesson,
                     Assignment, Exam, Questions, Review, SubCategory)
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('user_name', 'bio')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('questions_name',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)