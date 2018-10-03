from flask import Flask, Response, render_template, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect
import prometheus_client

from .emoji import categories, get_random_category, request_emoji
from .forms import GetEmojiForm, SendFeedbackForm

csrf = CSRFProtect()

# Metrics definition
vending_emoji_front_watched_counter = prometheus_client.Counter(
    "vending_emoji_front_watched_total",
    "Vending machine emoji watched.",
    [])
venging_emoji_requested_counter = prometheus_client.Counter(
    "vending_emoji_requested_total",
    "Requested emoji.",
    ["category_id", "category_name"])
venging_emoji_delivered_counter = prometheus_client.Counter(
    "vending_emoji_delivered_total",
    "Delivered emoji.",
    ["category_id", "category_name"])
venging_emoji_feedback_received_counter = prometheus_client.Counter(
    "vending_emoji_feedback_received_total",
    "Number of feedback received for emoji.",
    ["feedback"])
vending_emoji_overall_satisfaction_index_gauge = prometheus_client.Gauge(
    "vending_emoji_overall_satisfaction_index",
    "Client overall satisfaction index",
    [])


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['WTF_CSRF_SECRET_KEY'] = "secret_key"
    app.config['SECRET_KEY'] = "secret_key"

    # disable csrf to allow locust traffic
    app.config['WTF_CSRF_ENABLED'] = False

    csrf.init_app(app)

    @app.route('/metrics')
    def metrics_endpoint():
        exposition_text = prometheus_client.generate_latest()

        return Response(exposition_text, content_type=prometheus_client.CONTENT_TYPE_LATEST)

    @app.route('/')
    def landing():
        form = GetEmojiForm()

        vending_emoji_front_watched_counter.inc()

        # Choose a random category as default
        default_category = get_random_category()

        return render_template("landing.html.j2", form=form, categories=categories, default_category=default_category)

    @app.route('/request-emoji', methods=['POST'])
    def get_emoji():
        emoji_form = GetEmojiForm()

        if not emoji_form.validate_on_submit():
            print(emoji_form.is_submitted())
            abort(500)

        category_id = emoji_form.category.data
        category_name = categories[category_id]["name"]

        venging_emoji_requested_counter.labels(category_id=category_id, category_name=category_name).inc()

        # Cook Emoji
        emoji = request_emoji(category_id)

        venging_emoji_delivered_counter.labels(category_id=category_id, category_name=category_name).inc()

        form = SendFeedbackForm()
        return render_template("give_emoji.html.j2", form=form, emoji=emoji)

    @app.route('/send-feedback', methods=['POST'])
    def send_feedback():
        form = SendFeedbackForm()

        if not form.validate_on_submit():
            abort(500)

        feedback = form.feedback.data

        if feedback == "yes":
            venging_emoji_feedback_received_counter.labels(feedback=feedback).inc()
            vending_emoji_overall_satisfaction_index_gauge.inc()
        elif feedback == "no":
            venging_emoji_feedback_received_counter.labels(feedback=feedback).inc()
            vending_emoji_overall_satisfaction_index_gauge.dec()
        else:
            raise ValueError("Not a valid feedback response")

        return redirect(url_for("landing"))

    @app.route('/emojis')
    def show_emoji():
        return render_template("show_emoji.html.j2", emoji_data=categories)

    return app
