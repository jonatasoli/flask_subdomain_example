FROM python:3.10-slim
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8 && \
    apt update && \
    apt install -y libjpeg-dev zlib1g-dev python3-dev build-essential

# Set locale
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8
ENV LOC_ALL pt_BR.UTF-8
RUN locale-gen pt_BR.UTF-8

#Copy repository
ADD . /src
WORKDIR /src

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

RUN useradd -ms /bin/bash user

RUN chown -R user:user /src && \
    chmod -R 775 /src/

USER user

EXPOSE 5000
