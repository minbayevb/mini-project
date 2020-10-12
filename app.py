from flask import Flask, render_template, url_for, request

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
app=Flask(__name__, template_folder= "templates")


subscribers = []

@app.route('/')
def index():
    title = "Minbayev Bolatbek's Blog"
    return render_template("index.html", title=title, posts= posts), url_for('index')

@app.route('/about')
def about():
    title = "About Bolatbek Minbayev!"
    return render_template("about.html", title = title), url_for('about')

@app.route('/subscribe')
def subscribe():
    title = "Subscribe to my Blog"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name= request.form.get("first_name")
    last_name= request.form.get("last_name")
    email = request.form.get("email")

    conditions = [first_name, last_name, email]
    if any(conditions) and not all(conditions) :
        error_statement = "All Form Fields Required..."
        return render_template('subscribe.html', error_statement= error_statement,
        first_name =first_name, last_name=last_name, email=email) 
    
    subscribers.append(f"{first_name} {last_name} | {email}")
    title = "Thank you!"
    return render_template("form.html", title=title, subscribers=subscribers)

if __name__ == "__main__":
    app.run(debug=True)