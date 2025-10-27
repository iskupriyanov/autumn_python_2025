#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app'
}

with open('config_default.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
new_lines = []
for line in lines:
    if '=' in line and '?' in line:
        option = line.split('=')[0].strip()
        if option in config_values:
            value = config_values[option]
            # Приводим значение к строке и добавляем кавычки если нужно
            line = f"{option} = {value}\n"
    new_lines.append(line)

print(''.join(new_lines))


