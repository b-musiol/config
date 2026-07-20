These are some important commands for cmake.

Assuming the source (the `CMakeLists.txt`) is in the current folder `.` and the build directory is in `./build`.

# TL;DR

Linux
```
cmake -S . -B build -D CMAKE_EXPORT_COMPILE_COMMANDS=ON -G "Ninja Multi-Config" -DCMAKE_CXX_COMPILER=g++ -DCMAKE_C_COMPILER=gcc
```

```
cmake --build build --target <my_target> --config Debug
cmake --build build --target <my_target> --config Release
```

Windows msvc
```
cmake -S . -B build -G "Visual Studio 18 2026" -DCMAKE_CXX_COMPILER=cl -DCMAKE_C_COMPILER=cl
```

Windows clang
```
cmake -S . -B build -D CMAKE_EXPORT_COMPILE_COMMANDS=ON -G "Ninja Multi-Config" -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang
```

```
cmake --build build --target <my_target> --config Debug
cmake --build build --target <my_target> --config Release
```

# Configuration

## Build type
```
$ cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
$ cmake -S . -B build -D CMAKE_BUILD_TYPE=Debug
```

## Generator
```
$ cmake -S . -B build -G Ninja
$ cmake -S . -B build -G "Visual Studio 18 2026"
```
Find available with
```
$ cmake --help
```

## Compiler

```
$ cmake -S . -B build -D CMAKE_CXX_COMPILER=g++ -D CMAKE_C_COMPILER=gcc
$ cmake -S . -B build -D CMAKE_CXX_COMPILER=cl -D CMAKE_C_COMPILER=cl
$ cmake -S . -B build -D CMAKE_CXX_COMPILER=clang++ -D CMAKE_C_COMPILER=clang
```

## Explicit compile commands

```
$ cmake -S . -B build -D CMAKE_EXPORT_COMPILE_COMMANDS=ON
```

## Arbitrary custom variables

```
$ cmake -S . -B build -D GENERATE_TESTS=ON -D VERBOSE=ON
```

# Compilation

## Showing all available targets

```
$ cmake --build build --target help
```

## Building a target

```
$ cmake --build build --target my_target
```

## Clean then build

```
$ cmake --build build --clean-first
```

## Parallel build

```
$ cmake --build build -j 4
```

all cores
```
$ cmake --build build -j $(nproc)                 # Linux
$ cmake --build build -j %NUMBER_OF_PROCESSORS%   # Windows

$ cmake --build build -j  # auto inference of all cores
```

# Testing

```
$ ctest --test-dir build
$ ctest --test-dir build --output-on-failure
```

# Installation

```
$ cmake --install build
$ cmake --install build  --prefix /path/to/install
```

# Clear cmake cache

```
cmake --fresh -S . -B build
```