# Darwin all OK
# Windows fails shared builds - probably because source code doesn't export the DLL symbols.
# Linux all OK

from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(username="nunojpg")
    builder.add_common_builds(shared_option_name="restbed:shared", pure_c=False)
    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if (platform.system() == "Windows" and int(settings["compiler.version"]) >= 14 and options["restbed:shared"] == False or
                platform.system() == "Linux" or
                platform.system() == "Darwin"
            ):
            filtered_builds.append([settings, dict(options.items() + [('restbed:ssl', False)]), env_vars, build_requires])
            filtered_builds.append([settings, dict(options.items() + [('restbed:ssl', True)]), env_vars, build_requires])
    print "filtered_builds="
    print filtered_builds
    builder.builds = filtered_builds
    builder.run()
