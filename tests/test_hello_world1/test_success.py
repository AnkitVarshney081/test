from tests.test_hello_world1 import HelloWorld1LambdaTestCase


class TestSuccess(HelloWorld1LambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

