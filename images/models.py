from django.db import models
from django.core.exceptions import ValidationError
import opennsfw2 as n2
from PIL import Image as PILImage
import io


def validate_nsfw(field_file):
    try:
        nsfw_probability = n2.predict_image(field_file.file)

        if nsfw_probability > 0.2:
            raise ValidationError("L'image a été détectée comme inappropriée.")
    except Exception as e:
        raise ValidationError(f"Erreur lors de la validation de l'image : {str(e)}")


class Image(models.Model):
    image = models.ImageField(validators=[validate_nsfw])
    is_approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
