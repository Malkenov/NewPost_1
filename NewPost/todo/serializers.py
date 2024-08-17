from rest_framework import serializers
from .models import Post,User



class PostSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = "__all__"


class CreateNewUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.save()
        return user