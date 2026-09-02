# Day 3 — Working with Files in Python

## Lesson goal

By the end of this lesson, students should be able to:

- open and close files safely;
- choose the correct file mode;
- read text with `read()`, `readline()`, `readlines()`, or a loop;
- create and update text files with `write()` and `writelines()`;
- convert between JSON and Python data structures;
- read and write CSV rows;
- open, create, resize, and save images with Pillow; and
- explain the practical differences between PNG and JPEG.

Estimated teaching time: 90–120 minutes.

## Before class

From the repository root, install the one optional dependency:

```bash
python -m pip install -r requirements.txt
```

Run the complete demonstration:

```bash
python Day3/file_structure_and_handling.py
```

The program reads files from `Day3/data/` and creates files under
`Day3/output/`. Its contents can be recreated at any time. During Day 4,
students will see these output files in `git status` and learn how to ignore
them before making the first commit.

## Suggested lesson flow

| Time | Topic | Live demonstration |
| ---: | --- | --- |
| 10 min | Files and paths | Locate `Day3/data/text_file.txt` |
| 25 min | Text files | Run `demonstrate_text_files()` |
| 15 min | JSON | Inspect and update `course.json` |
| 20 min | CSV | Filter `students.csv` and write a new CSV |
| 25 min | Images | Generate PNG/JPEG files and compare them |
| 15 min | Exercises and review | Students change and rerun the examples |

---

## 1. The file-handling pattern

Most file operations follow three steps:

1. Open the file.
2. Read from it or write to it.
3. Close it.

Python's `with` statement handles step 3 automatically:

```python
with open("notes.txt", mode="r", encoding="utf-8") as file:
    content = file.read()

# The file is closed here, outside the with block.
```

Presenter note: ask what might happen if a program crashes before manually
calling `file.close()`. The `with` block is safer because cleanup still occurs.

### File modes

| Mode | Meaning | If the file does not exist | If it exists |
| --- | --- | --- | --- |
| `"r"` | Read text | Error | Opens it |
| `"w"` | Write text | Creates it | Erases and replaces it |
| `"a"` | Append text | Creates it | Writes at the end |
| `"x"` | Create text | Creates it | Error |
| `"rb"` | Read bytes | Error | Opens it |
| `"wb"` | Write bytes | Creates it | Erases and replaces it |

The `b` modes are for binary data such as images. Libraries such as Pillow
normally handle those bytes for us.

> **Important:** `"w"` replaces the entire file. Use `"a"` when existing
> content must remain.

### Paths with `pathlib`

The demonstration uses `Path` instead of manually joining strings:

```python
from pathlib import Path

day3_directory = Path(__file__).resolve().parent
text_path = day3_directory / "data" / "text_file.txt"
```

This also prevents a common problem: a relative path such as
`"data/text_file.txt"` depends on the terminal's current working directory.

---

## 2. Reading text files

Open `file_structure_and_handling.py` and present the four approaches in
`demonstrate_text_files()`.

### `read()`

Returns the file content as one string. It is convenient for small files.

```python
with open("story.txt", encoding="utf-8") as file:
    story = file.read()
```

`read(10)` reads at most ten characters. Calling `read()` again continues from
the current position rather than restarting.

### `readline()`

Returns one line at a time. The newline character is included when present.

```python
with open("story.txt", encoding="utf-8") as file:
    first = file.readline()
    second = file.readline()
```

### `readlines()`

Returns a list of lines. It is simple, but stores the full file in memory.

```python
with open("story.txt", encoding="utf-8") as file:
    lines = file.readlines()
```

### Looping over the file

This is the normal choice for a large text file because only one line is
processed at a time:

```python
with open("large_log.txt", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

Presenter prompt: ask students which technique they would select for a 5 GB
log file and why.

---

## 3. Writing text files

`write()` accepts one string and returns the number of characters written:

```python
with open("message.txt", "w", encoding="utf-8") as file:
    count = file.write("Hello\n")
