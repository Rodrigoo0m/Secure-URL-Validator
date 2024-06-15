# Secure URL Validator

This is a simple Python program to check if a URL is safe for access, identifying potentially malicious sites by querying URL reputation services.

## Features

- Checks the security of a URL by querying the URLVoid service.
- Returns a message indicating whether the URL is safe or potentially dangerous.
- Provides additional details on detections if any issues are found.

## Prerequisites

- Python 3.x installed
- Python libraries: `requests`

## Installing Dependencies

To install the `requests` library, you can use the `pip` package manager. In your terminal, run the following command:

```bash
pip install requests
```

## Usage

1. Clone the repository or download the files to your computer.

2. In your terminal, navigate to the directory where the files are located.

3. Run the Python script with the following command, replacing `https://example.com` with the URL you want to check:

   ```bash
   python url_validator.py
   ```

   Make sure to modify `url_validator.py` to the name of your Python script if necessary.

4. The program will display a message indicating whether the URL is safe or not, along with additional details if problems are detected.

## Example Output

```bash
$ python url_validator.py

Checking URL: https://example.com
The URL 'https://example.com' is safe.
```

## Contributions

Contributions are welcome! Feel free to submit pull requests for improvements, bug fixes, or new features.



