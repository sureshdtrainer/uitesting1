class AuthenticationService:
    def __init__(self, users=None):
        self._users = users or {}
        self.current_user = None

    def authenticate(self, username, password):
        if not username or not password:
            raise ValueError("Username and password are required.")

        user = self._users.get(username)
        if user is None:
            return False

        if user.get("password") != password:
            return False

        self.current_user = username
        return True

    def logout(self):
        self.current_user = None

    def is_authenticated(self):
        return self.current_user is not None
