"""
This module defines several views for handling CRUD operations on Article and Author models.
"""

import json
from marshmallow import ValidationError
from django.views.generic import View
from techtest.articles.models import Article, Author
from techtest.articles.schemas import ArticleSchema, AuthorSchema
from techtest.utils import json_response


class ArticlesListView(View):
    """
    View class for handling GET and POST requests on the article list endpoint.
    """

    def get(self, request, *args, **kwargs):
        """
        Get a list of all articles.
        Returns:
            JSON response with a list of articles serialized as JSON objects.
        """
        return json_response(ArticleSchema().dump(Article.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        """
        Create a new article.
        Args:
            request: Django HTTP request object.
        Returns:
            JSON response with the new article serialized as a JSON object.
        """
        try:
            article = ArticleSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(ArticleSchema().dump(article), 201)


class ArticleView(View):
    """
    View class for handling GET, PUT, and DELETE requests on a specific article endpoint.
    """

    def dispatch(self, request, article_id, *args, **kwargs):
        """
        Get the article object associated with the given article ID and set it as a class attribute.
        Args:
            request: Django HTTP request object.
            article_id: ID of the article to retrieve.
        Returns:
            Superclass method dispatch.
        """
        try:
            self.article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            return json_response({"error": "No Article matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.article.id)
        return super(ArticleView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Get the article object associated with this view.
        Returns:
            JSON response with the article serialized as a JSON object.
        """
        return json_response(ArticleSchema().dump(self.article))

    def put(self, request, *args, **kwargs):
        """
        Update the article object associated with this view.
        Args:
            request: Django HTTP request object.
        Returns:
            JSON response with the updated article serialized as a JSON object.
        """
        try:
            article = ArticleSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(ArticleSchema().dump(article))

    def delete(self, request, *args, **kwargs):
        """
        Delete the article object associated with this view.
        Returns:
            JSON response with a success message.
        """
        self.article.delete()
        return json_response({"message": "Article successfully deleted."})


class AuthorsListView(View):
    """
    View class for handling GET and POST requests on the author list endpoint.
    """

    def get(self, request, *args, **kwargs):
        """
        Get a list of all authors.
        Returns:
            JSON response with a list of authors serialized as JSON objects.
        """
        return json_response(AuthorSchema().dump(Author.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        """
        Create a new author.
        Args:
            request: Django HTTP request object.
        Returns:
            JSON response with the new author serialized as a JSON object.
        """
        try:
            author, created = AuthorSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(author), 201)


class AuthorView(View):
    """
    View class for handling GET, PUT, and DELETE requests on a specific author endpoint.
    """

    def dispatch(self, request, author_id, *args, **kwargs):
        """
        Get the author object associated with the given author ID and set it as a class attribute.
        Args:
            request: Django HTTP request object.
            author_id: ID of the author to retrieve.
        Returns:
            Superclass method dispatch.
        """
        try:
            self.author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return json_response({"error": "No Author matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.author.id)
        return super(AuthorView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Get the author object associated with this view.
        Returns:
            JSON response with the author serialized as a JSON object.
        """
        return json_response(AuthorSchema().dump(self.author))

    def put(self, request, *args, **kwargs):
        """
        Update the author object associated with this view.
        Args:
            request: Django HTTP request object.
        Returns:
            JSON response with the updated author serialized as a JSON object.
        """
        try:
            author, _ = AuthorSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(author))

    def delete(self, request, *args, **kwargs):
        """
        Delete the author object associated with this view.
        Returns:
            JSON response with a success message.
        """
        self.author.delete()
        return json_response({"message": "Author successfully deleted."})