from rest_framework import serializers
from watchlist_app.models import Movie

# validators
def validate_description(value):
    if len(value)>100:
        raise serializers.ValidationError('Description is too long!')
    return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description cannot be the same!')
        return data

    # field level validation
    def validate_name(self, value):
        if len(value)<3:
            raise serializers.ValidationError('Name is too short!')
        return value


# Scratch Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(required=False, allow_blank=True, validators=[validate_description])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description cannot be the same!')
#         return data

#     # field level validation
#     def validate_name(self, value):
#         if len(value)<3:
#             raise serializers.ValidationError('Name is too short!')
#         return value