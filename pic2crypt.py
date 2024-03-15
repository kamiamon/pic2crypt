import argparse
from PIL import Image
import numpy as np
import os

def generate_key(image_path):
    img = Image.open(image_path)
    width, height = img.size
    key = np.random.randint(256, size=(height, width, 3), dtype=np.uint8)
    return key

def encrypt_image(image_path, key_path=None, save_path=None):
    if not key_path:
        key = generate_key(image_path)
        key_path = os.path.splitext(image_path)[0]
        np.save(key_path, key)
    else:
        key = np.load(key_path)

    img = Image.open(image_path)
    img_array = np.array(img)
    encrypted_img = img_array ^ key

    if not save_path:
        save_path = image_path + "_encrypted.png"

    encrypted_image = Image.fromarray(encrypted_img)
    encrypted_image.save(save_path)

    print('The selected image has been successfully encrypted.')

def decrypt_image(encrypted_image_path, key_path, save_path=None):
    key = np.load(key_path)
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img_array = np.array(encrypted_img)
    decrypted_img = encrypted_img_array ^ key

    if not save_path:
        save_path = os.path.splitext(encrypted_image_path)[0]

    decrypted_image = Image.fromarray(decrypted_img)
    decrypted_image.save(save_path)

    print('The selected image has been successfully decrypted.')

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
