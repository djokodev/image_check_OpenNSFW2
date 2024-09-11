import opennsfw2 as n2


image_handle = "imagey1.jpg"

nsfw_probability = n2.predict_image(image_handle)

print(nsfw_probability)