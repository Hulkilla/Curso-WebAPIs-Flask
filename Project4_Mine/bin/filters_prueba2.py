from PIL import Image, ImageFilter
import io


def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """

    image = Image.open(file) #abre el archivo

    image = image.filter(eval(f"ImageFiler.{filter.upper()}")) #EEvalua el fintro que se le pasa y lo aplica
    
    file = io.BytesIO() #Crea un archivo donde va a guardar la imagen generada

    image.save(file, "JPEG") #lo guarda en formato jpeg
    file.seek(0) #vuelve al principio del archivo para poder leerlo

    return file