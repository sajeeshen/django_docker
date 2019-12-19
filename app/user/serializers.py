from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """ Serializers for User model """

    def validate_password(self, value):
        """ Validate the password """
        if value.isalnum():
            raise serializers.ValidationError('password must have atleast one special character.')
        return value

    # def to_internal_value(self, data):
    #     """ Serializer should work even if the object is not correct """
    #     user_data = data['user']
    #     return super().to_internal_value(user_data)

    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError("first_name and last_name shouldn't be same.")
        return data

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',
                    'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """ Create a new user with encrypted password and return """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ Update a user setting the password correctely and return it """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for user Authentication """
    email = serializers.CharField()
    password = serializers.CharField(
                    style={'input_type': 'password'},
                    trim_whitespace=False
                )

    def validate(self, attrs):
        """ Validate and authenticate user """
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            email = email,
            password = password
        )

        if not user:
            msg = _('Unable to authenticate the provided credentials')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs