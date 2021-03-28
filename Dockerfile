FROM centos:centos7

RUN yum update -y && \
  yum groupinstall -y 'Development Tools' && \
  yum install -y cmake clang libssl-dev yum-utils && \
  debuginfo-install -y glibc

WORKDIR /home/cppdev/googletest

RUN curl -OL https://github.com/google/googletest/archive/release-1.10.0.tar.gz \
  && tar xzf release-1.10.0.tar.gz \
  && cd googletest-release-1.10.0 \
  && cmake . \
  && make