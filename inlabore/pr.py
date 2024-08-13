from PIL import Image

def has_alpha(image):
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        return True
    return False

# Example usage:
img = Image.open('example.png')
if not has_alpha(img):
    # Do something if the image does not have an alpha channel
    print("Image does not have an alpha channel")
else:
    # Do something else if the image has an alpha channel
    print("Image has an alpha channel")
