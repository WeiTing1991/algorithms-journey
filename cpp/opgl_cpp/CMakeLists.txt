cmake_minimum_required(VERSION 3.22.1)

project(openglMiniProject VERSION 0.1.0)

add_executable(openglMiniProject src/main.cpp)


target_include_directories(openglMiniProject PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include/)
target_include_directories(openglMiniProject PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/lib/)



# target_link_directories()
# target_link_directories(openglMiniProject PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/lib/)

#target_compile_features(openglMini PRIVATE cxx_std_20)