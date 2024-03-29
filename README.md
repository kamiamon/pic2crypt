# pic2crypt

pic2crypt is a simple Python tool for encrypting and decrypting images using symmetric key encryption. It allows you to securely encrypt your images to protect sensitive information.

## Features

- Encrypt images using symmetric key encryption.
- Decrypt encrypted images with the correct key.
- Generate random keys or use existing ones for encryption and decryption.

## Installation

1. Clone the repository:

        git clone https://github.com/yourusername/pic2crypt.git


2. Install dependencies:

        cd pic2crypt
        chmod +x install.sh
        ./install.sh

## Usage

1. Encrypt an image:

        python pic2crypt.py encrypt --image <path_to_image> --output <path_to_save_encrypted_image>

2. Decrypt an encrypted image:

        python pic2crypt.py decrypt --image <path_to_encrypted_image> --key <path_to_key_file> --output <path_to_save_decrypted_image>


