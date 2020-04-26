from rest_framework import serializers
from myapi.models import Users

class UsersSerializers(serializers.ModelSerializer):
    name =serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)
    age = serializers.IntegerField(required=False)
    photo = serializers.ImageField(required=False)
    resume = serializers.ImageField(required=False)
    class Meta:
        model = Users
        fields : '__all__'
        exclude = []
        #fields = ('name','employee_id','age','ranking','photo','resume')

