import sys
from xisf import XISF
from pathlib import Path

dry_run = False

if len(sys.argv) < 3:
    print('XISF Filter Editor v1.0 (2026) Luca Padovani')
    print('Usage: edit-filter filter file...')
    sys.exit(-1)

new_filter = sys.argv[1]

def update(file_name):
    xisf = XISF(file_name)
    file_meta = xisf.get_file_metadata()
    ims_meta = xisf.get_images_metadata()
    im_data = xisf.read_image(0)
    old_filter = ims_meta[0]['XISFProperties']['Instrument:Filter:Name']['value']
    if old_filter != new_filter:
        ims_meta[0]['XISFProperties']['Instrument:Filter:Name']['value'] = new_filter
        XISF.write(
            file_name, im_data,
            image_metadata = ims_meta[0],
            xisf_metadata = file_meta,
            codec = 'lz4hc', shuffle = True
        )
        print(old_filter, '=>', new_filter)
    else:
        print('no change')

for f in sys.argv[2:]:
    print('Processing', f, '... ', end = '')
    update(f)
