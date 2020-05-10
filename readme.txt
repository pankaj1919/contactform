In settings.py use this code to configure SMTP Service Provided by Google


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  
EMAIL_HOST_USER = "yourmail@gmail.com"  
EMAIL_HOST_PASSWORD = "yourpassword" 
EMAIL_PORT = 587
EMAIL_USE_TLS = True

