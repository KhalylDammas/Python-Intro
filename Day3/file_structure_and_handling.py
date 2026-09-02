"""Day 3: beginner-friendly examples for working with files in Python.

Run this file from anywhere:

    python Day3/file_structure_and_handling.py

The examples read the starter files in ``Day3/data`` and write new files to
``Day3/output``. During Day 4, this output directory is used to explain why a
project needs a ``.gitignore`` file.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


# __file__ is the path of this Python file. Building paths from it means the
# script works whether it is launched from the repository root or from Day3.
DAY3_DIR = Path(__file__).resolve().parent
DATA_DIR = DAY3_DIR / "data"
OUTPUT_DIR = DAY3_DIR / "output"


def print_heading(title: str) -> None:
    """Make the terminal output easier to follow during a live lesson."""
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def demonstrate_text_files() -> None:
    """Read, write, and append to a UTF-8 text file."""
    print_heading("TEXT FILES")
    source_path = DATA_DIR / "text_file.txt"

    # open() returns a file object. The with block closes it automatically,
    # even if an error happens. Always state the text encoding explicitly.
    with source_path.open(mode="r", encoding="utf-8") as file:
        all_text = file.read()  # Read the rest of the file as one string.
    print("read() returned a", type(all_text).__name__)
    print(all_text)

    with source_path.open(mode="r", encoding="utf-8") as file:
        first_line = file.readline()  # One line, including its final \n.
        second_line = file.readline()
    print("First line:", first_line.rstrip())
    print("Second line:", second_line.rstrip())

    with source_path.open(mode="r", encoding="utf-8") as file:
        lines = file.readlines()  # A list containing all remaining lines.
    print("readlines() returned:", lines)

    # Iteration is memory-efficient because it reads one line at a time. This
    # is usually the best option for a very large text file.
    print("Numbered lines:")
    with source_path.open(mode="r", encoding="utf-8") as file:
        # for line_number, line in enumerate(file, start=1):
        #     print(f"  {line_number}: {line.rstrip()}")
        for i in range(3):
            print(f"  {i + 1}: {lines[i].rstrip()}")

    output_path = OUTPUT_DIR / "lesson_notes.txt"

    # "w" creates a file or REPLACES all of an existing file's contents.
    with output_path.open(mode="w", encoding="utf-8") as file:
        characters_written = file.write("File handling lesson\n")
        file.writelines(["- read text\n", "- write text\n"])
    print(f"write() wrote {characters_written} characters")

    # "a" creates a file if needed and adds content at the end.
    with output_path.open(mode="a", encoding="utf-8") as file:
        file.write("- append text\n")

    print(f"Created: {output_path.relative_to(DAY3_DIR)}")
    print(output_path.read_text(encoding="utf-8"))


def demonstrate_json_files() -> None:
    """Load JSON into Python, change it, and save valid JSON."""
    print_heading("JSON FILES")
    source_path = DATA_DIR / "course.json"

    with source_path.open(mode="r", encoding="utf-8") as file:
        # course: dict[str, Any] = json.load(file) # Typing is an advanced method. For reference only
        course = json.load(file)

    # JSON objects become dictionaries; arrays become lists. JSON also maps
    # strings, numbers, booleans, and null to their Python equivalents.
    print("Python type:", type(course).__name__)
    print("Course:", course["course_name"])
    print("Topics:", ", ".join(course["topics"]))

    course["completed"] = True
    course["topics"].append("images")

    output_path = OUTPUT_DIR / "course_updated.json"
    with output_path.open(mode="w", encoding="utf-8") as file:
        # indent makes the file readable. ensure_ascii=False preserves Unicode.
        json.dump(course, file, indent=2, ensure_ascii=False)
        file.write("\n")

    print(f"Created: {output_path.relative_to(DAY3_DIR)}")
    print(json.dumps(course, indent=2, ensure_ascii=False))


def demonstrate_csv_files() -> None:
    """Read and write rows in a comma-separated values file."""
    print_heading("CSV FILES")
    source_path = DATA_DIR / "students.csv"

    # newline="" is recommended by the csv documentation. DictReader uses
    # the first row as column names and returns each later row as a dictionary.
    with source_path.open(mode="r", encoding="utf-8", newline="") as file:
        students = list(csv.DictReader(file))

    print("Student rows:")
    for student in students:
        completed = student["completed"].lower() == "true"
        print(f"  {student['name']}: {student['score']} (completed={completed})")

    # CSV has no built-in number or Boolean types, so values read from a CSV
    # are strings. Convert them before doing calculations.
    average = sum(int(student["score"]) for student in students) / len(students)
    print(f"Average score: {average:.1f}")

    # Filter the list to include only students with a score of 80 or higher.
    passing_students = []
    for student in students:
        if int(student["score"]) >= 80:
            passing_students.append(student)

    # List comprehension is a more concise way to filter a list.
    # It is advanced syntax that is not required for this lesson, but it is included here
    # to show a more Pythonic way to achieve the same result.
    
    # passing_students = [
    #     student for student in students if int(student["score"]) >= 80
    # ]

    output_path = OUTPUT_DIR / "passing_students.csv"
    fieldnames = ["name", "score", "completed"]

    with output_path.open(mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(passing_students)

    print(f"Created: {output_path.relative_to(DAY3_DIR)}")


def demonstrate_images() -> None:
    """Create PNG and JPEG files and compare their important properties."""
    print_heading("IMAGES: PNG AND JPEG")

    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("Pillow is not installed. Run: python -m pip install Pillow")
        return

    width, height = 640, 360

    # RGBA means Red, Green, Blue, Alpha. Alpha controls transparency:
    # 0 is invisible, 255 is fully opaque, and values between are translucent.
    transparent_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(transparent_image)
    draw.rectangle((40, 40, 360, 250), fill=(30, 144, 255, 180))
    draw.ellipse((240, 90, 590, 330), fill=(255, 99, 71, 150))
    draw.text((50, 300), "PNG can preserve transparency", fill=(20, 20, 20, 255))

    png_path = OUTPUT_DIR / "transparency_demo.png"
    transparent_image.save(png_path, format="PNG")

    # JPEG has no alpha channel. Before saving, place the transparent artwork
    # on a solid background and convert RGBA to RGB.
    white_background = Image.new("RGBA", transparent_image.size, "white")
    flattened = Image.alpha_composite(white_background, transparent_image).convert("RGB")

    jpeg_medium_path = OUTPUT_DIR / "photo_quality_60.jpg"
    jpeg_high_path = OUTPUT_DIR / "photo_quality_95.jpg"
    flattened.save(jpeg_medium_path, format="JPEG", quality=60)
    flattened.save(jpeg_high_path, format="JPEG", quality=95)

    # Opening an image does not load every pixel immediately. A with block
    # ensures the underlying file is closed when its metadata has been read.
    for image_path in (png_path, jpeg_medium_path, jpeg_high_path):
        with Image.open(image_path) as image:
            size_kib = image_path.stat().st_size / 1024
            print(
                f"{image_path.name:26} format={image.format:4} "
                f"mode={image.mode:4} size={image.size} file={size_kib:.1f} KiB"
            )

    # thumbnail() changes this copy in place while keeping its aspect ratio.
    thumbnail = flattened.copy()
    thumbnail.thumbnail((200, 200))
    thumbnail_path = OUTPUT_DIR / "thumbnail.jpg"
    thumbnail.save(thumbnail_path, format="JPEG", quality=85)
    print(f"Created thumbnail with dimensions {thumbnail.size}")

    # A digital image is a grid. Each (x, y) coordinate stores one pixel.
    # This small image is drawn pixel by pixel from a text pattern.
    pixel_pattern = [
        "..........",
        "...YYYY...",
        "..YYYYYY..",
        ".YBYYYYBY.",
        ".YBYYYYBY.",
        ".YYYYYYYY.",
        ".YYBYYBYY.",
        ".YYYBBYYY.",
        "..YYYYYY..",
        "...YYYY...",
    ]
    palette = {
        ".": (100, 180, 255),  # Blue background
        "Y": (255, 213, 50),   # Yellow face
        "B": (40, 40, 40),     # Dark eyes and mouth
    }

    pixel_art = Image.new("RGB", (10, 10))
    for y, row in enumerate(pixel_pattern):
        for x, symbol in enumerate(row):
            # putpixel() changes one pixel at the (x, y) coordinate.
            pixel_art.putpixel((x, y), palette[symbol])

    pixel_art_path = OUTPUT_DIR / "pixel_art_10x10.png"
    pixel_art.save(pixel_art_path)

    print("Selected pixels from the 10 x 10 image:")
    for coordinate in ((0, 0), (3, 3), (2, 3)):
        # getpixel() returns this RGB image's (red, green, blue) tuple.
        print(f"  pixel {coordinate} = {pixel_art.getpixel(coordinate)}")

    # A 10 x 10 image is difficult to see. NEAREST repeats each original pixel
    # as a sharp square rather than blending neighboring colors together.
    scale = 32
    magnified_size = (pixel_art.width * scale, pixel_art.height * scale)
    magnified = pixel_art.resize(magnified_size, Image.Resampling.NEAREST)

    # Add a grid so the boundary of every original pixel is visible on screen.
    grid = ImageDraw.Draw(magnified)
    for x in range(0, magnified.width, scale):
        grid.line((x, 0, x, magnified.height), fill=(255, 255, 255), width=1)
    for y in range(0, magnified.height, scale):
        grid.line((0, y, magnified.width, y), fill=(255, 255, 255), width=1)

    magnified_path = OUTPUT_DIR / "pixel_art_magnified.png"
    magnified.save(magnified_path)
    print(f"Created visible pixel grid: {magnified_path.relative_to(DAY3_DIR)}")


def main() -> None:
    """Create the output directory and run every demonstration."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    # demonstrate_text_files()
    # demonstrate_json_files()
    # demonstrate_csv_files()
    demonstrate_images()


if __name__ == "__main__":
    main()
