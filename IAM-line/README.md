---
license: mit
language:
- en
task_categories:
- image-to-text
pretty_name: IAM-line

dataset_info:
  features:
    - name: image
      dtype: image
    - name: text
      dtype: string
  splits:
    - name: train
      num_examples: 6482
    - name: validation
      num_examples: 976
    - name: test
      num_examples: 2915
  dataset_size: 10373
tags:
  - atr
  - htr
  - ocr
  - modern
  - handwritten
---

# IAM - line level

## Table of Contents
- [IAM - line level](#iam-line-level)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)

## Dataset Description

- **Homepage:** [IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)
- **Paper:** [The IAM-database: an English sentence database for offline handwriting recognition](https://doi.org/10.1007/s100320200071)
- **Point of Contact:** [TEKLIA](https://teklia.com)

## Dataset Summary

The IAM Handwriting Database contains forms of handwritten English text which can be used to train and test handwritten text recognizers and to perform writer identification and verification experiments.

Note that all images are resized to a fixed height of 128 pixels.

### Languages

All the documents in the dataset are written in English.

## Dataset Structure

### Data Instances

```
{
  'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2467x128 at 0x1A800E8E190,
  'text': 'put down a resolution on the subject'
}
```

### Data Fields


- `image`: a PIL.Image.Image object containing the image. Note that when accessing the image column (using dataset[0]["image"]), the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the "image" column, i.e. dataset[0]["image"] should always be preferred over dataset["image"][0].
- `text`: the label transcription of the image.
