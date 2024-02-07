## resubminting to add doc strings.
class Profile:
    """Class representing a user's profile."""

    def __init__(self, username, password, screen_name, email):
        """to initialize profile instance."""
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email

    def __str__(self):
        """Return a string representation of the Profile."""
        return f"Profile - Username: {self.username}, Screen Name: {self.screen_name}, Email: {self.email}"

    def modify_profile(self, password=None, email=None, screen_name=None):
        """for users to edit profile."""
        if password:
            self.password = password
        if email:
            self.email = email
        if screen_name:
            self.screen_name = screen_name


class Activity:
    """Base class representing an activity."""
    def __init__(self, user, content):
        """TO initialize profiel instance"""
        self.user = user
        self.content = content

    def __str__(self):
        """ Return a string representation of the Activity."""
        return f"Activity - User: {self.user.profile.username}, Content: {self.content}"


class Post(Activity):
    """Class representing a user's post."""
    def __init__(self, user, content):
        """ Initialize a Post instance. """
        super().__init__(user, content)

    def __str__(self):
        """ Return a string representation of the Post. """
        return f"Post - {super().__str__()}"


class Message(Activity):
    """Class representing a user's message to another user."""
    def __init__(self, user, receiver, content):
        """to intialize message instance"""
        super().__init__(user, content)
        self.receiver = receiver

    def __str__(self):
        """ Return a string representation of the Message."""
        return f"Message - {super().__str__()}, Receiver: {self.receiver.profile.username}"


class User:
    """Class representing a user in the social network."""
    def __init__(self, username, password, screen_name, email):
        """user instancess"""
        self.profile = Profile(username, password, screen_name, email)
        self.posts = []
        self.messages = []

    def create_post(self, content):
        """Create a new post for the user.
        Args:
            content (str): The content of the post.

        Returns:
            Post: The created post.

        Raises:
            ValueError: If the content of the post is empty.
        """

        if not content:
            raise ValueError("Content cannot be empty.")
        post = Post(self, content)
        self.posts.append(post)
        return post

    def send_message(self, receiver, content):
        if not receiver or not content:
            raise ValueError("Receiver and Content must have values")
        message = Message(self, receiver, content)
        self.messages.append(message)
        return message

    def __str__(self):
        return f"User - {self.profile}"


# Example usage:
if __name__ == "__main__":
    user1 = User("user1", "password1", "User One", "user1@example.com")
    user2 = User("user2", "password2", "User Two", "user2@example.com")

    post1 = user1.create_post("This is my first post!")
    message1 = user2.send_message(user1, "Hi User One! How are you?")
    print(post1)
    print(message1)

    user1.profile.modify_profile(email="User1_1@uconn.edu")  # Corrected method name
    print(user1)
    print(user2)