version: '3'

services:
  dask:
    image: quay.io/informaticslab/asn-serve:v1.0.0
    container_name: dask
    entrypoint: /bin/bash
    command: -c 'dask-worker ${scheduler_address}:8786 --nprocs $(grep -c ^processor /proc/cpuinfo) --nthreads 1 --host $(wget -qO- http://instance-data/latest/meta-data/local-ipv4)' 
    network_mode: host
    restart: always
  thredds:
    image: unidata/thredds-docker:4.6.10
    ports:
      - '80:8080'
      - '443:8443'
      - '8443:8443'
    container_name: thredds
    volumes:
      - /opt/tomcat/logs/:/usr/local/tomcat/logs/
      - /opt/thredds/logs/:/usr/local/tomcat/content/thredds/logs/
      - /opt/thredds/:/usr/local/tomcat/content/thredds
    environment:
      - TDS_CONTENT_ROOT_PATH=/usr/local/tomcat/content
      - THREDDS_XMX_SIZE=4G
      - THREDDS_XMS_SIZE=4G
      - TDS_HOST=http://34.252.8.97/
