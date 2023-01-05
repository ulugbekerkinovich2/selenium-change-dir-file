from rest_framework import serializers

from basic_app.models import My


class MySerializers(serializers.ModelSerializer):
    class Meta:
        model = My
        fields = '__all__'

    # def create(self, validated_data):
    #     return self.validated_data and my_selen()
