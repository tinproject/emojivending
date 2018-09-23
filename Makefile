

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
	docker-compose up

.PHONY:
down:
	docker-compose down
