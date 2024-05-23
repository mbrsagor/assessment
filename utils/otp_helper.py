import random
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


# Generate password when user create account
def generate_otp(length=6):
    otp_chars = "0123456789"
    otp = ''.join(random.choice(otp_chars) for _ in range(length))
    return otp


# When signUp will done send OTP the user given email address
def send_otp(email, otp):
    template_name = 'email/email_otp.html'
    subject = 'Verification OTP'
    message = f'Your OTP for email verification is: {otp}. Please use this OTP to verify your email.'
    context = {'email': email, 'otp': otp}
    template = get_template(template_name).render(context)
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    send_mail(subject, message, from_email, to_email, html_message=template, fail_silently=False)
