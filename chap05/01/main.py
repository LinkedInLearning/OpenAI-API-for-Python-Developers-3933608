from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="中世のヨーロッパの風景",  # A text description of the desired image(s)
  size="1024x1024", # Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models
  quality="standard", # Defaults to standard, hd creates images with finer details and greater consistency across the image. 
  n=1, # For dall-e-3, only n=1 is supported.
)

image_url = response.data[0].url
print(image_url)