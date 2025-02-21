from rest_framework import serializers
from .models import Fund
# Serializers converts queryset and 
# model instances into Python datatypes 
# which will be rendered into JSON/XML
class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        # fields = "__all__"
        fields = ('id', 'name', 
                  'manager_name', 'description', 
                  'nav', 'performance', 
                  'created_at')