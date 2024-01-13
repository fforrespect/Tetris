from PIL import Image


def resize_with_aliasing(image_fp: str, target_fp: str) -> None:
    old_image = Image.open(image_fp)
    width, height = old_image.size

    # Resize the image with aliasing using Image.Resampling.NEAREST
    new_image = old_image.resize((width*2, height*2), Image.Resampling.NEAREST)

    # Save the resized image
    new_image.save(target_fp)


for i in range(10):
    resize_with_aliasing(f"../../Resources/Fonts/{i}.png", f"../../Resources/Fonts/{i}.png")
