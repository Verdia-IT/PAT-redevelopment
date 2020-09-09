from rest_framework import serializers



class LightingHourDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    scenario_id = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True)
    scenario_name = serializers.StringRelatedField(many=False, read_only=True)
    lighting_type = serializers.CharField(max_length=25)
    monday_lighting_hour_1_start = serializers.CharField(max_length=15)
    monday_lighting_hour_1_end = serializers.CharField(max_length=15)
    monday_lighting_hour_2_start = serializers.CharField(max_length=15)
    monday_lighting_hour_2_end = serializers.CharField(max_length=15)
    tuesday_lighting_hour_1_start = serializers.CharField(max_length=15)
    tuesday_lighting_hour_1_end = serializers.CharField(max_length=15)
    tuesday_lighting_hour_2_start = serializers.CharField(max_length=15)
    tuesday_lighting_hour_2_end = serializers.CharField(max_length=15)
    wednesday_lighting_hour_1_start = serializers.CharField(max_length=15)
    wednesday_lighting_hour_1_end = serializers.CharField(max_length=15)
    wednesday_lighting_hour_2_start = serializers.CharField(max_length=15)
    wednesday_lighting_hour_2_end = serializers.CharField(max_length=15)
    thursday_lighting_hour_1_start = serializers.CharField(max_length=15)
    thursday_lighting_hour_1_end = serializers.CharField(max_length=15)
    thursday_lighting_hour_2_start = serializers.CharField(max_length=15)
    thursday_lighting_hour_2_end = serializers.CharField(max_length=15)
    friday_lighting_hour_1_start = serializers.CharField(max_length=15)
    friday_lighting_hour_1_end = serializers.CharField(max_length=15)
    friday_lighting_hour_2_start = serializers.CharField(max_length=15)
    friday_lighting_hour_2_end = serializers.CharField(max_length=15)
    saturday_lighting_hour_1_start = serializers.CharField(max_length=15)
    saturday_lighting_hour_1_end = serializers.CharField(max_length=15)
    saturday_lighting_hour_2_start = serializers.CharField(max_length=15)
    saturday_lighting_hour_2_end = serializers.CharField(max_length=15)
    sunday_lighting_hour_1_start = serializers.CharField(max_length=15)
    sunday_lighting_hour_1_end = serializers.CharField(max_length=15)
    sunday_lighting_hour_2_start = serializers.CharField(max_length=15)
    sunday_lighting_hour_2_end = serializers.CharField(max_length=15)


class LightingInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    scenario_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    scenario_name = serializers.StringRelatedField(many=False, read_only=True)
    area = serializers.CharField(max_length=50)
    lighting_type_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    lighting_type = serializers.SlugRelatedField(many=False, read_only=True, slug_field='lighting_type')
    number_of_existing_luminaire = serializers.IntegerField()
    existing_luminaire_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    existing_luminaire = serializers.StringRelatedField(many=False, read_only=True)
    existing_luminaire_power = serializers.DecimalField(max_digits=8,decimal_places=1)
    number_of_replaced_luminaire = serializers.IntegerField()
    replacement_luminaire_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    replacement_luminaire = serializers.StringRelatedField(many=False, read_only=True)
    replacement_luminaire_power = serializers.DecimalField(max_digits=8,decimal_places=1)
    power_reduction = serializers.DecimalField(max_digits=10,decimal_places=2)
    estimated_operating_hours = serializers.IntegerField()
    total_estimated_savings_kwhs = serializers.DecimalField(max_digits=10, decimal_places=2)
    veec_discount = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    esc_discount = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    discount_adjustment = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    total_discount = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    maintenance_savings = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    dollar_per_fixture = serializers.DecimalField(max_digits=10,decimal_places=2)
    labour_per_hour = serializers.DecimalField(max_digits=10,decimal_places=2)
    fixtures_per_hour = serializers.IntegerField()
    total_cost = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    led_life_in_months = serializers.IntegerField()
    existing_lamp_replacement_costs = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    existing_luminaire_life_in_months = serializers.IntegerField()
    

class LightingOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    scenario_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    scenario_name = serializers.StringRelatedField(many=False, read_only=True)
    number_of_lights = serializers.IntegerField()
    maintenance_savings = serializers.DecimalField(max_digits=10, decimal_places=2)
    power_reduction = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_discount = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    installation_cost = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    other_adjustments_1 = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    verdia_fee = serializers.DecimalField(max_digits=5 ,decimal_places=2)
    verdia_fee_dollars = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    other_adjustments_2 = serializers.DecimalField(max_digits=10 ,decimal_places=2)
    total_cost = serializers.DecimalField(max_digits=10 ,decimal_places=2)  