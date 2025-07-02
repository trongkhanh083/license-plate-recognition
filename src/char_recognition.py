import cv2
import pytesseract
import os

def recognize_plate_text(plate):
    # apply threshold to get black and white effect
    _, thresh = cv2.threshold(plate, 150, 255, cv2.THRESH_BINARY)

    # perform OCR
    config = '--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(thresh, config=config)

    return text.strip()

def main(plate_dir='output/plate'):
    os.makedirs('output/text/', exist_ok=True)

    for img in os.listdir(plate_dir):
        img_path = os.path.join(plate_dir, img)
        img_name = os.path.splitext(img)[0]

        plate = cv2.imread(img_path)

        text = recognize_plate_text(plate)
        if text is None:
            print('Could not find plate text in {img}. Skipping...')
            continue
        else:
            text_dir = os.path.join('output/text', f"{img_name}.txt")
            with open(text_dir, 'w') as f:
                f.write(text + '\n')
        
            print(f"Saved plate text to: {text_dir}")

if __name__=="__main__":
    main()