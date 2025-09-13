from .models import Block
import random
import string

def create_block(data):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return Block.objects.create(**data,code=code)