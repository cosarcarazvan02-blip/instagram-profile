class InstagramProfile:
    def __init__(self, username, name, bio, followers, following, posts):
        self.username=username
        self.name=name 
        self.bio=bio 
        self.followers=followers
        self.following=following 
        self.posts=posts


    def display(self):
        print("=== Instagram Profile ===")
        print(f"Username: @{self.username}")
        print(f"Name: {self.name}")
        print(f"Bio: {self.bio}")
        print(f"Posts: {self.posts}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")

    