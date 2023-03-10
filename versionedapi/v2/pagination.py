from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_query_param = "page_size"
    max_page_size = 2000

class SimplePagination(PageNumberPagination):
    page_size = 1000
    page_query_param = "page_size"
    max_page_size = 2000