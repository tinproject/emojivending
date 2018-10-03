# Instrumenta tu app con Prometheus

## Vending Machine

Para ejecutar el proyecto se necesita: `make`, `docker`, y `docker-compose`.

Ejecuta `make setup-volumes` para crear los directorios necesarios para persistir datos.

Para ejecutar la aplicación haz `make run`, o `make run-debug` para lanzarla en modo debug.


La app expone los siguientes puertos para acceder a los servicios:

- Vending app: [http://localhost:8080]
- Grafana: [http://localhost:3000]
- Prometheus: [http://localhost:9090]
- Node-Exporter: [http://localhost:9100]
- Locust: [http://localhost:8089]
