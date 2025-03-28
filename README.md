# Калькулятор на Python

Простой калькулятор, использующийся в командной строке, запакованный с помощью Docker.

## Особенност
- Базовые операции: `+`, `-`, `*`, `/`
- Поддержка Docker для быстрого развертывания

## Установка

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/hqqqqqqqqqqqqqqqqq/python-calculator.git
cd python-calculator
```

### 2. Локальный запуск (без Docker)
#### Установите зависимости
```bash
pip install -r requirements.txt
```

#### Запустите калькулятор
```bash
python -m app
```

### 3. Запуск с Docker
#### Забилдите image
```bash
docker build -t python-calculator .
```

#### Запустите
```bash
docker run -it python-calculator
```

## ЛИцензия
MIT
