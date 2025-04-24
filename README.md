# 📶 Wi-Fi QR Generator (Windows EXE)

Графическое десктоп-приложение для генерации QR-кодов подключения к Wi-Fi.  
Работает как самостоятельное окно (без браузера), сохраняет историю и не требует установки Python.

---

## ⚙️ Технологии

- **Python 3.10+**
- **Flask** — серверная логика
- **PyWebView** — нативное окно вместо браузера
- **QRCode** — генерация QR-кодов
- **Pillow** — изображение в памяти
- **SQLite** — сохранение истории генераций
- **PyInstaller** — сборка в `.exe`

---

## 🖥 Что делает приложение

- Генерирует QR-код для подключения к Wi-Fi по SSID и паролю
- Показывает последний QR-код сразу после генерации
- Сохраняет историю всех сгенерированных кодов
- Позволяет просматривать историю в интерфейсе
- Работает как обычное Windows-приложение (`.exe`)

---

## 🚀 Как использовать

### 📥 Скачать

1. Перейди в раздел [Releases]([https://github.com/Snapsli/Wi-Fi-QR-Generator/releases/tag/v1.2)])
2. Скачай архив.
3. Запусти файл wifi_qr_gui_delete.exe в папке /dist

### ▶️ Запуск

Просто дважды кликни по `wifi_qr_gui_delete.exe`.  
Откроется окно с простым интерфейсом.

---

## 📁 Файлы проекта

Если ты разработчик и хочешь собрать `.exe` самостоятельно:

```bash
pip install flask qrcode pillow pywebview pyinstaller
pyinstaller wifi_qr_gui_delete.spec

📂 Получившийся .exe будет в папке dist/


# 📶 Wi-Fi QR Generator (Windows EXE)

A graphical desktop application for generating QR codes for connecting to Wi-Fi.  
It works as an independent window (without a browser), saves the history and does not require Python installation.

---

## ⚙️ Technologies

- **Python 3.10+**
- **Flask** — server logic
- **PyWebView** — native window instead of browser
- **QRcode** — QR code generation
- **Pillow** — image in memory
- **SQLite** — saving generation history
- **PyInstaller** — build in `.exe`

---

## 🖥 What does the app do

- Generates a QR code for connecting to Wi-Fi by SSID and password
- Shows the last QR code immediately after generation
- Saves the history of all generated codes
- Allows you to view the history in the interface
- Works like a regular Windows application ('.exe`)

---

## 🚀 How to use

### 📥 Download

1. Go to the [Releases] section([https://github.com/Snapsli/Wi-Fi-QR-Generator/releases/tag/v1.2)])
2. Download archive `wifi_qr_gui_delete.zip `
3. Launch the file wifi_qr_gui_delete.exe in the /dist folder

### ▶️ Launch

Just double-click on `wifi_qr_gui_delete.exe `.  
A window with a simple interface will open.

---

## 📁 Project files

If you are a developer and want to build the `.exe` yourself:

```bash
pip install flask qrcode pillow pywebview pyinstaller
pyinstaller wifi_qr_gui_delete.spec

The resulting one .the exe will be in the dist folder/
