cmake_minimum_required(VERSION 3.14)

project(<project_name>)

add_library(<project_name>_lib
  src/<path/to.cpp>
  src/<path/to.cpp>
  src/<path/to.cpp>
)
add_executable(<project_name> src/main.cpp)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.17.0  # Adjust to version you'd like
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(RunTests test/<path/to/test.cpp>)
target_link_libraries(RunTests <project_name>_lib GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(RunTests)

enable_testing()
