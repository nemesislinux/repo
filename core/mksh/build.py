import gf.tools

name = "mksh"
description = "MirBSD Korn Shell"
version = "R59b"

sources = ["https://github.com/MirBSD/mksh/archive/mksh-{}.tar.gz".format(version)]

def configure():
    pass

def build():
    env = gf.tools.env()
    env.add("CC", "tcc")

    gf.tools.unpack("mksh-{}.tar.gz".format(version), "mksh")
    gf.tools.run("cd mksh && ./Build.sh", env=env)

def install(target):
    gf.tools.mv("mksh/mksh", "{}/bin/mksh".format(target))