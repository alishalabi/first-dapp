from rest_framework import serializers

from pizza.models import Pizza, PizzaTopping, Topping


class PizzaToppingSerializer(serlizers.ModelSerializer):

    class Meta:
        model = PizzaTopping
        fields = '__all__'


class PizzaSerializer(serlizers.ModelSerializer):
    toppings = ToppingSerializer(many=True, required=True)

    class Meta:
        model = Pizza
        fields = '__all__'


class ToppingSerializer(serlizers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True, required=True)

    class Meta:
        model = Topping
        fields = '__all__'
