import cv2
import os

def preprocess_image(img_path):
    if isinstance(img_path, str):
        img = cv2.imread(img_path)
    else:
        img = img_path.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # reduce noise
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # edge detection
    edged = cv2.Canny(gray, 170, 200)

    return img, gray, edged

def find_license_plate(gray, edged):
    contour, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # sort contour by area and keep the largest one
    contour = sorted(contour, key=cv2.contourArea, reverse=True)[:30]

    plate_contour = None
    plate = None

    for c in contour:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

        # look for contour with 4 corners
        if len(approx) >= 4:
            plate_contour = approx
            # crop the license plate region
            x, y, w, h = cv2.boundingRect(c)
            plate = gray[y:y+h, x:x+w]
            break

    return plate, plate_contour

def main(raw_dir='data/raw'):
    os.makedirs('output/plate/', exist_ok=True)
    os.makedirs('output/detected_plate/', exist_ok=True)

    for img in os.listdir(raw_dir):
        img_path = os.path.join(raw_dir, img)
        img_name = os.path.splitext(img)[0]
        
        raw_img, gray, edged = preprocess_image(img_path)
            
        plate, plate_contour = find_license_plate(gray, edged)

        if plate is None:
            print("Could not find license plate in {img}. Skipping...")
            continue
        else:
            plate_dir = os.path.join('output/plate/', f"{img_name}.png")
            cv2.imwrite(plate_dir, plate)
            print(f"Saved license plate image to: {plate_dir}")

            cv2.drawContours(raw_img, [plate_contour], -1, (0, 255, 0), 3)
            detected_plate_dir = os.path.join('output/detected_plate/', f"{img_name}.png")
            cv2.imwrite(detected_plate_dir, raw_img)
            print(f"Saved detected license plate to: {detected_plate_dir}")

if __name__=="__main__":
    main()