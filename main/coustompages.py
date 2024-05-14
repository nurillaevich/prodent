from rest_framework.pagination import LimitOffsetPagination


class CustomPageNumberPagination(LimitOffsetPagination):
    page_size = 1
    max_page_size = 100
