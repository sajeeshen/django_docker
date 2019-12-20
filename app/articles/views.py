from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer


class ArticleViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer
 
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
 
    # Define search fields
    search_fields = (
        'title',
        'body',
    )
 
    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title.raw',
        'body': 'body.raw',
        'author': {
            'field': 'author_id',
            'lookups': [
                LOOKUP_QUERY_IN,
            ]
        },
        'created': 'created',
        'updated': 'updated',
        'pub_date': 'pub_date',
    }
 
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'author': 'author_id',
        'created': 'created',
        'updated': 'updated',
        'pub_date': 'pub_date',
    }

    # Specify default ordering
    ordering = ('id', 'created',) 