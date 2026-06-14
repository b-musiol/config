To format every .cpp and .hpp file that is not in the `build` directory as a task in VSCode, the following tasks.json can be used

```
{
  "version": "2.0.0",
  "tasks": [
        {
            "label": "Clang Format All Files",
            "type": "shell",
            "command": "find . -type d -name build -prune -o -type f \\( -name \"*.cpp\" -o -name \"*.hpp\" \\) -exec clang-format -i {} +",
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "annotation": "Formats all C++ source and header files excluding the build directory"
            }
        }
    ]
}
```
