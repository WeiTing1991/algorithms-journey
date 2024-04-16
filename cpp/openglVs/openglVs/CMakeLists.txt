# CMakeList.txt : CMake project for openglVs, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)
#cmake_minimum_required(VERSION 3.27.1)

# Add source to this project's executable.
add_executable (openglVs "openglVs.cpp" "openglVs.h")

project(${PROJECT_NAME} VERSION 0.1.0)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include/)
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/lib/)


# TODO: Add tests and install targets if needed.
