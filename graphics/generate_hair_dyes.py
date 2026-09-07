from pathlib import Path

# Hair dye name + RGB values
colors = [
    ("Black", 26, 23, 20),
    ("Blonde", 212, 171, 69),
    ("Ginger", 189, 89, 33),
    ("Light_Brown", 158, 107, 43),
    ("Brown", 102, 66, 23),
    ("Yellow", 255, 214, 115),
    ("Dark_Ginger", 150, 59, 8),
    ("Bright_Red", 255, 46, 102),
    ("Blue", 66, 89, 207),
    ("Green", 54, 107, 43),
    ("Pink", 245, 82, 150),
    ("Red", 209, 38, 18),
    ("White", 201, 199, 191),
    ("Bright_Yellow", 252, 222, 0),
    ("Orange", 252, 153, 0),
    ("Burgundy", 166, 31, 87),
    ("Purple", 184, 64, 227),
    ("Lime", 140, 199, 0),
    ("Teal", 3, 125, 145),
    ("Cyan", 59, 235, 230),
    ("Dark_Blue", 0, 51, 153),
    ("Dark_Green", 51, 102, 51),
    ("Dark_Red", 153, 0, 0),
    ("Sea_Green", 0, 153, 102),
    ("Indigo", 102, 51, 153),
    ("Grey", 128, 128, 128),
    ("Lavender", 217, 176, 235),
    ("Light_Green", 168, 255, 79),
    ("Olive", 110, 153, 54),
    ("Turquoise", 13, 212, 168),
]

# SVG dimensions
WIDTH = 40
HEIGHT = 16
BORDER = 2

# This script is located inside the graphics folder.
# SVG files will be created in the same graphics folder.
output_folder = Path(__file__).resolve().parent

# Generate each SVG
for name, r, g, b in colors:

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">

    <rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>

    <rect x="{BORDER}"
          y="{BORDER}"
          width="{WIDTH - BORDER * 2}"
          height="{HEIGHT - BORDER * 2}"
          fill="rgb({r}, {g}, {b})"/>
</svg>
'''

    file_path = output_folder / f"{name}.svg"
    file_path.write_text(svg, encoding="utf-8")

    print(f"Created: {name}.svg")

# Verification
created_files = [
    output_folder / f"{name}.svg"
    for name, r, g, b in colors
]

print()
print("=" * 50)
print(f"Colors in list:  {len(colors)}")
print(f"SVGs created:    {len(created_files)}")
print(f"Output folder:   {output_folder}")
print("=" * 50)

if all(file.exists() for file in created_files):
    print("SUCCESS: All 30 SVG files were created!")
else:
    print("ERROR: Some SVG files were not created.")