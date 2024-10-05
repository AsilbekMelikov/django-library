from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book
import re

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, attrs):
        title = attrs['title']
        isbn = attrs['isbn']

        if not re.match(r'^[a-zA-Z0-9 ]*$', title) or title.isdigit():
            raise ValidationError({
                "status": False,
                "message": f"Book title {title} must include only letters or a combination of letters and numbers"
            })
        if not isbn.isdigit():
            raise ValidationError({
                "status": False,
                "message": f"Book isbn {isbn} must include digits"
            })

        if Book.objects.filter(isbn=isbn):
            raise ValidationError({
                "status": False,
                "message": f"A book with the ISBN '{isbn}' already exists."
            })

        return attrs

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError({
                "status": False,
                "message": f"A book {price} is not valid."
            })