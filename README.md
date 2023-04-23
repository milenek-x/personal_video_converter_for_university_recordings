# My Personal Video Converter for University Recordings

This is a simple desktop application that allows you to merge two WebM files into a single MP4 file. The app was built using Python and the tkinter library for the user interface, as well as the ffmpeg library for file conversion.
Prerequisites

Before using the WebM to MP4 Converter, you must have the following software installed on your computer:

- Python 3.x
* ffmpeg

You can download the latest version of Python from the [official website](https://www.python.org/downloads/), and ffmpeg from the [ffmpeg website](https://ffmpeg.org/download.html).
## Installation

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
3. Install the required Python packages by running the command pip install -r requirements.txt.
4. You can now run the app by executing the command python main.py.

## Usage

1. Launch the app by running the _main.py_ or simply click _My Personal Video Converter.exe_.
2. Click the "Select the webm file for the audio of the merged video" button and select the audio WebM file you want to merge.
3. Click the "Convert to mp3" button to start the conversion process.
4. Click the "Select the webm file for the video of the merged video" button and select the video WebM file you want to merge.
5. Click the "Merge Files" button and choose an output directory and enter a name for the output MP4 file.
6. Once the conversion is complete, the app will display a message indicating success or failure.

## Acknowledgments

- The [ffmpeg](https://ffmpeg.org/) library for its powerful and versatile video processing capabilities.
* The [tkinter](https://docs.python.org/3/library/tkinter.html) library for providing an easy-to-use GUI toolkit for Python.
