project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(UNIX AND NOT APPLE)
    set(PTHREAD_LIB -pthread)
endif()

if(NOT MSVC)
    add_compile_options(-std=c++11)
endif()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS} ${PTHREAD_LIB})
