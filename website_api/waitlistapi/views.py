from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import WaitlistEntry
from .serializers import WaitlistEntrySerializer
from .mailer import send_email 
import os
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

class Waitlist(generics.ListAPIView):
    queryset = WaitlistEntry.objects.all()
    serializer_class = WaitlistEntrySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
# view for the waitlist entry serializer it takes both post and get requests
class WaitlistEntryView(generics.CreateAPIView):
    queryset = WaitlistEntry.objects.all()
    serializer_class = WaitlistEntrySerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().create(request, *args, **kwargs)
        
        # Use the created instance to access the validated data
        validated_data = serializer.validated_data

        # Retrieve the email from serializer data
        email = validated_data.get('email', None)
        name = validated_data.get('FirstName', None)

        if email:
            # Read HTML content from the template file
            template_file_path = os.path.join(os.path.dirname(__file__), 'mailertemplate.html')
            with open(template_file_path, 'r') as file:
                email_message = file.read()

            # Replace placeholders in the template with dynamic data
            email_message = email_message.replace('{{name}}', name)
        
            try:
                send_email(email_message, email, name)
                
                # If email sending is successful, include a success message in the response
                return Response({'message': 'created', 'email_sent': True}, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                # Handle email sending failure here
                return Response({'error': 'Failed to send email', 'email_sent': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # If no email is provided, respond with a simple created message
        return Response({'message': 'created', 'email_sent': False}, status=status.HTTP_201_CREATED)
    
   
