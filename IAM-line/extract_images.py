import pyarrow.parquet as pq
from PIL import Image
import io
import os
import argparse

def extract_images_from_parquet(parquet_file, output_dir):
    # Read the parquet file
    table = pq.read_table(parquet_file)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get the columns
    text_column = table['text']
    image_column = table['image']

    for i in range(table.num_rows):
        # Get the image struct
        image_struct = image_column[i]
        image_bytes = image_struct['bytes'].as_py()
        image_path = image_struct['path'].as_py()

        # Load image from bytes
        image = Image.open(io.BytesIO(image_bytes))

        # Save the image
        # Use the path or generate a filename
        filename = os.path.basename(image_path) if image_path else f"image_{i}.png"
        output_path = os.path.join(output_dir, filename)
        image.save(output_path)

        print(f"Saved image: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract images from parquet file")
    parser.add_argument("parquet_file", help="Path to the parquet file")
    parser.add_argument("output_dir", help="Output directory for extracted images")

    args = parser.parse_args()

    extract_images_from_parquet(args.parquet_file, args.output_dir)