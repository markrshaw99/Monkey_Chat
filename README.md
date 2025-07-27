## Monkey Chat - Live Chat Application
Deployed on Heroku: https://realtime-chatplication-9c6d5893bbc8.herokuapp.com/

Monkey Chat is a real-time chat application built with Django and Django Channels. It supports public and private group chats, user profiles, and live online status updates. The app is designed for deployment on Heroku and uses modern cloud services for media and real-time features.

### Features
- Real-time group chat with WebSockets (Django Channels)
- Public and private chat rooms
- User authentication and profile management
- Live online user status
- Media uploads with Cloudinary
- Responsive UI with Tailwind CSS and Alpine.js
- HTMX for dynamic, AJAX-powered UI updates

### Tech Stack
- Django 5.x
- Django Channels & Redis (for WebSockets)
- Daphne (ASGI server for real-time features)
- PostgreSQL (via Heroku Postgres)
- Cloudinary (media storage)
- HTMX & Alpine.js (frontend interactivity)
- Tailwind CSS (styling)
- Heroku (deployment)

### Setup
1. Clone the repo and install dependencies from `requirements.txt`.
2. Create a `.env` file (see `.env.template`) with your secrets and service URLs.
3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Deployment
This project is ready for Heroku deployment. Set your config vars for `DATABASE_URL`, `REDISCLOUD_URL`, `CLOUDINARY_URL`, and other secrets in the Heroku dashboard.

Repo: [markrshaw99/Monkey_Chat](https://github.com/markrshaw99/Monkey_Chat)