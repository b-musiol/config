With Windows, zed (rather clangd) often fails to find the C++ STL headers. To fix that, find

```
%LocalAppData%\clangd\config.yaml
```

and make sure it contains

```
CompileFlags:
  BuiltinHeaders: QueryDriver
  Compiler: clang++
```

If that still fails, make sure you actually have a C++ STL library installed. Whether from MSVC or libc++.

Make sure to use cmake with `CMAKE_EXPORT_COMPILE_COMMANDS=ON` to exclude the clangd issues with a missing `compile_commands.json` as well.
