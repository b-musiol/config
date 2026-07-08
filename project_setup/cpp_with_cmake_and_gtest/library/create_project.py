from pathlib import Path
import shutil
from datetime import datetime

current_year = str(datetime.now().year)

debug = True

cwd = Path(".")
# if debug:
#     cwd = cwd / "test"
#     cwd.mkdir(exist_ok=True)
#     shutil.rmtree(cwd)
#     cwd.mkdir()

cpp_standard_yr = 20


def head_comment(header: bool, name: str, description: str, author: str, email: str):
    text = f"""/**
 * {name}{f" - Header" if header else ""}
 * {description}
 *
 * Author: {author} ({email})
 *
 * See LICENSE
 */
    """
    return text


def mit_license(author_name):
    return f"""
MIT License

Copyright (c) {current_year} {author_name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


text_gitignore = """
.vscode/

# Prerequisites
*.d

# Compiled Object files
*.slo
*.lo
*.o
*.obj

# Precompiled Headers
*.gch
*.pch

# Linker files
*.ilk

# Debugger Files
*.pdb

# Compiled Dynamic libraries
*.so
*.dylib
*.dll
*.so.*


# Fortran module files
*.mod
*.smod

# Compiled Static libraries
*.lai
*.la
*.a
*.lib

# Executables
*.exe
*.out
*.app

# Build directories
build/
Build/
build-*/

# CMake generated files
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
install_manifest.txt
compile_commands.json

# Temporary files
*.tmp
*.log
*.bak
*.swp

# vcpkg
vcpkg_installed/

# debug information files
*.dwo

# test output & cache
Testing/
.cache/

"""


def text_cmakelists(
    project_name: str,
    cpp_standard: int = cpp_standard_yr,
    gtest_tag: str = "v1.17.0",
    cmake_min_version: str = "3.14",
):
    return f"""
cmake_minimum_required(VERSION {cmake_min_version})

project({project_name})

option({project_name}_BUILD_TESTS "Build tests for {project_name}" ON)

add_library({project_name}
  src/{project_name}.cpp
  src/Core.cpp
)
target_compile_features({project_name} PUBLIC cxx_std_{cpp_standard})

set(CMAKE_CXX_STANDARD {cpp_standard})
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(APPLE)
    find_library(ICONV_LIB iconv REQUIRED)
    target_link_libraries({project_name} PRIVATE ${{ICONV_LIB}})
endif()

include(FetchContent)


if({project_name}_BUILD_TESTS)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        {gtest_tag}  # Adjust to version you'd like
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(RunTests_{project_name} tests/{project_name}_tests.cpp)
target_link_libraries(RunTests_{project_name} {project_name} GTest::gtest_main)
target_compile_features(RunTests_{project_name} PUBLIC cxx_std_{cpp_standard})
target_compile_definitions(RunTests_{project_name} PRIVATE
    TEST_DATA_DIR="${CMAKE_CURRENT_SOURCE_DIR}/tests"
)

include(GoogleTest)
enable_testing()
gtest_discover_tests(RunTests_{project_name})
endif()

"""


def public_hpp(
    project_name: str,
    project_description: str,
    main_class_name: str,
    author_name: str,
    author_email: str,
):
    return f"""{head_comment(True, project_name, project_description, author_name, author_email)}

#ifndef _{project_name.upper()}_PUBLIC_HPP_
#define _{project_name.upper()}_PUBLIC_HPP_

#include <memory>

namespace {project_name} {{

class {main_class_name} {{
  public:
    {main_class_name}();
    ~{main_class_name}();

  private:
    // PIMPL
    struct Core;
    std::unique_ptr<Core> m_core;
    
}};

}}; // namespace {project_name}

#endif // _{project_name.upper()}_PUBLIC_HPP_
"""


def main_cpp(
    project_name: str,
    project_description: str,
    main_class_name: str,
    author_name: str,
    author_email: str,
):
    return f"""{head_comment(False, project_name, project_description, author_name, author_email)}

#include "../include/{project_name}/{project_name}.hpp"
#include "../include_private/Core.hpp"

#include <memory>

using namespace {project_name};

{main_class_name}::{main_class_name}() :
m_core(std::make_unique<{main_class_name}::Core>())
{{

}}

{main_class_name}::~{main_class_name}()
{{

}}
"""


def core_hpp(
    project_name: str,
    project_description: str,
    main_class_name: str,
    author_name: str,
    author_email: str,
):
    return f"""{head_comment(True, f"{project_name} Core", project_description, author_name, author_email)}

#ifndef _{project_name.upper()}_CORE_HPP_
#define _{project_name.upper()}_CORE_HPP_

#include "../include/{project_name}/{project_name}.hpp"

using namespace {project_name};

struct {main_class_name}::Core
{{
    Core();
    ~Core();
}};

#endif // _{project_name.upper()}_CORE_HPP_
"""


def core_cpp(
    project_name: str,
    project_description: str,
    main_class_name: str,
    author_name: str,
    author_email: str,
):
    return f"""{head_comment(False, f"{project_name} Core", project_description, author_name, author_email)}

#include "../include_private/Core.hpp"

using namespace {project_name};

{main_class_name}::Core::Core()
{{

}}

{main_class_name}::Core::~Core()
{{

}}
"""


def tests_cpp(
    project_name: str,
    project_description: str,
    main_class_name: str,
    author_name: str,
    author_email: str,
):
    return f"""{head_comment(False, f"{project_name} Tests", project_description, author_name, author_email)}

