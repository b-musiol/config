To use `msvc` cleanly, there is a developer prompt `*.bat` file, which sets up all appropriate environment Variables. This can be opened in an external terminal, but it can also be opened in an internal zed terminal. There is a bad way to override the default terminal configuration. A better approach is to create a new task.

# How to set up a task for the msvc developer prompt

Find the path to the aforementioned batch file. It is usually set up as a link from where you can extract it.

`F1` -> `zed: open tasks`

Into the json list, add a new object

```json
{
    "label": "Open VS Developer Command Prompt",
    "command": "cmd.exe",
    "args": [
      "/k",
      "\"C:\\path\\to\\the\\appropriate\\VsDevCmd.bat\"",
    ],
    "use_new_terminal": true,
    "allow_concurrent_runs": true,
    "reveal": "always",
  }
```

Pay attention to whether you need to add a comma.

# How to launch

Now you can launch it as a task

`ALT + SHIFT + T` -> `Open VS Developer Command Prompt`

It will open within the `cwd` of the currently focused file (or the file explorer)
