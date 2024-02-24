# Import SendinBlue library
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from decouple import config


# Create a SendinBlue API configuration
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = config('vBREVAPI')

# Initialize the SendinBlue API instance
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Define the email sender function
def send_email(html, to_address=None, receiver_username=None):
    
    email_subject = 'Thank you for joining the waitlist!'
    # SendinBlue mailing parameters
    sender = {"name": "Fira", "email": "agentmart100@gmail.com"}

    # Define the recipient(s)
    to = [{"email": to_address, "name": receiver_username}]
    #for multiple recipients
    '''
    if to_address:
        to.append({"email": to_address, "name": receiver_username})
  '''
    # Create a SendSmtpEmail object with the HTML content
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html, sender=sender, subject=email_subject)

    try:
        # Send the email
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
        return {"message": "Email sent successfully!"}
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)