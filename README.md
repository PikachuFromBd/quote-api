# Pika Quote API 💬

![API Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)
![Vercel](https://img.shields.io/badge/Hosted_on-Vercel-black?style=for-the-badge&logo=vercel)
![FastAPI](https://img.shields.io/badge/Built_with-FastAPI-blue?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)
![Requests](https://img.shields.io/badge/Library-Requests-orange?style=for-the-badge)
![Docs](https://img.shields.io/badge/Interactive-Docs-green?style=for-the-badge&logo=swagger)

---

## 📖 **Introduction**

**Pika Quote API** is a feature-rich API for generating high-quality quote images for Telegram messages. With customizable options such as text, dimensions, background color, and format, this API is designed for developers and Telegram bot creators.

---

## 🚀 **Base URL**

The API is hosted at:  
**[https://pika-quote-api.vercel.app](https://pika-quote-api.vercel.app)**

---

## 📚 **Endpoints**

### 1. **Root Endpoint** (`/`)
Provides basic information about the API and its usage.

#### **Request**
```bash
GET https://pika-quote-api.vercel.app/
```

#### **Response**
```json
{
  "API": "Quote Generator API",
  "Description": "Generate quotes for Telegram messages with ease.",
  "Endpoints": {
    "/": "API details (this endpoint)",
    "/create": "Generate quotes (parameters: username, text, width, height, format, backgroundColor, key)",
    "/docs": "API documentation"
  },
  "Dev": "pikachufrombd.t.me"
}
```

---

### 2. **Create Quote** (`/create`)

Generates a quote image for a given Telegram username and text with optional customization.

#### **Request**
```bash
GET https://pika-quote-api.vercel.app/create
```

#### **Parameters**

| Parameter         | Type     | Description                                               | Required | Default       |
|--------------------|----------|-----------------------------------------------------------|----------|---------------|
| **username**       | `string` | Telegram username of the user for whom the quote is created | Yes      | `None`        |
| **text**           | `string` | The text to display in the quote                          | Yes      | `None`        |
| **width**          | `int`    | Width of the generated image in pixels                   | No       | `512`         |
| **height**         | `int`    | Height of the generated image in pixels                  | No       | `768`         |
| **format**         | `string` | Format of the image (e.g., `webp`, `png`)                | No       | `webp`        |
| **backgroundColor**| `string` | Background color of the image (e.g., `#FFFFFF`)          | No       | `#FFFFFF`     |
| **key**            | `string` | Security key for restricted usernames                    | No       | `None`        |

#### **Example Request**
```bash
GET https://pika-quote-api.vercel.app/create?username=shahad4t&text=Hello&width=600&height=800&format=png&backgroundColor=%23000000
```

#### **Response**
```json
{
  "message": "Quote generated and uploaded successfully.",
  "image_url": "https://i.ibb.co/8syYc9s/88522eea4573.png",
  "Dev": "pikachufrombd.t.me"
}
```

---

### 3. **Docs Endpoint** (`/docs`)

Access the interactive API documentation powered by FastAPI and Swagger.

#### **Request**
```bash
GET https://pika-quote-api.vercel.app/docs
```

#### **Features**:
- Visual representation of all endpoints.
- Detailed parameter descriptions.
- Ability to test API calls directly from the browser.

---

## 🎨 **Customization Options**

1. **Text and User Information**:
   - Display a message and the user’s profile image in the generated quote.

2. **Image Dimensions**:
   - Adjust the `width` and `height` to fit your design requirements.

3. **Background Color**:
   - Use the `backgroundColor` parameter to set custom colors (e.g., `#000000` for black).

4. **Image Format**:
   - Choose between `webp`, `png`, or other supported formats for the generated image.

5. **Security**:
   - Restricted usernames require a valid `key` to create quotes.

---

## ⚙️ **Technology Stack**

- **Language**: ![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
- **Framework**: ![FastAPI](https://img.shields.io/badge/FastAPI-High_Performance-blue?style=for-the-badge&logo=fastapi)
- **Libraries**:
  - `requests`: For API communication
  - `base64`: For image encoding and decoding

---

## 💻 **Example Integrations**

### **Python Integration**
```python
import requests

url = "https://pika-quote-api.vercel.app/create"
params = {
    "username": "shahad4t",
    "text": "Hello World!",
    "width": 600,
    "height": 800,
    "format": "png",
    "backgroundColor": "#000000"
}
response = requests.get(url, params=params)
print(response.json())
```

### **cURL Example**
```bash
curl -X GET "https://pika-quote-api.vercel.app/create?username=shahad4t&text=Hello&width=600&height=800&format=png&backgroundColor=%23000000"
```

---

## 🛠️ **Development**

1. Clone the repository:
   ```bash
  git clone https://github.com/PikachuFromBd/quote-api.git
   cd pika-quote-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Deploy to Vercel:
   ```bash
   vercel deploy
   ```

---

## 👨‍💻 **Author**

[![Shahadat Hassan](https://img.shields.io/badge/Telegram-Shahadat_Hassan-blue?style=for-the-badge&logo=telegram)](https://pikachufrombd.t.me)

---
