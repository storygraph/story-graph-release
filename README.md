### :gift: Story-Graph release

This is a kubernetes release for Story-Graph

#### Prerequisites

You need to have the following tools installed:
- direnv
- kubectl
- k14s utilities, like ytt and kapp
You would need a Unix (or Unix-like) OS and a running Kubernetes cluster.

#### :rocket: Deployment

You can deploy like so:
```bash
./script/deploy.py# installs storygraph to your k8s cluster
kapp inspect -a storygraph  # details for storygraph installation
```

If your are running it locally then you might need some port-forwarding in order to be able to access your app:
```bash
# forward port to some free port on your machine
# by default:
# - SOME_FREE_PORT_ON_YOUR_MACHINE=8080
# - STORYGRAPH_PORT_ON_CLUSTER=8080
kubectl -n storygraph port-forward service/storygraph-service <SOME_FREE_PORT_ON_YOUR_MACHINE>:<STORYGRAPH_PORT_ON_CLUSTER>&
```

Now you should be able to access your Story Graph instance like so:
```bash
curl localhost:<SOME_FREE_PORT_ON_YOUR_MACHINE>/greet 
```