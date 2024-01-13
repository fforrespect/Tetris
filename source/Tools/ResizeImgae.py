from PIL import Image


def resize_with_anti_aliasing(image_fp: str) -> None:
    old_image = Image.open(image_fp)
    width, height = old_image.size

    # Resize the image with anti-aliasing using Image.Resampling.LANCZOS
    new_image = old_image.resize((width*2, height*2), Image.Resampling.LANCZOS)

    # Save the resized image
    new_image.save("../../Resources/Images/resized_image.png")


resize_with_anti_aliasing("../../Resources/Images/game_board_original.png")
