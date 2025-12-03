from rest_framework import serializers
from .models import (UserProfile, Category, SubCategory, Course, Lesson, Assignment,
                     Exam, Questions, Option, Certificate, Review, Cart, CartItem)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'price']

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url']

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content', 'course']


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']

class CourseDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y')
    category_course = CourseListSerializer(read_only=True, many=True)
    course_lesson = LessonListSerializer(many=True, read_only=True)
    course_assignment = AssignmentListSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level', 'price',
                  'created_by', 'created_at', 'updated_at', 'category_course',
                  'course_lesson', 'course_assignment']



class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title']


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['questions_name']

class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option']


class OptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['questions', 'option', 'bool']


class QuestionsDetailSerializer(serializers.ModelSerializer):
    option_question = OptionListSerializer(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = ['exam', 'questions_name', 'passing_score', 'option_question']



class ExamDetailSerializer(serializers.ModelSerializer):
    exam_questions = QuestionsListSerializer(many=True, read_only=True)
    class Meta:
        model = Exam
        fields = ['title', 'course', 'duration', 'exam_questions']



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Certificate
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'