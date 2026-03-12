def validate_image(image):

    h, w = image.shape[:2]

    if h < 300 or w < 300:
        return "Low Resolution Image"

    return "Valid Image"