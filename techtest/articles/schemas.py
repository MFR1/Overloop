from marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load

from techtest.articles.models import Article, Author
from techtest.regions.models import Region
from techtest.regions.schemas import RegionSchema


class AuthorSchema(Schema):
    """Schema for Author model"""

    class Meta(object):
        """Metadata for AuthorSchema"""
        model = Author

    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()

    @post_load
    def make_author(self, data, **kwargs):
        """Create or update Author object and return it"""
        author, created = Author.objects.update_or_create(id=data.get('id'), defaults=data)
        return author, created


class ArticleSchema(Schema):
    """Schema for Article model"""

    class Meta(object):
        """Metadata for ArticleSchema"""

        model = Article

    id = fields.Integer()
    title = fields.String(validate=validate.Length(max=255))
    content = fields.String()
    author = fields.Integer(load_only=True, required=False)
    regions = fields.Method(
        required=False, serialize="get_regions", deserialize="load_regions"
    )

    def get_regions(self, article):
        """Return serialized list of region objects for given article"""
        return RegionSchema().dump(article.regions.all(), many=True)

    def load_regions(self, regions):
        """Get or create Region objects from given serialized data"""
        return [
            Region.objects.get_or_create(id=region.pop("id", None), defaults=region)[0]
            for region in regions
        ]

    @classmethod
    def load_author(cls, value):
        """Load Author object for given id"""
        return Author.objects.get(id=value)

    @post_load
    def update_or_create(self, data, *args, **kwargs):
        """Create or update Article object with given data and return it"""
        author_id = data.pop("author", None)
        regions = data.pop("regions", None)
        article, _ = Article.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )

        # Set regions if provided
        if isinstance(regions, list):
            article.regions.set(regions)

        # Set author if provided
        if author_id is not None:
            article.author = self.load_author(author_id)
            article.save()

        # Return updated or created Article object
        return article

