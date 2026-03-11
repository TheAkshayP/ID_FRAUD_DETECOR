def validate_image(image):

    height, width = image.shape[:2]

    if height < 300 or width < 300:
        return "Low Resolution Image"

    return "Valid Image"