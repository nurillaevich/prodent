from .coustompages import CustomPageNumberPagination
from rest_framework import generics
from .models import (Category,
                     Comment,
                     LaveComment,
                     Services,
                     About,
                     Author,
                     Tags,
                     Food,
                     Good,
                     News,
                     OpenHours)
from .serializers import (ServicesSerializer,
                          CommentSerializer,
                          FoodSerializer,
                          NewsSerializer,
                          TagsSerializer,
                          AboutSerializer,
                          GoodsSerializer, AuthorSerializer,
                          OpenHoursSerializer,
                          LaveCommentSerializer,
                          CategorySerializer)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LaveCommentList(generics.CreateAPIView):
    queryset = LaveComment.objects.all()
    serializer_class = LaveCommentSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ServicesList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class GoodList(generics.ListAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodsSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TagList(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class FoodList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        t = self.request.query_params.get('t')
        cat = self.request.query_params.get('cat')
        if t:
            return Food.objects.filter(name__icontains=t)
        if cat:
            return Food.objects.filter(category__title__icontains=cat)
        else:
            return Food.objects.all()


class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    # def post(self, request, *args, **kwargs):
    #     comment = request.data.get('comment')
    #     Food.objects.create(name=comment)


class OpenHoursList(generics.ListAPIView):
    queryset = OpenHours.objects.all()
    serializer_class = OpenHoursSerializer
