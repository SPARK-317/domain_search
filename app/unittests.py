import unittest
import application

class AppTests(unittest.TestCase):
  
  # setUp test server
  def setUp(self):
    application.app.testing = True
    self.app = application.app.test_client()

  def test_home(self):
    result = self.app.get("/")
    self.assertIn("Whois domain search", str(result.data), "Index page should load")

  # test empty search
  def test_empty_search(self):
    result = self.app.get("/search?domain=")
    self.assertIn("Invalid domain name", str(result.data), "Empty search should throw error")

  # test invalid search
  def test_invalid_domain(self):
    array = ["google", "YOUTUBE.foo", "cadosecurity.co.uk", "TRAVELCOLOR.CO.UK"]

    for i in array:
      result = self.app.get(f"/search?domain={i}")
      self.assertTrue(i.lower() or i.upper() not in str(result.data), "Invalid domain should throw error")

  # test valid search
  def test_valid_domain(self):
    array = ["google.com", "YOUTUBE.com", "cadosecurity.com", "TRAVELCOLOUR.CO.UK"]

    for i in array:
      result = self.app.get(f"/search?domain={i}")
      self.assertTrue(i.lower() or i.upper() in str(result.data), f"Valid domain should display Whois info for {i}")

if __name__=="__main__":
  unittest.main()