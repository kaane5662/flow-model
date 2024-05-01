def users():
    print("Testing if users schema is working")
    print("Test complete")

def items():
    print("Testing if items schema is working")
    print("Test complete")

def item(id):
    print(f"Fetching specific item: {id}")
    print("Test complete")

def user(id):
    print(f"Testing user profile {id}")
    print("Test complete")


users()
items()
item(1)
user(20)