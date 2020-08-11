import sys
import os
from PIL import Image
import pyheif

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 convert_heic.py <input directory>")
		sys.exit(64)
	input_dir = os.path.abspath(sys.argv[1])
	for picture in os.listdir(input_dir):
		if picture.endswith(".HEIC"):
			try:
				print(f"{input_dir}/{picture}")
				heif = pyheif.read_heif(f"{input_dir}/{picture}")
				img = Image.frombytes(mode=heif.mode, size=heif.size, data=heif.data)
				img.save(f"{picture[:-5]}.jpg", format="jpeg")
			except:
				print("failed for some reason")
				continue
if __name__ == "__main__":
	main()
