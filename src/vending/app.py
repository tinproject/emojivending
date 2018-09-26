from flask import Flask, Response, render_template, redirect, url_for
import prometheus_client


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def landing():

        return render_template("landing.html.j2")

    @app.route('/request-emoji', methods=['POST', 'GET'])
    def get_emoji():

        return render_template("emoji.html.j2")

    @app.route('/send-feedback', methods=['POST', 'GET'])
    def send_feedback():

        return redirect(url_for('landing'))

    @app.route('/metrics')
    def metrics_endpoint():
        exposition_text = prometheus_client.generate_latest()

        return Response(exposition_text, content_type=prometheus_client.CONTENT_TYPE_LATEST)

    return app
