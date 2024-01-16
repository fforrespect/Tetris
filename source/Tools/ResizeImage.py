from PIL import Image


def resize_with_aliasing(image_fp: str, target_fp: str) -> None:
    old_image = Image.open(image_fp)
    new_size = tuple(map(lambda x: round(x*.75), old_image.size))

    # Resize the image with aliasing using Image.Resampling.NEAREST
    new_image = old_image.resize(new_size, Image.Resampling.NEAREST)

    # Save the resized image
    new_image.save(target_fp)


resize_with_aliasing("../../Resources/Images/Blocks/Classic/blocks.png",
                     "../../Resources/Images/Blocks/Classic/blocks_new.png")
