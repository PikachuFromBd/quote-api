import requests
import base64

IMG_API_KEY = "1e23ecfe622866a143e2aadbf1ef5a1b"

def fetch_user_info(username: str):
    """Fetch user info from the Telegram username info API."""
    url = f"https://tg-username-info.vercel.app/?username={username}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch user info.")
    data = response.json()
    if "image_url" not in data or "title" not in data:
        raise Exception("Invalid response from user info API.")
    return data

def generate_quote(user_data: dict, text: str, width: int, height: int, format: str, backgroundColor: str):
    """Generate a quote image using the LyoSU API."""
    quote_data = {
        "type": "quote",
        "format": format,
        "backgroundColor": backgroundColor,
        "width": width,
        "height": height,
        "scale": 2,
        "messages": [
            {
                "entities": [],
                "avatar": True,
                "from": {
                    "id": 1,
                    "name": user_data["title"],
                    "photo": {
                        "url": user_data["image_url"]
                    }
                },
                "text": text,
                "replyMessage": {}
            }
        ]
    }
    response = requests.post("https://bot.lyo.su/quote/generate", json=quote_data)
    if response.status_code != 200:
        raise Exception("Failed to generate quote.")
    image_data = base64.b64decode(response.json()["result"]["image"])
    return image_data

def upload_to_imgbb(image_data: bytes):
    """Upload the generated image to ImgBB."""
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMG_API_KEY,
        "image": base64.b64encode(image_data).decode("utf-8")
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception("Failed to upload to ImgBB.")
    data = response.json()
    if "data" not in data or "url" not in data["data"]:
        raise Exception("Invalid response from ImgBB API.")
    return data["data"]["url"]