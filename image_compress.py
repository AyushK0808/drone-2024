# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from PIL import Image

# define a function for
# compressing an image
def compressMe(file, output_directory, verbose=False):

    # Get the path of the file
    filepath = os.path.join(os.getcwd(), file)

    # open the image
    picture = Image.open(filepath)

    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more
    # the value of quality variable
    # and lesser the compression
    compressed_filepath = os.path.join(output_directory, "Compressed_" + file)
    picture.save(compressed_filepath,
                 "JPEG",
                 optimize=True,
                 quality=10)
    return

# Define a main function
def main():
    verbose = False

    # checks for verbose flag
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-v":
            verbose = True

    # finds current working dir
    cwd = os.getcwd()

    # Specify the directory containing the images
    input_directory = cwd

    # Specify the directory to save compressed images
    output_directory = os.path.join(cwd, "Compressed_Images")

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    formats = ('.jpg', '.jpeg')

    # looping through all the files
    # in a specified directory
    for file in os.listdir(input_directory):
        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, output_directory, verbose)

    print("Done")

# Driver code
if __name__ == "__main__":
    main()
