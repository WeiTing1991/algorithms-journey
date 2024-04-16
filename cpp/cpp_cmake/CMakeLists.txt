cmake_minimum_required(VERSION 3.22.1)
project(Test_CMake VERSION 0.1.0)


add_executable(TestCMake src/main.cpp)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)

