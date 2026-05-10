# First Steps

To initialize a project in C++ using cmake and googletest, do the following:

0. Create a central git repository, whether it is on github, gitlab, your own instance of git hoster, or just a bare repository on a central drive
1. Go to a folder where another folder can be created with your project.
2. `git clone` the empty central git repository.
3. Create a `.gitignore` file with `build*`, a `README.md` file with a short description and choose a license to put into a `LICENSE` file.
4. Commit these files as `Initial Commit`
5. Create a `src` folder. If you want a separate `include` folder, you can do that, too.
6. Create a `tests` folder
7. Decide if this is a library or an application and continue with the appropriate step 8.

# Product specific

When replacing placeholders, consider using Find and Replace (often `CTRL+H`).

## Library

If this is a library, do the following next:

8. Copy the `CMakeLists.txt` from `cpp_with_cmake_and_gtest/library` into the root folder.
9. Adjust all occurrences of `<project_name>`
10. Figure out the latest version of googletest and adjust it in `CMakeLists.txt`
11. Create a `<project_name>_test.cpp` file containing your tests in `tests` and add `#include <gtest/gtest.h>` into it.
12. Create a public header `<project_name>.hpp` file in `src` and decide on a simple namespace.
13. Create your first `.cpp` file in `src` including `<project_name>.hpp`
14. Write your first bit of functionality (or just a hello world if you want to test the configuration)
15. Write your first test in `tests/<project_name>_test.cpp` using `TEST(<suite_name>, <test_name>){}` referencing `src/<project_name>.hpp` (or just write another hello world into the test for configuration testing)
16. Add the `src/*.cpp` in `CMakeLists.txt` in the statement `add_library(<project_name> ...)` (possibly remove the placeholders)
17. Add the `tests/<project_name>_test.cpp` in `CMakeLists.txt` in the statement `add_executable(RunTests ...)` (possibly remove the placeholders)
18. `Configure` with cmake
19. `Build` with cmake
20. Run the previously created test.

Now simply add newly created `*.cpp` files to the `add_library(<project_name> ...)` command as you go.

The library builds into the `build` directory. Depending on the machine this can be a `.a` file or something else. You must use this with the public header. 


## Application

If this is an application, do the following next.

8. Copy the `CMakeLists.txt` from `cpp_with_cmake_and_gtest/executable` into the root folder.
9. Adjust all occurrences of `<project_name>`. Make sure not to overwrite the `_lib` suffixes if they are present!
10. Figure out the latest version of googletest and adjust it in `CMakeLists.txt`
11. Create a `<project_name>_test.cpp` file containing your tests in `tests` and add `#include <gtest/gtest.h>` into it.
12. Create your first actual functional `.cpp`/`.hpp` file pair in `src`
13. Create a `main.cpp` in `src` and put the main function in there. Include the just made `.hpp`.
14. Write your first bit of functionality (or just a hello world if you want to test the configuration)
15. Write your first test in `tests/<project_name>_test.cpp` using `TEST(<suite_name>, <test_name>){}` referencing the `.hpp` in `src` (or just write another hello world into the test for configuration testing)
16. Add the `src/*.cpp` in `CMakeLists.txt` in the statement `add_library(<project_name>_lib ...)` (possibly remove the placeholders)
17. Add the `src/main.cpp` in `add_executable(<project_name> ...)` (possibly remove the placeholders)
17. Add the `tests/<project_name>_test.cpp` in `CMakeLists.txt` in the statement `add_executable(RunTests ...)` (possibly remove the placeholders)
18. `Configure` with cmake
19. `Build` with cmake
20. Run the previously created test.
21. Run the executable

Now simply add newly created `*.cpp` files to the `add_library(<project_name>_lib ...)` command as you go. The `main.cpp` should best be light and only contain some argparse stuff, possibly even delegate that.

The executable builds into the `build` directory. You can just copy it out of there.

You could use the library that has been created, but it likely doesn't have a good include file, as it is just an intermediate thing.