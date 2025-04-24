# mbox-to-eml

This Python script converts an MBOX file into a series of individual `.eml` files.

## Usage

1.  **Install Python:** Ensure you have Python 3.6 or higher installed.
2.  **Clone the repository:**

    If you have git installed, you can clone the repository using the following command:

    ```bash
    git clone git@github.com:Riadz/mbox-to-eml.git
    cd mbox-to-eml
    ```

    If you don't have git installed, you can download the zip file from the repository and extract it.

3.  **Prepare your MBOX file:** Replace `all_mail.mbox` with your MBOX file, most be the same name.
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