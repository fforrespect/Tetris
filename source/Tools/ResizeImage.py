from PIL import Image


def resize_with_aliasing(image_fp: str, target_fp: str) -> None:
    old_image = Image.open(image_fp)
    width, height = old_image.size

    # Resize the image with aliasing using Image.Resampling.NEAREST
    new_image = old_image.resize((width*2, height*2), Image.Resampling.NEAREST)

    # Save the resized image
    new_image.save(target_fp)


resize_with_aliasing("../../Resources/Images/Blocks/blocks.png",
                     "../../Resources/Images/Blocks/blocks.png")