```

Python does not add a newline automatically. Include `\n` when a line should
end. `writelines()` accepts an iterable of strings, but it also does not add
newlines:

```python
lines = ["First\n", "Second\n"]
with open("message.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

Append without deleting the existing content:

```python
with open("message.txt", "a", encoding="utf-8") as file:
    file.write("Third\n")
```

---

## 4. JSON files

JSON is text designed to represent structured data. It is common in web APIs,
configuration files, and data exchange.

| JSON | Python after loading |
| --- | --- |
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

Read JSON directly from a file with `json.load()`:

```python
import json

with open("course.json", encoding="utf-8") as file:
    course = json.load(file)
```

Change the normal Python object, then write it with `json.dump()`:

```python
course["completed"] = True

with open("course_updated.json", "w", encoding="utf-8") as file:
    json.dump(course, file, indent=2, ensure_ascii=False)
```

Easy distinction to teach:

- `load()` and `dump()` work with **file objects**.
- `loads()` and `dumps()` work with **strings**.

Malformed JSON raises `json.JSONDecodeError`. JSON requires double quotes
around property names and string values; Python-style single quotes are not
valid JSON.

---

## 5. CSV files

CSV stores rows and columns as text. A comma is the usual delimiter, but CSV
files can also use semicolons or tabs.

`csv.DictReader` uses the header row as keys:

```python
import csv

with open("students.csv", encoding="utf-8", newline="") as file:
    students = list(csv.DictReader(file))
```

All values read from CSV are strings. Convert values before calculations:

```python
average = sum(int(row["score"]) for row in students) / len(students)
```

Use `csv.DictWriter` to keep column names visible in the code:

```python
columns = ["name", "score", "completed"]

with open("results.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(students)
```

The `csv` module correctly handles commas and quotes inside values. Avoid
building CSV rows by joining strings manually.

---

## 6. Images with Pillow

A digital image is a grid of pixels. A pixel's channels depend on the image
mode:

- `RGB`: red, green, and blue, each normally from 0 to 255;
- `RGBA`: RGB plus alpha (transparency);
- `L`: grayscale.

Basic Pillow operations:

```python
from PIL import Image

with Image.open("picture.png") as image:
    print(image.format)  # PNG
    print(image.size)    # (width, height)
    print(image.mode)    # RGBA, RGB, L, etc.

    copy = image.copy()

copy.thumbnail((200, 200))
copy.save("thumbnail.png")
```

### Seeing individual pixels

An image is a two-dimensional grid of pixels. Pillow addresses a pixel with an
`(x, y)` coordinate:

- `x` starts at `0` on the left and increases to the right;
- `y` starts at `0` at the top and increases downward; and
- an RGB pixel is represented by a tuple such as `(255, 0, 0)` for red.

Read or change one pixel with `getpixel()` and `putpixel()`:

```python
from PIL import Image

image = Image.new("RGB", (3, 2), "white")
image.putpixel((1, 0), (255, 0, 0))

print(image.getpixel((1, 0)))  # (255, 0, 0)
```

The complete demonstration creates a tiny 10 × 10 pixel-art image. It then
magnifies the image to 320 × 320 using nearest-neighbor resizing and draws a
grid around the original pixels:

```python
scale = 32
magnified = pixel_art.resize((320, 320), Image.Resampling.NEAREST)
```

Nearest-neighbor scaling copies each source pixel into a larger solid block.
Other resize filters blend neighboring pixels, which is desirable for photos
but makes a pixel demonstration less clear.

Presenter activity:

1. Open `pixel_art_10x10.png`. Explain that its entire width is only ten
   pixels, so many image viewers display it as a tiny image.
2. Open `pixel_art_magnified.png` on the projector.
3. Point to one square and connect it to an `(x, y)` coordinate and its printed
   RGB tuple.
4. Change one entry in `pixel_pattern`, rerun the script, and locate the changed
   pixel.

### PNG compared with JPEG

| Property | PNG | JPEG |
| --- | --- | --- |
| Compression | Lossless | Lossy |
| Transparency | Supported with alpha | Not supported |
| Best suited to | Logos, icons, screenshots, text | Photographs and complex color gradients |
| Repeated saves | Keeps pixel data | Can add compression artifacts |
| Typical extension | `.png` | `.jpg` or `.jpeg` |

Compression and file size depend on the image content. JPEG's `quality`
setting trades file size for visual detail. A PNG can sometimes be smaller
than a JPEG for flat graphics, while JPEG is usually effective for photos.

Run the demonstration and open the files created in `Day3/output/`:

- `transparency_demo.png` keeps partially transparent pixels;
- `photo_quality_60.jpg` has stronger compression;
- `photo_quality_95.jpg` preserves more detail but is usually larger; and
- `thumbnail.jpg` demonstrates resizing while preserving aspect ratio;
- `pixel_art_10x10.png` is the actual ten-by-ten-pixel image; and
- `pixel_art_magnified.png` makes every original pixel visible as a grid cell.

Presenter prompt: compare the terminal's format, mode, dimensions, and file
size output. Explain why the JPEG versions have mode `RGB`, not `RGBA`.

---

## Student exercises

1. Change the text example so it counts how many words are in
   `data/text_file.txt`.
2. Add a `duration_minutes` property to `data/course.json`, then print it.
3. Change the CSV passing score from 80 to 85. Predict which names will be in
   the output before running the program.
4. Add a new student row and confirm the average changes.
5. Create JPEG files at quality 20 and quality 100. Compare their file sizes
   and zoom in to look for artifacts.
6. Change the PNG alpha values. What does 0 look like? What does 255 look like?
7. Change one pixel in the pixel-art pattern. Predict its `(x, y)` coordinate,
   then confirm its RGB value with `getpixel()`.

## Exercise hints

<details>
<summary>Show hints</summary>

1. Use `all_text.split()` and `len()`.
2. Assign with `course["duration_minutes"] = 120`.
3. Change the comparison inside the list comprehension.
4. CSV rows must follow the same three-column header.
5. Pass `quality=20` or `quality=100` to `save()`.
6. Alpha is the fourth number in an RGBA tuple.
7. Remember that coordinates begin at `(0, 0)` in the top-left corner.

</details>

## Review questions

- Why is `with open(...)` preferred over opening and closing manually?
- What is the difference between `"w"` and `"a"`?
- When would a loop be preferable to `readlines()`?
- What Python type does a JSON array become?
- Why must a CSV score be converted before arithmetic?
- Why can an RGBA image not be saved directly as JPEG?
- Where is pixel `(0, 0)`, and what does an RGB tuple contain?

## Common mistakes to demonstrate

- Running from a different directory and using a fragile relative path.
- Forgetting `encoding="utf-8"` for text.
- Expecting `write()` or `writelines()` to insert newlines.
- Using `"w"` when intending to append.
- Writing Python dictionary syntax and calling it JSON.
- Treating CSV numbers as numbers instead of strings.
- Trying to save an `RGBA` image as JPEG without flattening it to `RGB`.
