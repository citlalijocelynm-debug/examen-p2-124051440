FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    python3 \
    python3-pip \
    wget \
    tar \
    openssh-server \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz \
    && tar -xzf hadoop-$HADOOP_VERSION.tar.gz -C /opt/ \
    && mv /opt/hadoop-$HADOOP_VERSION $HADOOP_HOME \
    && rm hadoop-$HADOOP_VERSION.tar.gz

RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 600 ~/.ssh/authorized_keys

EXPOSE 22
CMD service ssh start && tail -f /dev/null
