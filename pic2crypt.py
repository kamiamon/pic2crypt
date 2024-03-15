import argparse
from PIL import Image
import numpy as np
import os

def generate_key(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        key = np.random.randint(256, size=(height, width, 3), dtype=np.uint8)
        return key
    except Exception as e:
        print(f"Error generating key: {e}")
        return None

def encrypt_image(image_path, key_path=None, save_path=None):
    key = generate_key(image_path)
    if key is None:
        return

    try:
        key_path = os.path.splitext(image_path)[0] + "_key"
        np.save(key_path, key)

        img = Image.open(image_path)
        img_array = np.array(img)
        encrypted_img = img_array ^ key

        if not save_path:
            save_path = os.path.splitext(image_path)[0] + "_encrypted.png"

        encrypted_image = Image.fromarray(encrypted_img)
        encrypted_image.save(save_path)

        print('The selected image has been successfully encrypted.')
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(encrypted_image_path, key_path, save_path=None):
    try:
        key = np.load(key_path)
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_img_array = np.array(encrypted_img)
        decrypted_img = encrypted_img_array ^ key

        if not save_path:
            save_path = os.path.splitext(encrypted_image_path)[0] + "_decrypted.png"

        decrypted_image = Image.fromarray(decrypted_img)
        decrypted_image.save(save_path)

        print('The selected image has been successfully decrypted.')
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    parser = argparse.ArgumentParser(description='Image Encryption/Decryption Tool')
    parser.add_argument('command', choices=['encrypt', 'decrypt'], help='Choose "encrypt" to encrypt an image or "decrypt" to decrypt an image')
    parser.add_argument('--image', help='Path to the image file')
    parser.add_argument('--key', help='Path to the key file (for decryption)')
    parser.add_argument('--output', help='Path to save the output image')

    args = parser.parse_args()

    if args.command == 'encrypt':
        encrypt_image(args.image, args.key, args.output)
    elif args.command == 'decrypt':
        decrypt_image(args.image, args.key, args.output)

if __name__ == "__main__":
    main()
