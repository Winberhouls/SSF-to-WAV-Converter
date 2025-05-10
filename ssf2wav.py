import tkinter as tk
from tkinter import filedialog
import os
import sys
from tqdm import tqdm

def process_ssf_files_in_directory(directory):
    # Scan all .ssf files in the folder and subfolders
    ssf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.ssf'):
                ssf_files.append(os.path.join(root, file))

    total_files = len(ssf_files)
    print(f"Found {total_files} .ssf files to process.")

    # Process each file with a progress bar
    progress_bar = tqdm(ssf_files, desc="Processing files", unit="file", file=sys.stdout, leave=True)
    for file_path in progress_bar:
        try:
            progress_bar.set_description(f"Processing: {os.path.basename(file_path)}")

            with open(file_path, 'rb') as f:
                content = f.read()

            # Calculate the duration of the file based on its size
            sample_rate = 44100  # 44.1 kHz
            bit_depth = 16  # 16 bits
            num_channels = 2  # Stereo
            byte_rate = sample_rate * num_channels * (bit_depth // 8)
            data_size = len(content) - 44  # Data size excluding the WAV header
            duration = data_size / byte_rate

            # Create a standard WAV header
            wav_header = b'RIFF'  # Chunk ID
            wav_header += (36 + data_size).to_bytes(4, 'little')  # Chunk Size
            wav_header += b'WAVE'  # Format
            wav_header += b'fmt '  # Subchunk1 ID
            wav_header += (16).to_bytes(4, 'little')  # Subchunk1 Size
            wav_header += (1).to_bytes(2, 'little')  # Audio Format (PCM)
            wav_header += (num_channels).to_bytes(2, 'little')  # Num Channels
            wav_header += (sample_rate).to_bytes(4, 'little')  # Sample Rate
            wav_header += (byte_rate).to_bytes(4, 'little')  # Byte Rate
            wav_header += (num_channels * (bit_depth // 8)).to_bytes(2, 'little')  # Block Align
            wav_header += (bit_depth).to_bytes(2, 'little')  # Bits per Sample
            wav_header += b'data'  # Subchunk2 ID
            wav_header += data_size.to_bytes(4, 'little')  # Subchunk2 Size

            # Replace the first bytes with the WAV header
            new_content = wav_header + content[44:]

            # Save the modified file with a .wav extension
            new_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".wav"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            with open(new_file_path, 'wb') as new_file:
                new_file.write(new_content)
        except Exception as e:
            tqdm.write(f"Error processing file {file_path}: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    directory = filedialog.askdirectory(title="Select a folder with .ssf files")

    if directory:
        print(f"Selected folder: {directory}")
        process_ssf_files_in_directory(directory)
    else:
        print("No folder selected.")

if __name__ == "__main__":
    main()

input("Press Enter to exit...")