FROM python:3.8-buster

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  DEBIAN_FRONTEND='noninteractive' \
  apt-get install -y --no-install-recommends \
  curl \
  sudo \
  unzip \
  vim \
  wget \
  zsh

COPY container/usr /usr

RUN useradd developer -m -d /home/developer -s /bin/bash \
  && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
  && adduser developer sudo

COPY container/entrypoint*.sh /
RUN chmod 755 /entrypoint*.sh

COPY container/home /home/developer
RUN chown -R developer:developer /home/developer && \
    export ZSH=/home/developer/.oh-my-zsh && \
    export ZDOTDIR=/home/developer && \
    /usr/local/ohmyzsh/tools/install.sh

COPY requirements.txt /tmp/requirements.txt
RUN \
  su -c 'pip install -r /tmp/requirements.txt' -l developer && \
  su -c 'pip install pytest' -l developer

COPY container/motd /motd
RUN chmod 666 /motd

COPY container/bin /home/developer/bin
RUN chown -R developer:developer /home/developer/bin && chmod 755 -R /home/developer/bin

ENV HOSTNAME crypto-notifier
ENV PATH /home/developer/bin:$PATH
USER developer
WORKDIR /home/developer
ENTRYPOINT ["/entrypoint.sh"]
CMD ["zsh"]