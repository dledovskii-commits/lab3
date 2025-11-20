# Lab 3 - Fibonacci CI/CD

Лабораторная работа по настройке CI/CD пайплайна.

## Структура
- `src/fibs.py` - функция Фибоначчи
- `src/test.py` - тесты
- GitHub Actions - автоматическое тестирование

## Локальный запуск тестов
```bash
pip install -r requirements.txt
python -m pytest src/ -v