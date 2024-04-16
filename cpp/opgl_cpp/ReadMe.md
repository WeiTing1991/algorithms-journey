opengl
Window


install CMake =  3.27.1

with cmake -G "Your Generator" -D CMAKE_C_COMPILER=gcc-4.2 -D CMAKE_CXX_COMPILER=g++-4.2 path/to/your/source

https://www.khronos.org/opengl/wiki/Related_toolkits_and_APIs

## Windows
GLFW 
https://learnopengl.com/Getting-started/Creating-a-window
https://www.glfw.org/download.html

GLAD
https://glad.dav1d.de/
sellect core and gl version

cmake -G "MinGW Makefiles" .


opengl_cpp_vscode_sample
Code example to test your VSCode C++ OpenGL setup with GLFW/GLAD.
Done on Windows, with the g++ compiler.

How to use this repo
watch this video.
main.cpp is an example file for GLFW/GLAD use (for OpenGL 3.3). Just copy its content if you don't already have a cpp file.
tasks.json is the VSCode file (put it in .vscode/) which tells how to build the exe. Change the paths given so they match your repo structure and compiler location.