from rest_framework import serializers
from .models import WaitlistEntry
import phonenumbers
from phonenumbers import NumberParseException


class WaitlistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistEntry
        fields = ['email','FirstName','LastName', 'phone', 'id']
        
        
        # Validate the phone number
        
    def validate_phone(self, value):
        try:
            parsed_phone = phonenumbers.parse(str(value), None)
            if not phonenumbers.is_valid_number(parsed_phone) or parsed_phone.country_code != 1:
                raise serializers.ValidationError("Invalid phone number. Please provide a valid US number.")
        except NumberParseException:
            raise serializers.ValidationError("Invalid phone number. Please provide a valid US number.")

        return value

    def validate(self, data):
        # Call the parent class's validation method
        super().validate(data)
    
        return data
        
    