#include "../include/{project_name}/{project_name}.hpp"

#include <gtest/gtest.h>

using namespace {project_name};

// just here for compilation test. Replace with real tests.
TEST(s1, a1){{
    {main_class_name} instance;
    int a = 0;
    EXPECT_EQ(a, 0);
}}
"""


text_clangdfile = """CompileFlags:
  Add: [-std=c++20]
"""

text_clang_format_file = """Language: Cpp
BasedOnStyle: Microsoft
ColumnLimit: 80

AlignConsecutiveAssignments: true

BreakBeforeBraces: Custom
BraceWrapping:
  AfterFunction: true
  BeforeCatch: true
  BeforeElse: true

AllowAllParametersOfDeclarationOnNextLine: false
AllowAllArgumentsOnNextLine: false

BinPackParameters: false
BinPackArguments: false

AllowShortIfStatementsOnASingleLine: AllIfsAndElse
AllowShortLoopsOnASingleLine: true
AllowShortCaseLabelsOnASingleLine: true

AllowShortBlocksOnASingleLine: true
AllowShortFunctionsOnASingleLine: true
AllowShortLambdasOnASingleLine: true
"""

if __name__ == "__main__":
    project_name = input(
        "What would you like to call your project?\nIf you use whitespaces, they are converted to underscores (_).\nI recommend only using alphanumeric characters and starting with a letter.\nThe name will also be used as a folder name.\nGood names are simple.\nEnter name here: "
    )
    project_name = project_name.replace(" ", "_")
    cwd = cwd / project_name

    project_description = input(
        "What would you describe your project as if you only had one paragraph to do so?\nEnter description here: "
    )

    main_class_name = input(
        f"I will call your outer namespace like your project name.\nHow would you like your main class to be called?\nIt can be the same as your project name, but do you actually want to call your class like the following?\n{project_name}::{project_name}\nIf this is okay, then just enter nothing.\nEnter class name here: "
    )
    if len(main_class_name) < 1:
        main_class_name = project_name

    author_name = input(
        "What is your name?\nIf you don't like entering this, you can enter nothing or nonsense.\nIt will however mess up formatting and the license text.\nEnter name here: "
    )
    author_email = input(
        "What is your email?\nIf you don't like entering this, you can enter nothing or nonsense.\nIt will however mess up formatting and the license text.\nEnter email here: "
    )
    is_MIT_ok = ""
    while is_MIT_ok not in ["y", "Y", "yes", "YES", "n", "N", "no", "NO"]:
        is_MIT_ok = input(
            "Is using the MIT License okay?\nIf yes, the LICENSE file will be pre-populated with the MIT-License\nIf no, the LICENSE file will be empty and you need to sort this out yourself.\nRemember: YOU must be comfortable with using the license, not the others!\nEnter [y/yes/n/no]: "
        )

    src_folder = cwd / "src"
    src_folder.mkdir(parents=True)
    include_folder = cwd / "include" / project_name
    include_folder.mkdir(parents=True)
    include_private_folder = cwd / "include_private"
    include_private_folder.mkdir(parents=True)
    docs_folder = cwd / "docs"
    docs_folder.mkdir(parents=True)
    data_folder = cwd / "data"
    data_folder.mkdir(parents=True)
    tests_folder = cwd / "tests"
    tests_folder.mkdir(parents=True)

    with open(cwd / ".gitignore", "w") as gitignore:
        gitignore.write(text_gitignore)
    with open(cwd / "README.md", "w") as readme:
        readme.write(f"# {project_name}\n\n{project_description}")
    with open(cwd / "CMakeLists.txt", "w") as cmakelists:
        cmakelists.write(text_cmakelists(project_name, cpp_standard=cpp_standard_yr))
    with open(cwd / "LICENSE", "w") as license:
        if is_MIT_ok in ["y", "Y", "yes", "YES"]:
            license.write(mit_license(author_name))
        else:
            license.write(" ")
            print("  Remember to choose a LICENSE!")

    with open(include_folder / f"{project_name}.hpp", "w") as project_hpp:
        project_hpp.write(
            public_hpp(
                project_name,
                project_description,
                main_class_name,
                author_name,
                author_email,
            )
        )

    with open(src_folder / f"{project_name}.cpp", "w") as project_cpp:
        project_cpp.write(
            main_cpp(
                project_name,
                project_description,
                main_class_name,
                author_name,
                author_email,
            )
        )

    with open(include_private_folder / "Core.hpp", "w") as project_core_hpp:
        project_core_hpp.write(
            core_hpp(
                project_name,
                project_description,
                main_class_name,
                author_name,
                author_email,
            )
        )

    with open(src_folder / "Core.cpp", "w") as project_core_cpp:
        project_core_cpp.write(
            core_cpp(
                project_name,
                project_description,
                main_class_name,
                author_name,
                author_email,
            )
        )

    with open(tests_folder / f"{project_name}_tests.cpp", "w") as project_Tests_cpp:
        project_Tests_cpp.write(
            tests_cpp(
                project_name,
                project_description,
                main_class_name,
                author_name,
                author_email,
            )
        )

    with open(cwd / ".clangd", "w") as clangdfile:
        clangdfile.write(text_clangdfile)

    with open(cwd / ".clang-format", "w") as clangformatfile:
        clangformatfile.write(text_clang_format_file)

    print(
        "You did it! Now just run `git init`, delete this python file, and you're good to go."
    )
