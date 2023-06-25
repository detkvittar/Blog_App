import json
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    with open('blog_posts.json', 'r') as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Load the data from the json file
        try:
            with open('blog_posts.json', 'r') as f:
                blog_posts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            blog_posts = []

        # Generate the next ID by incrementing the ID of the last post
        next_id = blog_posts[-1]['id'] + 1 if blog_posts else 1

        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        if not author or not title or not content:
            # One or more fields are empty
            return "Error: All fields are required", 400

        new_post = {
            "id": next_id,
            "author": author,
            "title": title,
            "content": content
        }
        blog_posts.append(new_post)

        # Write the data back to the json file
        with open('blog_posts.json', 'w') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    try:
        # Load the data from the json file
        with open('blog_posts.json', 'r') as f:
            blog_posts = json.load(f)

        # Find the blog post with the given id
        post_to_delete = next((post for post in blog_posts if post['id'] == post_id), None)
        if post_to_delete is None:
            abort(404)  # If the post isn't found, return a 404 error

        # Remove the post from the list
        blog_posts.remove(post_to_delete)

        # Write the data back to the json file
        with open('blog_posts.json', 'w') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))
    except (FileNotFoundError, json.JSONDecodeError):
        abort(500)  # If there's an error loading the file, return a 500 error


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    with open('blog_posts.json', 'r') as f:
        blog_posts = json.load(f)

    post_to_update = next((post for post in blog_posts if post['id'] == post_id), None)
    if post_to_update is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        post_to_update['author'] = request.form.get('author')
        post_to_update['title'] = request.form.get('title')
        post_to_update['content'] = request.form.get('content')

        with open('blog_posts.json', 'w') as f:
            json.dump(blog_posts, f)

        return redirect(url_for('index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post_to_update)


@app.route('/like/<int:post_id>')
def like(post_id):
    # Load the data from the json file
    with open('blog_posts.json', 'r') as f:
        blog_posts = json.load(f)

    # Find the post with the given id
    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] += 1
            break
    else:
        return "Post not found", 404

    # Write the data back to the json file
    with open('blog_posts.json', 'w') as f:
        json.dump(blog_posts, f)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
