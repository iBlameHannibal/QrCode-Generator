import qrcode  # Install using `pip install qrcode`

def generate_qrcode(data, output_file, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_L,
                   border=4, margin=1, foreground_color="black", background_color="white"):
    """
    Generates a QR code and saves it as an image file.

    Args:
        data (str): The data to encode into the QR code.
        output_file (str): The path to the output image file.
        box_size (int, optional): The size of each box in the QR code (default: 10).
        error_correction (qrcode.constants.ERROR_CORRECT, optional): The error correction level.
                                 Higher levels can recover from more damage (default: ERROR_CORRECT_L).
        border (int, optional): The number of white pixels around the QR code (default: 4).
        margin (int, optional): The number of white pixels between boxes (default: 1).
        foreground_color (str, optional): The color of the QR code modules (default: "black").
        background_color (str, optional): The background color (default: "white").
    """

    qr = qrcode.QRCode(
        version=None,  # Automatically determine version based on data and error correction
        box_size=box_size,
        error_correction=error_correction
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    img.save(output_file)

# Example usage:
data = "https://www.example.com"  # Replace with your desired data
output_file = "qrcode.png"
generate_qrcode(data, output_file, box_size=15, error_correction=qrcode.constants.ERROR_CORRECT_H)

print(f"QR code generated successfully and saved to '{output_file}'")
