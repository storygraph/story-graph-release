#!/usr/bin/env python3

import subprocess
import os
import argparse
import pathlib

YTT_CONFIG = "YTT_CONFIG"

def deploy(name, kubeConfig):
    appConfig = generate_config()
    deploy_app(name, appConfig, kubeConfig)


def generate_config():
    yttConfig = os.getenv(YTT_CONFIG)

    if len(yttConfig) == 0:
        raise Exception("Error: YTT_CONFIG env variable is not defined.")

    ytt = subprocess.Popen(['ytt', '-f', yttConfig], stdout=subprocess.PIPE)

    return ytt.stdout


def deploy_app(name, appConfig, kubeConfig):
    kapp = subprocess.Popen(['kapp', 'deploy', '-a', name, '-f-', '--yes', '--kubeconfig', kubeConfig], stdin=appConfig)

    kapp.wait()


def main():
    parser = argparse.ArgumentParser()

    optionalNamed = parser.add_argument_group("Optional named arguments")
    optionalNamed.add_argument("-a", help="Application name", default="storygraph")

    defaultKubeconfig = str(pathlib.Path.home()) + "/.kube/config"
    optionalNamed.add_argument("-k", help="Kubeconfig file path. Defaults to ~/.kube/config.", default=defaultKubeconfig)

    args = parser.parse_args()

    try:
        deploy(args.a, args.k)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
