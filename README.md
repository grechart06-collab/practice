# Инструкция по запуску

**Требования:**
- Python 3.12 или выше

### Шаги

1. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   ```

2. **Активируйте виртуальное окружение:**

   Windows:
   ```bash
   venv\Scripts\activate
   ```

   Linux / macOS:
   ```bash
   source venv/bin/activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```

5. **Откройте сайт в браузере:**

   http://127.0.0.1:8000/

6. **Админка:**

   http://127.0.0.1:8000/admin/

   Данные для входа: используйте логин и пароль, указанные при создании администратора.
