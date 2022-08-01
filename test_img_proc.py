from images.image_processor import ImageProcessor

from PIL import Image
import sys

if __name__ == '__main__':
    processor = ImageProcessor()
    img = processor.generate_schedule()
    img.show()
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'save':
            img.save('images/temp/test_img_proc.png')