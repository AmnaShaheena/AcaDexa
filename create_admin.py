from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if admin already exists
    existing_admin = User.query.filter_by(username='admin').first()
    if existing_admin:
        print("Admin user already exists!")
    else:
        admin = User(
            username='admin',
            email='admin@acadexa.com',
            password=generate_password_hash('admin123'),
            year=4,
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123")