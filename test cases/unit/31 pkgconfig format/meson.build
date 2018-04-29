project('pkgformat', 'c',
  version : '1.0')

pkgg = import('pkgconfig')

l = shared_library('something', 'somelib.c')

pkgg.generate(libraries: l,
              version: '1.0',
              name: 'libsomething',
              description: 'A library that does something',
              requires: 'gobject-2.0 >= 2.54, gio-2.0 >= 2.54')
