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
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "testing testing")
    
    def test_profile(self):
        """for test and edit user profile"""
        self.user.profile.profile_edit(email="newemail@test.com", screen_name="New screen name")
        self.assertEqual(self.user.profile.email, "newemail@test.com")
        self.assertEqual(self.user.profile.screen_name, "New screen name")

    def test_user_str(self):
        """testing user str represention"""
        expected_str = "User - Profile - Username: user, Screen Name: User One, Email: user1@example.com"
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()

