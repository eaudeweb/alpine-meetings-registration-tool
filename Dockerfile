FROM alpine
MAINTAINER "Eau de Web" <cornel.nitu@eaudeweb.ro>

ENV MRT_SRC=/var/local/meetings

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    freetype-dev \
    musl-dev 

RUN runDeps="curl vim \
             make g++ \
             linux-headers \
             alpine-sdk  netcat-openbsd  \
             libpq  libxml2-dev libjpeg-turbo-dev \
             jpeg-dev libxrender libxrender-dev  fontconfig libxtst" \
 && apk update \
 && apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
 && apk add postgresql-dev \
 && apk add   $runDeps \
 && curl -o /tmp/wkhtmltopdf.tgz -SL https://svn.eionet.europa.eu/repositories/Zope/trunk/wk/wkhtmltopdf-0.12.2.4.tgz \
 && tar -zxvf /tmp/wkhtmltopdf.tgz -C /tmp/ \
 && mv -v /tmp/wkhtmltopdf /usr/bin/ \
 && rm -vrf /var/lib/apt/lists/* \
 && rm -vrf /tmp/*

COPY requirements-dep.txt  requirements-dev.txt  requirements.txt   $MRT_SRC/
WORKDIR $MRT_SRC

RUN     pg_config --bindir \
	&& pip install -U pip \
	&& pip install -U setuptools \
 	&& pip install -U setuptools \
    	&& pip install -r requirements-dep.txt \
    	&& mkdir -p $MRT_SRC/instance/files

COPY . $MRT_SRC/

RUN pybabel compile -d mrt/translations \
 && mv settings.example instance/settings.py \
 && mv ./docker/docker-entrypoint.sh /bin/

ENTRYPOINT ["docker-entrypoint.sh"]
