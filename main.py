from profile import InstagramProfile

def main():
    print("Enter the data:\n")

    username = input("Username: ")
    name = input("Name: ")
    bio = input("Bio: ")

    posts = int(input("Posts: "))
    followers = int(input("Followers: "))
    following = int(input("Following: "))

    profile = InstagramProfile(username, name, bio, followers, following, posts)
    print()
    profile.display()
main()
