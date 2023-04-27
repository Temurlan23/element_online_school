from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone: str, password: str = None):
        if not phone:
            raise ValueError('Users must have a phone')
        user = self.model(
           phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password) -> None:
        user = self.create_user(
            phone,
            password=password
        )
        user.is_active = True
        user.save(using=self._db)