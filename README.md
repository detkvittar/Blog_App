Flask Blog Application
Overview

A Flask-based web application as a simple blog platform where users can add, update, delete, and like blog posts. The application uses a JSON file (blog_posts.json) as a simple database to store blog posts.

Requirements

    Python 3
    Flask
    A modern web browser

Installation

    Clone the repository or download the source code.
    Install Flask using pip:

    pip install Flask

File Structure

    app.py: The main Python file with Flask routes.
    blog_posts.json: JSON file acting as a simple database for blog posts.
    templates/: Folder containing HTML templates.
        add.html: Template for adding a new blog post.
        index.html: Template for the blog's homepage, displaying all posts.
        update.html: Template for updating an existing blog post.
    static/: Folder containing static files.
        style.css: CSS file for basic styling.

Usage

    Run the Flask application:

    python app.py

    Access the application in a web browser at http://0.0.0.0:5000.

Features

    Home Page (/): Displays all blog posts with options to like, update, or delete each post.
    Add New Post (/add): A form to submit a new blog post.
    Update Post (/update/<int:post_id>): Update the details of an existing post.
    Delete Post (/delete/<int:post_id>): Delete a specific blog post.
    Like Post (/like/<int:post_id>): Increment the like count for a specific post.

API Endpoints

    GET /: Home page, lists all posts.
    GET /add: Form to add a new post.
    POST /add: Endpoint to submit a new post.
    GET /update/<int:post_id>: Form to update an existing post.
    POST /update/<int:post_id>: Endpoint to submit updated post details.
    GET /delete/<int:post_id>: Endpoint to delete a post.
    GET /like/<int:post_id>: Endpoint to like a post.

Notes

    The application uses JSON to store data, which is not suitable for production use due to scalability and concurrency issues.
    The application lacks user authentication and is intended for learning purposes!

License

This project is licensed under the MIT License.

MIT License

Copyright (c) [2023] [Emilia Malmqvist]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
