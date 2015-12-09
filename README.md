## mumble-docker

A dockerised [mumble](http://wiki.mumble.info/wiki/Main_Page) server easy to use and customisable.

This docker image is available on Docker Hub in the public repository [opiumozor/mumble](https://hub.docker.com/r/opiumozor/mumble/).

**Base image:** [ubuntu:14.04](https://hub.docker.com/_/ubuntu/)


### Basic usage

Pull the image from Docker hub:

* `docker pull opiumozor/mumble`

Start the server:

* `docker run -d -p 64738:64738 -p 64738:64738/udp opiumozor/mumble`

And it's working!

### Custom usage

You can add envoronement variable to the `docker run` command to custom your mumble server.

Here are the available variables:

| Variable         | Usage                    | Default         |
|:----------------:|:-----------------------: | :--------------:|       
| SERVER_MSG       | welcome message          | Welcome!        |
| SERVER_PASSWORD  | server access password   | no password     |
| MAX_USERS        | maximum number of users  | 50              |
| CHANNEL_NAME     | name of the root channel | Mumble server   |
| SU_PASSWORD      | superuser password       | see docker logs |

Example :

* `docker run -d -e SERVER_MSG='Welcome on my mumble server!' -e MAX_USERS=100 -p 64738:64738 -p 64738:64738/udp opiumozor/mumble`
