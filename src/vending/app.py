from flask import Flask, Response
import prometheus_client


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/metrics')
    def metrics_endpoint():
        exposition_text = prometheus_client.generate_latest()

        return Response(exposition_text, content_type=prometheus_client.CONTENT_TYPE_LATEST)

    return app
