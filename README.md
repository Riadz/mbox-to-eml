# mbox-to-eml

This Python script converts an MBOX file into a series of individual `.eml` files.

## Description

This script takes an MBOX file as input and extracts each email message, saving it as a separate `.eml` file.

## Usage

1.  **Install Python and Git:** Ensure you have Python 3.6 or higher and Git installed.
2.  **Clone the repository:**

    ```bash
    git clone git@github.com:Riadz/mbox-to-eml.git
    cd mbox-to-eml
    ```

3.  **Prepare your MBOX file:** Replace `all_mail.mbox` with the path to your MBOX file.
4.  **Run the script:**

    ```bash
    python main.py
    ```

5.  **Find your EML files:** The converted `.eml` files will be located in the `output` directory.

## Gmail to Outlook Migration

I recently needed this script to move my emails from Gmail to Outlook because my company migrated from Google Workspace to Microsoft 365, for this specific use case do the following:

- using [Google Takeout](https://takeout.google.com/), check Gmail and download the takeout.
- unzip the downloaded file, find the `Mail` folder and rename the `.mbox` file inside to `all_mail.mbox`.
- place the `all_mail.mbox` file in the same directory as this script.
- run the script, and it will create an `output` folder with all your emails in `.eml` format.
- go to Outlook, then Settings, then Files, from there you can select the output folder to import.

## Limitations

*   The script assumes a standard MBOX format.
*   Large MBOX files may take a significant amount of time to process.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.