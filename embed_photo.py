import base64
import mimetypes
from pathlib import Path
import sys
root = Path(__file__).resolve().parent
photo = Path(sys.argv[1]) if len(sys.argv)>1 else root/'profile.jpg'
mime = mimetypes.guess_type(photo.name)[0]
if mime not in ('image/jpeg','image/png'): raise ValueError('Use a JPG or PNG photograph.')
banner = root/'banner.svg'
s = banner.read_text(encoding='utf-8')
if 'PASTE_BASE64_IMAGE_HERE' not in s: raise ValueError('Placeholder not found; photo may already be embedded.')
banner.write_text(s.replace('PASTE_BASE64_IMAGE_HERE',f'data:{mime};base64,'+base64.b64encode(photo.read_bytes()).decode()),encoding='utf-8')
print('Photo embedded successfully.')
