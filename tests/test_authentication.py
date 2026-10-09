import unittest

from authentication import AuthenticationService


class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        users = {
            "Admin": {"username": "Admin", "password": "admin123"},
            "user1": {"username": "user1", "password": "pass123"},
        }
        self.auth = AuthenticationService(users)

    def test_authenticate_success_with_valid_credentials(self):
        result = self.auth.authenticate("Admin", "admin123")

        self.assertTrue(result)
        self.assertEqual(self.auth.current_user, "Admin")

    def test_authenticate_fails_with_invalid_password(self):
        result = self.auth.authenticate("Admin", "wrong_password")

        self.assertFalse(result)
        self.assertIsNone(self.auth.current_user)

    def test_authenticate_fails_for_unknown_user(self):
        result = self.auth.authenticate("unknown_user", "pass123")

        self.assertFalse(result)
        self.assertIsNone(self.auth.current_user)

    def test_authenticate_raises_for_empty_username(self):
        with self.assertRaises(ValueError):
            self.auth.authenticate("", "admin123")

    def test_authenticate_raises_for_empty_password(self):
        with self.assertRaises(ValueError):
            self.auth.authenticate("Admin", "")

    def test_authenticate_raises_for_empty_username_and_password(self):
        with self.assertRaises(ValueError):
            self.auth.authenticate("", "")

    def test_is_authenticated_returns_true_after_successful_login(self):
        self.auth.authenticate("user1", "pass123")

        self.assertTrue(self.auth.is_authenticated())

    def test_is_authenticated_returns_false_before_login(self):
        self.assertFalse(self.auth.is_authenticated())

    def test_logout_clears_current_user(self):
        self.auth.authenticate("Admin", "admin123")

        self.auth.logout()

        self.assertIsNone(self.auth.current_user)
        self.assertFalse(self.auth.is_authenticated())


if __name__ == "__main__":
    unittest.main()
