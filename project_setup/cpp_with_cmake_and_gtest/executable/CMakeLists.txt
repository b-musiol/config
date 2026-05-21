cmake_minimum_required(VERSION 3.14)

project(<project_name>)

add_library(<project_name>_lib
  src/<path/to.cpp>
  src/<path/to.cpp>
  src/<path/to.cpp>
)
add_executable(<project_name> src/main.cpp)
target_link_libraries(<project_name> <project_name>_lib)
target_compile_features(<project_name>_lib PUBLIC cxx_std_20)
target_compile_features(<project_name> PUBLIC cxx_std_20)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.17.0  # Adjust to version you'd like
  DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(RunTests test/<path/to/test.cpp>)
target_link_libraries(RunTests <project_name>_lib GTest::gtest_main)
target_compile_features(RunTests PUBLIC cxx_std_20)

include(GoogleTest)

enable_testing()
gtest_discover_tests(RunTests)

