from .models import Transactions, Slot
import random
import string

def add_to_Transactions():
    choices= ["BTC", "ETH"]
    currency= random.choice(choices)

    if currency== "BTC":
        pre_choices= ["bc", "1", "3"]
        pre= random.choice(pre_choices)
        characters= string.ascii_lowercase + string.digits
        wallet= "".join(random.choice(characters) for _ in range(13))
        address= pre+wallet
        
    else:
        pre= "0x"
        characters= string.digits + string.ascii_lowercase
        wallet= "".join(random.choice(characters) for _ in range(13))
        address= pre+wallet
        
    deposit= random.uniform(0, 0.9)
    received= deposit * 2
    
    new_transaction= Transactions(
            Address= address,
            Deposit= deposit,
            Received= received,
            Currency= currency,
        )
    new_transaction.save()

    available_slots = Slot.objects.all()
    available_slots.slots -= 1
    available_slots.save()