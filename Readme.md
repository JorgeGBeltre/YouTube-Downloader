# YouTube Video Downloader

A simple Python script to download YouTube videos or audio using `yt-dlp`. Allows you to select the output format from several popular options.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Clone the Repository](#clone-the-repository)
- [Usage](#usage)
- [Supported Formats](#supported-formats)
- [Code Structure](#code-structure)
- [Known Limitations](#known-limitations)
- [Possible Errors](#possible-errors)
- [License](#license)
- [Contact](#contact)
- [Support](#support)


## Requirements

- Python 3.6 or higher
- pip (Python package manager)

## Installation

First, make sure you have the `yt-dlp` library installed:

```bash
pip install yt-dlp
```

## Clone the Repository

To clone this project to your local machine, run the following command in your terminal:

```bash
git clone https://github.com/JorgeGBeltre/YouTube-Downloader.git
```

Then navigate to the project directory:

```bash
cd youtube-downloader
```

## Usage

Once inside the directory, run the script with Python:

```bash
python downloader.py
```

**Note:** Make sure the file is named `downloader.py` (or whatever name you gave it).

When you run the script:

1. You will be prompted to enter the YouTube video URL
2. Then you need to specify the desired output format
3. The script validates if the format is supported
4. If valid, it starts downloading the highest quality available
5. The file is saved in the same directory where the script is executed, using the original video title

### Example execution:

```
Insert a YouTube video URL: https://www.youtube.com/watch?v=example
Insert the desired output format: mp4
Downloading...
```

## Supported Formats

| Format | Type  |
|--------|-------|
| mp4    | Video |
| mp3    | Audio |
| mkv    | Video |
| webm   | Video |
| flv    | Video |

## Code Structure

The script consists of:

1. **User input** – Prompts for YouTube URL and output format
2. **Validation** – Checks if the format is in the list of supported formats
3. **Download function** – Configures `yt-dlp` options and downloads the video
4. **Execution** – Calls the download function with user-provided values

### Key `yt-dlp` options used:

- `'format': 'best'` – Downloads the best available quality
- `'outtmpl': '%(title)s.' + output_format` – Saves the file with the video title and chosen extension

## Known Limitations

- **MP3 "conversion"** – For MP3 format, the script only saves the downloaded stream with an `.mp3` extension. It does **not** perform actual conversion to MP3 format. For proper MP3 conversion, additional options like `'postprocessors'` would be required.
- No error handling for invalid URLs or network issues
- Downloads only the best quality (no option to select specific quality)
- No progress bar or download status feedback

## Possible Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'yt_dlp'` | `yt-dlp` not installed | Run `pip install yt-dlp` |
| `Invalid format` message | Unsupported format entered | Use one of the supported formats: mp4, mp3, mkv, webm, flv |
| Download fails or stuck | Invalid URL or network issue | Verify the URL and check your internet connection |
| File not saved with correct extension | Video stream doesn't match the specified format | The format parameter only changes the file extension, not the actual stream format |

---

## License

Licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contact

Author: **Jorge Gaspar Beltre Rivera**  
Project: **YouTube Video Downloader**

<p align="center">
  <a href="https://www.linkedin.com/in/jorge-gaspar-beltre-rivera/" target="_blank"><img src="https://user-images.githubusercontent.com/74038190/235294012-0a55e343-37ad-4b0f-924f-c8431d9d2483.gif" alt="LinkedIn" width="100"></a>
  <a href="https://github.com/JorgeGBeltre" target="_blank"><img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" alt="GitHub" width="100"></a>
  <a href="mailto:Jorgegaspar3021@gmail.com"><img src="https://user-images.githubusercontent.com/74038190/216122065-2f028bae-25d6-4a3c-bc9f-175394ed5011.png" alt="E-Mail" width="100"></a>
</p>

---

## Support

This project is developed independently.

Even a small contribution helps me dedicate more time to development, testing, and releasing new features.


<p align="center">
  <a href="https://www.paypal.com/donate/?hosted_button_id=2VLA8BWT967LU">
    <img src="https://www.paypalobjects.com/webstatic/icon/pp258.png"
         alt="Donate with PayPal"
         height="60">
  </a>
</p>
