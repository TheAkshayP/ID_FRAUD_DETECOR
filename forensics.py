import numpy as np
from PIL import Image
import io

def error_level_analysis(image):

    original = Image.fromarray(image)

    buffer = io.BytesIO()
    original.save(buffer, "JPEG", quality=90)

    compressed = Image.open(buffer)

    ela = np.abs(np.array(original) - np.array(compressed))
    ela_mean = np.mean(ela)

    # 🔥 More refined thresholds
    if ela_mean > 18:
        return "High Compression Artifacts"
    elif ela_mean > 10:
        return "Moderate Compression Artifacts"
    else:
        return "Normal Compression Pattern"