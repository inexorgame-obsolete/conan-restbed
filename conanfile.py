from conans import ConanFile, CMake, tools

class RestbedConan(ConanFile):
    name = "restbed"
    version = "next"
    license = "AGPL"
    description = "RESTful server framework for C++11 applications"
    url = "https://github.com/Corvusoft/restbed"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "ssl": [True, False]
    }
    default_options = "shared=False","ssl=True"
    requires = "asio/next@nunojpg/ci"
    generators = "cmake"

    def source(self):
        self.run("git clone --depth 1 https://github.com/Corvusoft/restbed")
        self.run("cd restbed && git submodule update --depth 1 --init dependency/kashmir")
        tools.replace_in_file("restbed/CMakeLists.txt", "project( restbed CXX )", '''project( restbed CXX )
            include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
            conan_basic_setup()''')

    def requirements(self):
        if self.options.ssl:
            self.requires.add("OpenSSL/1.0.2k@lasote/stable", private=False)
        else:
            if "OpenSSL" in self.requires:
                del self.requires["OpenSSL"]

    def build(self):
        shared = "-DBUILD_SHARED=ON" if self.options.shared else "-DBUILD_SHARED=OFF"
        ssl = "-DBUILD_SSL=ON" if self.options.ssl else "-DBUILD_SSL=OFF"
        cmake = CMake(self)
        cmake.configure(source_dir="restbed", build_dir="./", args=[shared, ssl])
        cmake.build()

    def package(self):
        self.copy("restbed", dst="include", src="restbed/source")
        self.copy("*.hpp", dst="include", src="restbed/source")
        self.copy("librestbed.a", dst="lib", src="lib")
        self.copy("restbed.lib", dst="lib", src="lib")
        self.copy("librestbed.so*", dst="lib")
        self.copy("librestbed*dylib", dst="lib")
        
    def package_info(self):
        self.cpp_info.libs = ["restbed"]
