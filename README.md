**SANTIAGO ESCUDERO**

# CircleCi

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-santiescu/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-santiescu/tree/main)

# Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/8e3f4167b71acbdc9b75/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-santiescu/maintainability)

# Test Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/8e3f4167b71acbdc9b75/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-santiescu/test_coverage)

## Jugar

### Para jugar Local

Clonar el repo

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-santiescu.git
```

Instalar requirements

```bash
pip install -r requirements.txt
```

Correr el juego

```bash
python3 -m game.cli
```

### Jugar con Docker

Instalar docker para Debian

```bash
sudo apt install docker
```

Crear la imagen de Dcoker:

```bash
docker buildx build -t ajedrez-2024-santiescu .
```

Jugar con los test

```bash
docker run -i /ajedrez-2024-santiescu .
```
