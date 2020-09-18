from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from api.models import User

class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION", None)

        if auth is None:
            return None
        auth_list = auth.split()

        if not (len(auth_list) == 2 and auth_list[0].lower() == "hello"):
            raise exceptions.APIException("用户认证信息格式有误")

        if auth_list[1] != "cancan":
            raise exceptions.APIException("用户信息校验失败")

        user = User.objects.filter(username="cancan").first()

        if not user:
            raise exceptions.APIException("用户不存在")

        return (user, None)
