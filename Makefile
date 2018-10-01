

.PHONY:
setup-volumes:
	mkdir -p .volumes/prometheus
	chmod 777 .volumes/prometheus
	mkdir -p .volumes/grafana/data
	chmod 777 .volumes/grafana/data

.PHONY:
prom-check-config:
	docker-compose run --entrypoint=promtool --rm prometheus check config /etc/prometheus/prometheus.yml

.PHONY:
up:
	docker-compose up -d

.PHONY:
down:
	docker-compose down

.PHONY:
run:
	docker-compose up

.PHONY:
run-debug:
	FLASK_DEBUG=1 docker-compose up



# Get resources
./emoji/emoji-test.txt:
	wget https://unicode.org/Public/emoji/11.0/emoji-test.txt -O ./emoji/emoji-test.txt

./src/vending/data/emoji-test.json: ./emoji/emoji-test.txt
	python ./emoji/parse_emoji.py
	mv ./emoji/emoji-test.json ./src/vending/data/emoji-test.json

.PHONY:
get-emoji-data: ./src/vending/data/emoji-test.json

./src/vending/static/NotoColorEmoji.ttf:
	wget https://github.com/googlei18n/noto-emoji/raw/master/fonts/NotoColorEmoji.ttf -O ./src/vending/static/NotoColorEmoji.ttf

.PHONY:
get-statics: ./src/vending/static/NotoColorEmoji.ttf

.PHONY:
setup: get-emoji-data get-statics
