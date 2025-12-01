from django.urls import include, path
from rest_framework import routers
from .views import (UserProfileViewSet, CategoryViewSet, SubCategoryViewSet, CourseListAPIView,
                    CourseDetailAPIView, LessonListAPIView, LessonDetailAPIView, AssignmentListAPIView, AssignmentDetailAPIView,
                     ExamListAPIView, ExamDetailAPIView, QuestionsListAPIView, QuestionsDetailAPIView,
                    OptionListAPIView, OptionDetailAPIView, CertificateViewSet,
                    ReviewViewSet, CartViewSet, CartItemViewSet)


router = routers.SimpleRouter()
router.register(r'user_profile', UserProfileViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'sub_category', SubCategoryViewSet)
router.register(r'certificate', CertificateViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart_item', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
    path('exam/', ExamListAPIView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
    path('questions/', QuestionsListAPIView.as_view(), name='questions-list'),
    path('questions/<int:pk>/', QuestionsDetailAPIView.as_view(), name='questions-detail'),
    path('option/', OptionListAPIView.as_view(), name='option-list'),
    path('option/<int:pk>/', OptionDetailAPIView.as_view(), name='option-detail'),
]