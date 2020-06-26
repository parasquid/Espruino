# Usage:
#
# Note: if you're in Linux you need to run socker with 'sudo'.
#   But honestly if you're on linux you should just save yourself
#   gigabytes of downloads and disk space and build Espruino directly.
#
# 1: Build the container image
#
#   docker build . -t img_name
#
# 2: Run container image so it builds espruino
#
#   docker run -e BOARD='PICO_R1_3' --name container_name img_name
# or
#   docker run -e BOARD='BANGLEJS' -e DFU_UPDATE_BUILD=1 --name container_name img_name
#
# This will run the container and save build results into the container's filesystem.
# Near the end of the build the filename will be displayed, for example espruino_2v00_pico_1r3.bin
#
# 3: Copy build results from the container into your filesystem
#
#   docker cp container_name:espruino/espruino_2v00_pico_1r3.bin ./
#

FROM ubuntu:xenial

WORKDIR /espruino

# Workaround add some stuff that the provision script uses
# in here so it doesn't have to use sudo
RUN apt-get update
RUN apt-get install -qq -y curl build-essential git unzip python wget libncurses-dev flex bison gperf python-pip python-setuptools cmake ninja-build ccache libffi-dev libssl-dev nano
RUN pip install --upgrade pip
RUN pip install pyserial
RUN pip install nrfutil
RUN pip install future
RUN pip install cryptography

COPY ./scripts /espruino/scripts
COPY ./targetlibs /espruino/targetlibs

# This ensures ALL dependencies are installed beforehand
RUN echo "cd /espruino && source scripts/provision.sh ALL" >> /root/.bashrc
RUN bash -c "source scripts/provision.sh ALL"

COPY . /espruino

ENV RELEASE 1
CMD ["bash", "-c", "source scripts/provision.sh ALL && make"]

