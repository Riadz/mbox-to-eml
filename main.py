import mailbox
import os
import re

def sanitize_filename(subject):
    # Remove invalid characters for filenames
    sanitized = re.sub(r'[\\/*?:"<>|]', "", subject)
    # Truncate if too long (optional)
    return sanitized[:100] # Limit length

mbox_file_path = './all_mail.mbox'
output_directory = './output'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Open the MBOX file
mbox = mailbox.mbox(mbox_file_path)

print(f"Processing {len(mbox)} messages from {mbox_file_path}...")

for i, message in enumerate(mbox):
    try:
        # Generate a filename (be careful with subjects containing special chars)
        subject = message.get('Subject', 'No Subject')
        # Simple unique name approach: index + sanitized subject
        filename = f"{i:04d}_{sanitize_filename(subject)}.eml"
        filepath = os.path.join(output_directory, filename)

        message_bytes = message.as_bytes()

        # Write the bytes to an .eml file
        with open(filepath, 'wb') as f:
            f.write(message_bytes)

        # print progress
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1} messages...")

    except Exception as e:
        print(f"Error processing message {i}: {e}")

print(f"Conversion complete. EML files saved in {output_directory}")