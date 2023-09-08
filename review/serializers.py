from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField #(чтобы не указывать автора)
from .models import Like, Dislike, Comment, Rating, Favorites

class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context.get('request').user
        # print('===============')
        print(user)
        # print('===============')
        comment = Comment.objects.create(author=user, **validated_data)
        return comment
    
class RatingSerializer(ModelSerializer):
    
    author = ReadOnlyField(source = 'author.email')
    
    class Meta:
        model = Rating
        fields = '__all__'
     
    def validate_rating(self, rating):
        if rating in range (1, 6):
            return rating
        raise ValidationError('рейтинг должен быть от 1 до 5')
        
    def validate_product(self, product):
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(product=product, author=user).exists():
            raise ValidationError(
                'Вы уже оставляли отзыв на данный продукт')
        return product
    
    # def update(self, instance, validated_data):
    #     instance.rating = validated_data.get('rating')
    #     instance.save()
    #     return super().update(instance, validated_data)
    
    def create(self, validated_data):
        user = self.context.get('request').user #для получения user
        return self.Meta.model.objects.create(author=user, **validated_data)
     
class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')
    product = ReadOnlyField()
    
    class Meta:
        model = Like
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)
    
class DislikeSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')
    product = ReadOnlyField()
    
    class Meta:
        model = Dislike
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)
    
class FavoritsSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')
    product = ReadOnlyField()
    
    class Meta:
        model = Favorites
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)