import sys
from xisf import XISF

def strip(file_name):
    xisf = XISF(file_name)
    file_meta = xisf.get_file_metadata()
    ims_meta = xisf.get_images_metadata()
    im_data = xisf.read_image(0)

    XISF.write(
        file_name, im_data,
        creator_app = "XISF Strip",
        image_metadata = ims_meta[0],
        xisf_metadata = file_meta,
        codec='lz4hc', shuffle=True
    )

if len(sys.argv) < 2:
    print('XISF Strip v1.0 by Luca Padovani (2026)')
    print('Usage: xisfstrip file ...')
    sys.exit(-1)

for f in sys.argv[1:]:
    print('Processing', f, '...')
    strip(f)
