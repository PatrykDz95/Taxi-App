from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = 'pAssw0rd!'


# new
def create_user(username='user@example.com', password=PASSWORD):
    return get_user_model().objects.create_user(
        username=username, password=password)


class AuthenticationTest(APITestCase):

    # Function collapsed for clarity.
    def test_user_can_sign_up(self): ...

    # new
    def test_user_can_log_in(self):
        user = create_user()
        response = self.client.post(reverse('log_in'), data={
            'username': user.username,
            'password': PASSWORD,
        })
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['username'], user.username)

    # new
    def test_user_can_log_out(self):
        user = create_user()
        self.client.login(username=user.username, password=PASSWORD)
        response = self.client.post(reverse('log_out'))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)