import json

from flask import Flask, Response, render_template, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect
import prometheus_client

from .forms import GetEmojiForm, SendFeedbackForm, category

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['WTF_CSRF_SECRET_KEY'] = "secret_key"
    app.config['SECRET_KEY'] = "secret_key"

    csrf.init_app(app)

    @app.route('/')
    def landing():
        form = GetEmojiForm()

        categories = [(k, v) for k, v in category.items()]
        default_category = categories[-1]

        return render_template("landing.html.j2", form=form, categories=categories, default_category=default_category)

    @app.route('/request-emoji', methods=['POST'])
    def get_emoji():
        emoji_form = GetEmojiForm()

        if not emoji_form.validate_on_submit():
            print(emoji_form.is_submitted())
            abort(500)

        # Cook Emoji
        emoji = "🐼"

        form = SendFeedbackForm()
        return render_template("emoji.html.j2", form=form, emoji=emoji)

    @app.route('/send-feedback', methods=['POST'])
    def send_feedback():
        form = SendFeedbackForm()

        if not form.validate_on_submit():
            abort(500)

        return redirect(url_for("landing"))

    @app.route('/metrics')
    def metrics_endpoint():
        exposition_text = prometheus_client.generate_latest()

        return Response(exposition_text, content_type=prometheus_client.CONTENT_TYPE_LATEST)

    @app.route('/emojis')
    def show_emoji():
        file = "/home/agustin/CODE/projects/talks/instrumenta/src/vending/data/emoji-test.json"
        print(file)
        with open(file, "rt") as f:
            emoji_data = json.load(f)
        return render_template("show_emoji.html.j2", emoji_data=emoji_data)

    return app
