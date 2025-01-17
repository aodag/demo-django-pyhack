from django.test import TestCase

# Create your tests here.
class HelloTest(TestCase):

    def test_hello(self):
        result = self.client.get("/hello/")
        self.assertEqual(result.context["message"], "Hello, world!")
