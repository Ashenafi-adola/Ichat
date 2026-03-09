from rest_framework.serializers import ModelSerializer

from . models import FriendMessage

class FriendMessageSerialize(ModelSerializer):
    class Meta:
        model = FriendMessage
        fields = "__all__"