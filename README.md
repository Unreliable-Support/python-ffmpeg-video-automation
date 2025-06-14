# Automated Social Media Video Generator

This project is a Python-based automation tool that programmatically creates short, engaging social media videos from a CSV data source using the powerful FFMPEG library.

It was developed as a portfolio piece to demonstrate the core skills required for the **AI Automation Developer** role at **TheSoul Publishing**, focusing on automating video production pipelines.

---

### Live Demo

A one-minute video demonstrating the script in action, from running the command to showing the final, generated MP4 files.

**[Click here to watch the full demo video (demo.mkv)]**

[![Watch the Demo](demo_thumbnail.jpg)](demo.mkv)

---

### The Problem
Creating dozens of unique, branded videos for social media is a slow, repetitive, and unscalable manual process. A creative team could spend hours creating content that a script can generate in minutes.

### The Solution
This script provides an end-to-end automated pipeline:
1.  It reads data (quotes and authors) from a simple `quotes.csv` file.
2.  For each row, it programmatically calls FFMPEG.
3.  It combines a background image, background music, and dynamically generated text into a finished MP4 video.
4.  The entire process is hands-off after running a single command.

### Key Technical Features
*   **Data-Driven:** The content of the videos is controlled entirely by the CSV file, making it easy to scale and manage.
*   **Advanced FFMPEG Filtering:** Uses a chained `drawtext` filter to achieve precise, professional-looking text layout, giving independent control over the position of the main text and the author.
*   **Dynamic Text Wrapping:** Implements Python's `textwrap` module to automatically break long lines of text, ensuring they fit within the video's dimensions.
*   **Robust and Standalone:** The script is self-contained and relies only on Python and a standard FFMPEG installation.

### Technologies Used
*   **Python 3**
    *   `subprocess` module for interfacing with the command line.
    *   `textwrap` module for text formatting.
*   **FFMPEG**

### How to Run
1.  Ensure you have [Python 3](https://www.python.org/downloads/) and [FFMPEG](https://ffmpeg.org/download.html) installed and accessible in your system's PATH.
2.  Clone this repository: `git clone https://github.com/YOUR_USERNAME/python-ffmpeg-video-automation.git`
3.  Navigate to the project directory: `cd python-ffmpeg-video-automation`
4.  Run the script: `python video_generator.py`
5.  The final videos will be saved in the `output_videos` folder.