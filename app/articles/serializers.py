from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import ArticleDocument


class ArticleDocumentSerializer(DocumentSerializer):
    """ Serializer from Article Elastic search engine """

    class Meta:
        document = ArticleDocument
        fields = (
            'id',
            'title',
            'body',
            'author',
            'created',
            'modified',
            'pub_date',
        )  