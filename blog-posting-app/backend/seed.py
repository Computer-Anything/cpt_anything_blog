from app import app, db
from models import User, BlogPost


# Push the application context
with app.app_context():
    # Create a test user
    user = User(username="testuser", email="test@example.com")
    user.set_password("testing")  # Use the set_password method to hash the password
    db.session.add(user)
    db.session.commit()

    # Create a test blog post_1
    post = BlogPost(title="First Post", content="This is a test post.", user_id=user.id)
    db.session.add(post)
    db.session.commit()

    # Create a test blog post_2
    post = BlogPost(title="Second Post", content="This is another test post.", user_id=user.id)
    db.session.add(post)
    db.session.commit()

    print("Database seeded!")
