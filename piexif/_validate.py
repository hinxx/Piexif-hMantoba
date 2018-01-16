import struct
import copy

# from ._common import *
# from ._exceptions import InvalidImageDataError
from ._exif import *
# from piexif import _webp

def validate(exif_dict_original):
    """
    py:function:: piexif.validate(ifd_dict)

    Return exif data as dict. Keys(IFD name), be contained, are "0th", "Exif", "GPS", "Interop", "1st", and "thumbnail". Without "thumbnail", the value is dict(tag name/tag value). "thumbnail" value is JPEG as bytes.

    :param dict exif data({"0th":dict, "Exif":dict, "GPS":dict, "Interop":dict, "1st":dict, "thumbnail":bytes})
    :return: Exif data({"0th":dict, "Exif":dict, "GPS":dict, "Interop":dict, "1st":dict, "thumbnail":bytes})
    :rtype: dict
    """
    
    exif_dict = copy.deepcopy(exif_dict_original)
    for n, ifd in exif_dict.items():
#         print("IFD:", n, ifd)
        rmtags = []
        if ifd is not None:
            for tag in ifd:
                #print("IFD-TAG:", ifd, tag)
                if n == 'thumbnail':
                    continue
                if n == '_types':
                    continue
                if tag in TAGS[n]:
#                    print("Found tag", tag, "in IFD", n)
                    value = ifd[tag]
                    value_type = exif_dict['_types'][n][tag]
                    # print("Found tag", tag, "in IFD", n, "value", value, "type", value_type)
                    check_type = TAGS[n][tag]['type']
                    if value_type != check_type:
                        print(">>>> XXX: Tag types do not match:", value_type, check_type)
                        rmtags.append(tag)
                else:
                    print("Missing tag", tag, "in IFD", n)

            for tag in rmtags:
                del ifd[tag]

    return exif_dict
