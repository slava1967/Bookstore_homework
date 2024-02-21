## Запуск приложения
```
flask --app bookstore run
```

## Выбираем хранилище:

### Хранилище в памяти:

#### В файле context.py строку 8 определяем:
```
book_storage = MemoryStorage()
```

### Хранилище в SQLite:

#### В файле context.py строку 8 определяем:
```
book_storage = SQLiteStorage()
```

## cURL тестирование

### получение списка книг
```
curl -s "http://localhost:5000/books/"
```

### добавление новых книг
```
curl http://localhost:5000/books/ -X POST -H 'Content-Type: application/json' -d '{"title": "thebook", "created_at": "2023-01-01", "description": "a book", "publish_year": 2023, "pages_count": 100}'
```
```
curl http://localhost:5000/books/ -X POST -H 'Content-Type: application/json' -d '{"title": "thebook2", "created_at": "2023-03-15", "description": "another book", "publish_year": 2024, "pages_count": 150}'
```

### удаление книги по идентификатору / ID == 1
```
curl -X DELETE "http://localhost:5000/books/1"
```
