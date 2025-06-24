===========================================
Secure Image Steganography using RSA
===========================================

This project hides secret messages inside an image using LSB (Least Significant Bit) steganography,
and encrypts the message using RSA public key encryption to ensure high security.

-------------------------
PROJECT STRUCTURE
-------------------------

rsa_steg_project/
│
├── main.py              -> Main program to run hide/extract options
├── rsa_utils.py         -> RSA key generation, encryption, decryption
├── steg_utils.py        -> LSB steganography functions
├── sample_image.png     -> Input image (you provide this)
├── output_image.png     -> Output image with hidden message
├── private.pem          -> Private RSA key file (generated automatically)
├── README.txt           -> Project description

-------------------------
FEATURES
-------------------------

- Encrypt message using RSA before hiding it
- Hide encrypted message inside image pixels (LSB)
- Decrypt and extract hidden message using private key
- Lossless method (uses PNG image)
- Educational project to learn steganography and cryptography

-------------------------
REQUIREMENTS
-------------------------

Install required packages:

> pip install pillow pycryptodome

-------------------------
HOW TO USE
-------------------------

1. Add a PNG image as 'sample_image.png' to the folder.
2. Run the main program:

> python main.py

3. Choose:
   1 - To hide a message
   2 - To extract a message

4. If hiding:
   - Type your secret message
   - Encrypted message will be saved in 'output_image.png'
   - Private key will be saved in 'private.pem'

5. If extracting:
   - Make sure 'private.pem' and 'output_image.png' are in the folder
   - It will decode and decrypt the original message

-------------------------
NOTES
-------------------------

- Keep 'private.pem' secure. Anyone with it can decrypt your message.
- Only PNG images are recommended for accurate hiding.
- Maximum message size depends on image dimensions.

-------------------------
AUTHOR
-------------------------

Ankitha Kunta 
B.Tech Cybersecurity Student  
 
