import os
import subprocess
import textwrap

# --- SETTINGS (Final Professional Version) ---
OUTPUT_DIR = "output_videos"
BACKGROUND_IMAGE = "background.jpg"
MUSIC_FILE = "music.mp3"
CSV_FILE = "quotes.csv"
FONT_FILE = "arial.ttf" 
VIDEO_DURATION = "10"
FONT_SIZE = "52"
FONT_COLOR = "white"
WRAP_WIDTH = 40
# The vertical distance (in pixels) between the main quote and the author's name
AUTHOR_OFFSET_Y = 120

# --- SCRIPT START ---

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(CSV_FILE, mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    
    for i, line in enumerate(lines[1:]):
        if not line.strip():
            continue

        try:
            quote_part, author_part = line.strip().rsplit(',', 1)
        except ValueError:
            print(f"WARNING: Line {i+1} is not in the correct format and will be skipped: {line.strip()}")
            continue

        quote = quote_part.strip().replace('"', '')
        author = author_part.strip()
        
        output_filename = os.path.join(OUTPUT_DIR, f"quote_video_{i+1}.mp4")
        
        print(f"Generating video {i+1}: {author}")

        # --- ADVANCED TEXT RENDERING: TWO-FILTER CHAIN ---
        # This method provides precise control over the layout by using two separate drawtext filters.

        # 1. Wrap the long quote text
        wrapper = textwrap.TextWrapper(width=WRAP_WIDTH)
        wrapped_quote = wrapper.fill(text=quote)

        # 2. Escape special characters for FFMPEG filter
        def escape_ffmpeg_text(text):
            return text.replace("'", "'\\''").replace(":", "\\:")

        safe_wrapped_quote = escape_ffmpeg_text(wrapped_quote)
        safe_author = escape_ffmpeg_text(f"- {author}")

        # 3. Create the two chained drawtext filters
        # The first filter draws the main quote, shifted slightly up.
        # The second filter draws the author, shifted slightly down.
        # The comma between them chains the filters together.
        drawtext_filter = (
            f"drawtext="
            f"fontfile='{FONT_FILE}':"
            f"text='{safe_wrapped_quote}':"
            f"x=(w-text_w)/2:"
            f"y=(h-text_h)/2 - {AUTHOR_OFFSET_Y / 2}:" # Position the quote block
            f"fontsize={FONT_SIZE}:"
            f"fontcolor={FONT_COLOR}:"
            f"box=1:boxcolor=black@0.5:boxborderw=15," # Note the comma here
            
            f"drawtext="
            f"fontfile='{FONT_FILE}':"
            f"text='{safe_author}':"
            f"x=(w-text_w)/2:"
            f"y=(h-text_h)/2 + {AUTHOR_OFFSET_Y / 2}:" # Position the author block
            f"fontsize={FONT_SIZE}:"
            f"fontcolor={FONT_COLOR}:"
            f"box=1:boxcolor=black@0.5:boxborderw=15"
        )

        # 4. Assemble and run the final command
        command = [
            'ffmpeg', '-y',
            '-loop', '1',
            '-i', BACKGROUND_IMAGE,
            '-i', MUSIC_FILE,
            '-vf', drawtext_filter,
            '-c:v', 'libx264',
            '-t', VIDEO_DURATION,
            '-c:a', 'aac',
            '-shortest',
            '-pix_fmt', 'yuv420p',
            output_filename
        ]
        
        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Video {i+1} created successfully!")
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Could not create video {i+1}.")
            print("FFMPEG Error Message:")
            print(e.stderr.decode('utf-8', errors='ignore'))

print("\nProcess finished!")
print(f"Your videos have been saved to the '{OUTPUT_DIR}' folder.")