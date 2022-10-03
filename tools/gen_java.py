#!/usr/bin/env python3
# vim: ts=4 sw=4 sts=4 et ai

import os
import shutil

CLASS_HEADER = """
package {package};

class {klass_name}
"""

CLASS_FOOTER = """
}
"""


def generate_source(basedir, package, klass_name):
    output = os.path.join(*package.split('.'))
    output = os.path.join(basedir, output, klass_name + '.java')
    with open(output, 'w') as fp:
        fp.write(CLASS_HEADER.format(
            package=package,
            klass_name=klass_name
        ) + "{\n")
        for i in range(2000):
            fp.write(f"public int field{i} = 1;\n")

        fp.write(CLASS_FOOTER)


if __name__ == "__main__":
    package = "com.example"
    basedir = 'java/src/main/java'

    shutil.rmtree(basedir, True)
    os.makedirs(os.path.join(basedir, os.path.join(*package.split('.'))))

    for i in range(200):
        klass_name = f"Klass{i}"
        generate_source(basedir, package, klass_name)
