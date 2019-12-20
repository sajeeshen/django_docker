from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields 
from core.models import Article


article_index = Index('articles')
article_index.settings (
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=['standard', 'lowercase', 'stop', 'snowball'],
    char_filter = ["html_strip"]
)

@article_index.doc_type
class ArticleDocument(Document):
    """ Article elasticsearch document """
    id = fields.IntegerField(attr='id')
    title = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword')
        }
    )
    body = fields.StringField(
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword')
        }
    )
    created = fields.DateField()
    updated = fields.DateField()
    pub_date = fields.DateField()

    class Django:
        model = Article