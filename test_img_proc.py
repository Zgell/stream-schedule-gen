from images.image_processor import ImageProcessor

from PIL import Image

if __name__ == '__main__':
    processor = ImageProcessor()
    img = processor.generate_schedule()
    img.show()