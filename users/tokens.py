
from datetime import timedelta
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)
    refresh.access_token.set_exp(lifetime=timedelta(days=10))

    tokens = {"access": str(refresh.access_token), "refresh": str(refresh), "expireAt":str(refresh.lifetime)}
    print(str(refresh.lifetime))
    return tokens