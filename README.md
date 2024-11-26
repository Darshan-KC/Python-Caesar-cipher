# Python Caesar Cipher

This repository contains a simple implementation of the Caesar Cipher algorithm in Python. The Caesar Cipher is a classic encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## Features

- Encrypt a plaintext message using a shift key.
- Decrypt a ciphertext message using a shift key.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetic characters during encryption/decryption.

## How It Works

The Caesar Cipher shifts each letter in the message by a specified number of positions. For example, with a shift of `3`:
- `A` becomes `D`
- `B` becomes `E`
- `Z` wraps around to `C`

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/Darshan-KC/Python-Caesar-cipher.git
    cd Python-Caesar-cipher
    ```

2. Run the script:
    ```bash
    python caesar_cipher.py
    ```

3. Follow the on-screen prompts to:
    - Choose between encryption and decryption.
    - Input the message and shift key.

### Example

**Input:**
- Operation: Encrypt
- Message: `Hello, World!`
- Shift Key: `3`

**Output:**
- Encrypted Message: `Khoor, Zruog!`

## File Structure

- `caesar_cipher.py`: The main script implementing the Caesar Cipher.

## Contributing

Contributions are welcome! If you find bugs or want to enhance the functionality, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 😊
