import random
from django.utils import timezone

def generate_client_id():
    number = random.randint(1,9999)
    return 'ID{}{}{}'.format(timezone.now().strftime('%y%m%d'), number, "01")

def generate_entity_id():
    number = random.randint(1,9999)
    return 'ID{}{}{}'.format(timezone.now().strftime('%y%m%d'), number, "02")

def generate_department_id():
    number = random.randint(1,9999)
    return 'ID{}{}{}'.format(timezone.now().strftime('%y%m%d'), number, "03")
