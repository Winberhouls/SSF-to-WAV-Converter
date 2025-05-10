# SSF to WAV Converter

This script processes `.ssf` files in a selected directory and converts them into `.wav` files. It uses a standard WAV header and calculates the duration of the audio based on the file size.

## Features
- Recursively scans a directory for `.ssf` files.
- Converts `.ssf` files to `.wav` format.
- Displays a progress bar using `tqdm` to show the processing status.
- Calculates the audio duration based on a sample rate of 44.1 kHz, 16-bit depth, and stereo channels.

## How to Use
1. Run the script.
2. A dialog will appear asking you to select a folder containing `.ssf` files.
3. The script will process all `.ssf` files in the folder and its subfolders.
4. Converted `.wav` files will be saved in the same directory as the original `.ssf` files.

## Requirements
- Python 3.x
- `tqdm` library for the progress bar.

## Installation
1. Install Python 3.x if not already installed.
2. Install the `tqdm` library by running:
   ```bash
   pip install tqdm
   ```

## Example
If you have a folder with `.ssf` files, the script will convert them as follows:

```
Input: example.ssf
Output: example.wav
```

## Notes
- The script assumes a sample rate of 44.1 kHz, 16-bit depth, and stereo channels for the WAV header.
- Ensure the `.ssf` files are valid and contain audio data.

## License
This script is provided as-is without any warranty. Use it at your own risk.
