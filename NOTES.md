From https://www.loc.gov/preservation/digital/formats/fdd/fdd000017.shtml

The first two bytes of every JPEG stream are the Start Of Image (SOI) marker with
values 0xFF 0xD8.

Beyond that, JPEG images consist of a sequence of segments, each beginning with
a marker, each of which begins with a 0xFF byte followed by a byte indicating
what kind of marker it is.

One important type of segment is called the application data segment, designated
by application data markers, tagged with the prefix APP. APPs that appear near
the head of a file can be construed as signifiers, as suggested by the
Web documentation of the JHOVE JPEG module:

The file contains one of the following segments as the first segment of the file, not counting comments:

APP0 (0xE0) with identifier 0x4A, 0x46, 0x49, 0x46, 0x00, indicating a JFIF or JTIP file.
APP1 (0xE1) with identifier 0x45, 0x78, 0x69, 0x66, 0x00, 0x00, indicating an Exif file.
APP8 (0xE8) with identifier 0x53, 0x50, 0x49, 0x46, 0x46, 0x00, indicating a SPIFF file.
JPG7 (0xF7), also known as SOF55, indicating a JPEG-LS file." [Compiler's note: ISO/IEC 14495-1 associates SOF55, with "55" rendered as subscript, with 0xFFF7.]

From https://www.loc.gov/preservation/digital/formats/fdd/fdd000147.shtml

According to http://sylvana.net/jpegcrop/exifpatch.html:

"IJG based software writes a JFIF APP0 marker between SOI and Exif APP1 marker.
According to the Exif specification, the Exif APP1 marker has to follow immediately
after the SOI, just as the JFIF specification requires the same for the JFIF APP0
marker! Therefore a JPEG file cannot legally be both Exif and JFIF at the same time!'

