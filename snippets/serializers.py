from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

class OrderStatusSerializer(serializers.Serializer):
    orderId = serializers.CharField(max_length=100)
    statusId = serializers.CharField(max_length=100)


class WorkEffortsSerializer(serializers.Serializer):
        workEffortTypeId = serializers.CharField(max_length=100)
        workEffortName = serializers.CharField(max_length=200)
        workEffortId = serializers.CharField(max_length=100)
        scopeEnumId = serializers.CharField(max_length=100)
        locationDesc = serializers.CharField(max_length=500)
        lastUpdatedTxStamp = serializers.DateTimeField
        lastUpdatedStamp = serializers.DateTimeField
        lastStatusUpdate = serializers.DateTimeField
        estimatedCompletionDate = serializers.DateTimeField
        description = serializers.CharField(max_length=500)
        createdStamp = serializers.DateTimeField
        createdTxStamp = serializers.DateTimeField
        currentStatusId = serializers.CharField(max_length=100)

