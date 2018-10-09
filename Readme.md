# Emoji Vending Machine

This repository is a companion part of my talk **"[Instrumenta tu app con Prometheus](https://speakerdeck.com/tinproject/instrumenta-tu-app-con-prometheus-pycones-2018)"** at PyConES 2018.

It has the code exposed on the talk, and it's also a playground to poke with Grafana and Prometheus metrics.


## Run the project

To run this project you need: `make`, `docker`, & `docker-compose`.

Run `make setup` to create local folders for docker volumes and to download fonts and emoji data.

To run the project you could do one of the following:
- `make up` will start the project in background.
- `make run` will start the project in foregroung, dumping docker-compose logs to stdout.
- `make run-debug` will start the project in debug mode, dumping docker-compose logs to stdout.

Once you run the project, this endpoints will be exposed on your local machine:
- EmojiVending app: [http://localhost:8080](http://localhost:8080)
- Grafana: [http://localhost:3000](http://localhost:3000)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Node-Exporter: [http://localhost:9100](http://localhost:9100)
- Locust: [http://localhost:8089](http://localhost:8089)

To stop the containers of the project, just run `make down`.


## Play

Play with the project, you can:
- Take a look at the EmojiVending app and get some emojis. 
- Then you can take a look at the Prometheus Graph explorer and Grafana. 
- Run the preconfigured locust job to simulate traffic and take a look back at Grafana dashboard.
- Take a look at Node-Exporter exported metrics.
- Tweak Gafana dashboards or create new ones.

