from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'inpute_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['email','date_of_birth','name','password','password2']

        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2:
            raise serializers.ValidationError("pass1 and pass2 didn't match")

        return attrs

    def  create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UseLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=225)
    class Meta:
        model=User
        fields=['email','password']
