import json

# Открываем JSON-файл для чтения
with open("sample-data.json", "r") as file:
    # Загружаем JSON-данные
    json_data = json.load(file)

# Выводим структуру JSON-данных
print(json.dumps(json_data, indent=2))
