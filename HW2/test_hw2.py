import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    pass
    

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    pass

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    pass
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    pass
class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    # Add more test cases for other methods and classes
    
    def setUp(self):
        self.user = User("user1", "password1", "User One", "user1@example.com")

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("testing testing")
        self.assertIn(post, self.user.posts)
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.content, "testing testing")
    
    def test_profile(self):
        """for test and edit user profile"""
        self.user.profile.modify_profile(email="newemail@test.com", screen_name="New screen name")
        self.assertEqual(self.user.profile.email, "newemail@test.com")
        self.assertEqual(self.user.profile.screen_name, "New screen name")

    def test_user_str(self):
        """testing user str represention"""
        expected_str = f"User - Profile - Username: {self.user.profile.username}, Screen Name: {self.user.profile.screen_name}, Email: {self.user.profile.email}"
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()

