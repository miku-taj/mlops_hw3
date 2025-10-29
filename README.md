# 🎓 Предсказатель оценок (Student Performance Predictor)

Учебный проект, реализованный на **FastAPI**, предназначен для предсказания результатов учащихся по трём предметам:
- **Математика**
- **Чтение**
- **Письмо**

Модель обучена на датасете [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) и использует алгоритм **Random Forest Regressor** из `scikit-learn`.  
API предоставляет простой интерфейс для получения прогнозов на основе демографических и социальных характеристик учащихся (например, *gender*, *race/ethnicity*, *lunch*, *parental level of education* и др.).

---

## ⚙️ Основной стек

- **Python 3.12**
- **FastAPI** — веб-фреймворк для REST API  
- **Uvicorn** — ASGI сервер  
- **Scikit-learn** — машинное обучение  
- **Poetry** — управление зависимостями  
- **Docker** — контейнеризация приложения  

---

## 🧱 Структура проекта

project-root/
│
├── dto/ # Data Transfer Objects (описание входных и выходных данных)
├── encoders/ # Сохранённые энкодеры (LabelEncoder, OneHotEncoder и т.д.)
├── model/ # Папка с функционалом для предсказаний и версиями обученных моделей (.pkl)
├── preprocessing/ # Скрипты предобработки данных
├── main.py # Основной входной файл FastAPI-приложения
├── pyproject.toml # Конфигурация Poetry
├── poetry.lock # Зависимости проекта
└── Dockerfile # Docker-контейнер для развёртывания

## 🚀 Эндпоинты API

| Метод | Путь | Описание |
|-------|------|-----------|
| `GET` | `/` | Базовый маршрут (приветственное сообщение) |
| `GET` | `/health` | Проверка состояния сервера |
| `POST` | `/predict` | Получение предсказаний по входным данным |

**Пример входных данных (`POST /predict`):**
```json
{
  "gender": "female",
  "race_ethnicity": "group B",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "test_preparation_course": "completed"
}

**Запуск через Poetry**
1. Установка и запуск Поетри
```
pip install poetry
poetry install
poetry env activate
```
2. Запуск сервера
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
Сервис будет доступен по адресу: http://localhost:8000/docs

**Запуск через Docker**
1. Собери образ:
```
docker build -t student-predictor .
docker run -d -p 8008:8008 student-predictor
```
