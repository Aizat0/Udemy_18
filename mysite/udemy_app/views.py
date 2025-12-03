from rest_framework import viewsets, generics
from .models import (UserProfile, Category, SubCategory, Course, Lesson, Assignment,
                     Exam, Questions, Option, Certificate, Review, Cart, CartItem)
from .serializers import (UserProfileSerializer, CategorySerializer, SubCategorySerializer, CourseListSerializer, CourseDetailSerializer,
                          LessonListSerializer, LessonDetailSerializer, AssignmentListSerializer, AssignmentDetailSerializer,
                     ExamListSerializer, ExamDetailSerializer, QuestionsListSerializer, QuestionsDetailSerializer,
                          OptionListSerializer, OptionDetailSerializer, CertificateSerializer,
                          ReviewSerializer, CartSerializer, CartItemSerializer)

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


from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ProductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'country']
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'price']


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
