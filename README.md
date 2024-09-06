# CS50 Forum Platform
#### Video Demo:  <URL https://youtu.be/Vfyrf5ZYnTc>
#### Description:

This is a forum platform built using Django, a Python web framework designed for fast development and clean, pragmatic design. The platform is tailored for users who want to discuss topics related to CS50 courses, allowing them to create, view, and comment on posts. The application supports essential features such as user authentication (register, login, logout), post management, category filtering, and comment threads. Additionally, there is an administrative section where an admin user can manage posts, categories, and comments efficiently.

---

Features:

1. User Authentication:

Registration: New users can sign up by creating an account with a username, email, and password. Django’s built-in authentication system is used to securely store user credentials.

Login: Once registered, users can log in to access their account and post on the forum.

Logout: Users can log out, which will invalidate their session and return them to the homepage.

Dynamic Navigation: The navigation bar includes a login or logout option based on whether the user is authenticated.

2. Post Creation and Management:

Create Posts: Authenticated users can create new posts by providing a title, body, and selecting an appropriate category. These posts serve as discussion starters for various topics related to CS50.

View Posts: All users (authenticated or not) can view posts. Each post includes details such as the author, creation date, associated category, and comments.

Search and Filter: Users can search for posts by title or content. Additionally, they can filter posts by category, allowing for easy navigation of topics.

3. Comment System:

Add Comments: Authenticated users can add comments to any post, fostering discussion and interaction. Each comment is associated with the user who made it and includes a timestamp.

View Comments: Each post page displays a list of comments, allowing users to see the entire thread of discussion in one place.

4. Administrative Management:

Admin Panel: Django’s admin interface allows administrators to manage posts, comments, and categories. This ensures that content on the platform remains appropriate and well-organized.

Post Moderation: Admins can edit or delete posts and comments, ensuring quality control and adherence to community guidelines.

Category Management: Admins can create, edit, and delete categories, helping to organize the discussions into relevant topics.

---

Project Structure and Explanation of Files

The project is divided into several key components:

models.py
This file contains the data models for the application, which define the structure of the data stored in the database.

User: Uses Django's built-in User model for authentication.

Category: Stores different discussion categories. Each post belongs to one category.

Post: Represents individual discussion posts. Each post has a title, body, author, creation date, and belongs to a category.

Comment: Represents comments made on posts. Each comment has an author, body, timestamp, and is linked to a specific post. The models establish relationships between each other using Django’s foreign key fields. For example, a Post is linked to a Category, and a Comment is linked to a Post.