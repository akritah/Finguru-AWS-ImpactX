"""Test receipt upload endpoint"""
import requests
import sys

# Test with a simple image
url = "http://localhost:8000/api/receipts/upload"

# Create a dummy image file for testing
test_image = b'\xff\xd8\xff\xe0\x00\x10JFIF'  # Minimal JPEG header

files = {'file': ('test.jpg', test_image, 'image/jpeg')}

try:
    response = requests.post(url, files=files)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
