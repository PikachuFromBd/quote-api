from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from app.dependencies import validate_key
from app.utils import fetch_user_info, generate_quote, upload_to_imgbb

app = FastAPI()

@app.get("/")
async def api_details():
    """Root endpoint providing API details."""
    return JSONResponse({
        "API": "Quote Generator API",
        "Description": "Generate quotes for Telegram messages with ease.",
        "Endpoints": {
            "/": "API details (this endpoint)",
            "/create": "Generate quotes (parameters: username, text, width, height, format, backgroundColor, key)",
            "/docs": "API documentation"
        },
        "Dev": "pikachufrombd.t.me"
    })

@app.get("/create")
async def create_quote(
    username: str = Query(..., description="Telegram username."),
    text: str = Query(..., description="Text for the quote."),
    width: int = Query(512, description="Width of the quote image."),
    height: int = Query(768, description="Height of the quote image."),
    format: str = Query("webp", description="Output format of the quote image (e.g., webp, png)."),
    backgroundColor: str = Query("#FFFFFF", description="Background color of the quote (e.g., #000000)."),
    key: str = Query(None, description="Security key (required for restricted usernames).")
):
    """
    Generate a quote for the specified Telegram username.
    """
    try:
        # Validate the security key if necessary
        validate_key(username, key)

        # Fetch user info
        user_data = fetch_user_info(username)

        # Generate the quote
        image_data = generate_quote(user_data, text, width, height, format, backgroundColor)

        # Upload the image to ImgBB
        image_url = upload_to_imgbb(image_data)

        # Return the result
        return {
            "message": "Quote generated and uploaded successfully.",
            "image_url": image_url,
            "Dev": "pikachufrombd.t.me"
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
