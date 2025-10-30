from flask import Flask, render_template, redirect, url_for
from forms import FeedbackForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

FEEDBACK_FILE = "feedbacks.json"

#  ფაილიდან წაკითხვა
def load_feedbacks():
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # თუ ფაილი არ არსებობს, ვაბრუნებთ ცარიელ სიას
        return []
    except json.JSONDecodeError:
        # თუ ფაილი დაზიანებულია ან ცარიელია
        return []

# Helper – შენახვა
def save_feedbacks(feedbacks):
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(feedbacks, f, ensure_ascii=False, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback_data = {
            "name": form.name.data,
            "email": form.email.data,
            "message": form.message.data,
            "type": form.feedback_type.data
        }

        feedbacks = load_feedbacks()
        feedbacks.append(feedback_data)
        save_feedbacks(feedbacks)

        return redirect(url_for("all_feedbacks"))

    return render_template("feedback.html", form=form)

@app.route("/all_feedbacks")
def all_feedbacks():
    feedbacks = load_feedbacks()
    return render_template("all_feedbacks.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
