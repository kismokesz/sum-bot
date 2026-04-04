      aiohttp/_websocket.c:2741:9: note: in expansion of macro ‘__PYX_PY_DICT_LOOKUP_IF_MODIFIED’
Menu
       2741 |         __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      aiohttp/_websocket.c: In function ‘__Pyx_PyInt_As_long’:
      aiohttp/_websocket.c:3042:53: error: ‘PyLongObject’ {aka ‘struct _longobject’} has no member named ‘ob_digit’
       3042 |             const digit* digits = ((PyLongObject*)x)->ob_digit;
            |                                                     ^~
      aiohttp/_websocket.c:3097:53: error: ‘PyLongObject’ {aka ‘struct _longobject’} has no member named ‘ob_digit’
       3097 |             const digit* digits = ((PyLongObject*)x)->ob_digit;
            |                                                     ^~
      aiohttp/_websocket.c:3183:27: error: too few arguments to function ‘_PyLong_AsByteArray’
       3183 |                 int ret = _PyLong_AsByteArray((PyLongObject *)v,
            |                           ^~~~~~~~~~~~~~~~~~~
      In file included from /opt/render/project/python/Python-3.14.3/include/python3.14/longobject.h:171,
                       from /opt/render/project/python/Python-3.14.3/include/python3.14/Python.h:92:
      /opt/render/project/python/Python-3.14.3/include/python3.14/cpython/longobject.h:84:17: note: declared here
         84 | PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
            |                 ^~~~~~~~~~~~~~~~~~~
Failed to build aiohttp
      aiohttp/_websocket.c: In function ‘__Pyx_PyInt_As_int’:
      aiohttp/_websocket.c:3238:53: error: ‘PyLongObject’ {aka ‘struct _longobject’} has no member named ‘ob_digit’
       3238 |             const digit* digits = ((PyLongObject*)x)->ob_digit;
            |                                                     ^~
      aiohttp/_websocket.c:3293:53: error: ‘PyLongObject’ {aka ‘struct _longobject’} has no member named ‘ob_digit’
       3293 |             const digit* digits = ((PyLongObject*)x)->ob_digit;
            |                                                     ^~
      aiohttp/_websocket.c:3379:27: error: too few arguments to function ‘_PyLong_AsByteArray’
       3379 |                 int ret = _PyLong_AsByteArray((PyLongObject *)v,
            |                           ^~~~~~~~~~~~~~~~~~~
      /opt/render/project/python/Python-3.14.3/include/python3.14/cpython/longobject.h:84:17: note: declared here
         84 | PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
            |                 ^~~~~~~~~~~~~~~~~~~
      aiohttp/_websocket.c: In function ‘__Pyx_PyIndex_AsSsize_t’:
      aiohttp/_websocket.c:3744:45: error: ‘PyLongObject’ {aka ‘struct _longobject’} has no member named ‘ob_digit’
       3744 |     const digit* digits = ((PyLongObject*)b)->ob_digit;
            |                                             ^~
      error: command '/usr/bin/gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for aiohttp
[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
error: failed-wheel-build-for-install
× Failed to build installable wheels for some pyproject.toml based projects
╰─> aiohttp
==> Build failed 😞
