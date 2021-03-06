import numpy as np
import pydicom
from PIL import Image

ds = pydicom.dcmread('path') # pre-existing dicom file
jpg_image = Image.open('path') # the PNG or JPG file to be replace

if jpg_image.mode == 'L':
       
    np_image = np.array(jpg_image.getdata(),dtype=np.uint8)
    ds.Rows = jpg_image.height
    ds.Columns = jpg_image.width
    ds.PhotometricInterpretation = "MONOCHROME1"
    ds.SamplesPerPixel = 1
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = np_image.tobytes()
    ds.save_as('result_gray.dcm')

elif jpg_image.mode == 'RGBA':

    np_image = np.array(jpg_image.getdata(), dtype=np.uint8)[:,:3]
    ds.Rows = jpg_image.height
    ds.Columns = jpg_image.width
    ds.PhotometricInterpretation = "RGB"
    ds.SamplesPerPixel = 3
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = np_image.tobytes()
    ds.save_as('result_rgb.dcm')