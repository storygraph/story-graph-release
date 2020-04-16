#!/usr/bin/env python3

import subprocess
import os
import argparse

YTT_CONFIG = "YTT_CONFIG"

def deploy(name):
    config = generateConfig()
    deployApp(name, config)


def generateConfig():
    yttConfig = os.getenv(YTT_CONFIG)

    if len(yttConfig) == 0:
        raise Exception("Error: YTT_CONFIG env variable is not defined.")

    ytt = subprocess.Popen(['ytt', '-f', yttConfig], stdout=subprocess.PIPE)

    return ytt.stdout


def deployApp(name, config):
    kapp = subprocess.Popen(['kapp', 'deploy', '-a', name, '-f-', '--yes'], stdin=config)

    kapp.wait()


def main():
    parser = argparse.ArgumentParser()

    optionalNamed = parser.add_argument_group("Optional named arguments")
    optionalNamed.add_argument("-a", help="Application name", default="storygraph")

    args = parser.parse_args()
    

    try:
        deploy(args.a)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
