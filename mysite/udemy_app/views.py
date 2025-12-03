from tokenize import TokenError
from drf_yasg.openapi import Response
from rest_framework import viewsets, generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import (UserProfile, Category, SubCategory, Course, Lesson, Assignment,
                     Exam, Questions, Option, Certificate, Review, Cart, CartItem)
from .serializers import (UserProfileSerializer, CategorySerializer, SubCategorySerializer, CourseListSerializer,
                          CourseDetailSerializer,
                          LessonListSerializer, LessonDetailSerializer, AssignmentListSerializer,
                          AssignmentDetailSerializer,
                          ExamListSerializer, ExamDetailSerializer, QuestionsListSerializer, QuestionsDetailSerializer,
                          OptionListSerializer, OptionDetailSerializer, CertificateSerializer,
                          ReviewSerializer, CartSerializer, CartItemSerializer, CourseCreateSerializer, UserSerializer,
                          LoginSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'detail': 'Недействительный токен.'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course_name', 'category']
    search_fields = ['course_name', 'category', 'created_by']
    ordering_fields = ['price']

class CourseCreateViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer

class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer

class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer

class QuestionsListAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsListSerializer

class QuestionsDetailAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailSerializer

class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionListSerializer

class OptionDetailAPIView(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionDetailSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer



from rest_framework import viewsets, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ["movie_name", "director__name", "actor__name"]
    ordering_fields = ["year", "movie_name"]


from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
    ...
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
