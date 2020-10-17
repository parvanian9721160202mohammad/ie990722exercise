import os
formats = [ 'utf8',     'bom-utf8',
            'ucs2le',   'bom-ucs2le', 
            'ucs2be',   'bom-ucs2be',
            'ucs4le',   'bom-ucs4le', 
            'ucs4be',   'bom-ucs4be', 
            'cp1256',
           ]

for name in formats:
    os.system('hexdump ' + name + '.txt | convert label:@- ' + name + '.jpg')