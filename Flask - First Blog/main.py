from flask import Flask, render_template
from post import Post


app = Flask(__name__)


@app.route('/')
def home_page():
    my_tool = Post()
    blog_list = my_tool.get_info()
    blog_length = len(blog_list)
    return render_template("index.html", my_blog=blog_list, my_length=blog_length)


@app.route('/blog/<int:number>')
def post_page(number):
    my_tool = Post()
    blog_list = my_tool.get_info()[int(number) - 1]
    return render_template("post.html", my_blog=blog_list)


if __name__ == "__main__":
    app.run(debug=True)
