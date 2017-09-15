[![Download](https://api.bintray.com/packages/nunojpg/conan-repo/restbed%3Anunojpg/images/download.svg)](https://bintray.com/nunojpg/conan-repo/restbed%3Anunojpg/_latestVersion)
[![Build Status](https://travis-ci.org/nunojpg/conan-restbed.svg?branch=master)](https://travis-ci.org/nunojpg/conan-restbed)
[![Build status](https://ci.appveyor.com/api/projects/status/d3m9un5jlbvd174f/branch/master?svg=true)](https://ci.appveyor.com/project/nunojpg/conan-restbed/branch/master)

# conan-restbed

## Reuse the packages

### Basic setup

    $ conan install restbed/next@nunojpg/ci
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    restbed/next@nunojpg/ci

    [options]
    #restbed:shared=true # default is false
    #restbed:ssl=false # default is true
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.