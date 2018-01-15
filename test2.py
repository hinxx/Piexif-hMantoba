import piexif
import sys

exif_dict = piexif.load(sys.argv[1])
#for ifd in ("0th", "Exif", "GPS", "1st"):
#    for tag in exif_dict[ifd]:
#        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

#print('Keys:', exif_dict.keys())
#print('Pre validate:', exif_dict['_types']['GPS'])
#print('Pre validate:', exif_dict['GPS'])
std_exif_dict = piexif.validate(exif_dict)
#print('Post fixup:', std_exif_dict['GPS'])

exif_bytes_1 = piexif.dump(exif_dict)
exif_bytes_2 = piexif.dump(exif_dict, True)

