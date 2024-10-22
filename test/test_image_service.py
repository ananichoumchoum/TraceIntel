from app.services.image_service import analyze_image

def test_analyze_image():
    result = analyze_image()
    assert result == "Image analysis started."
