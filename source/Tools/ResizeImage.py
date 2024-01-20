from PIL import Image


def resize(image_fp: str, target_fp: str, factor: float, anti_aliasing: bool = False) -> None:
    old_image = Image.open(image_fp)
    new_size = tuple[int, int](map(lambda x: round(x*factor), old_image.size))

    # Resize the image with aliasing using Image.Resampling.NEAREST
    resample = Image.Resampling.LANCZOS if anti_aliasing else Image.Resampling.NEAREST
    new_image = old_image.resize(new_size, resample)

    # Save the resized image
    new_image.save(target_fp)


resize("/Users/jaiveer/Downloads/smile.png",
       "/Users/jaiveer/Downloads/smile.png",
       0.5,
       False)
