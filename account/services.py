from .models import User

def create_new_user(data):
    try:

        return User.objects.create_user(**data,password='bhade')
    except Exception as e:
        return "User not created"