FROM jonduckworthdg/geopandas-base

ARG ADDITIONAL_PACKAGE
# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apt-get update -y && apt-get install  -y curl ${ADDITIONAL_PACKAGE} \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

ENV PATH=$PATH:/home/app/.local/bin
WORKDIR /home/app/
COPY index.py        .
COPY requirements.txt   .
RUN pip install -r requirements.txt
RUN mkdir -p function
ADD ./function  ./function
RUN pip install --user -r ./function/requirements.txt
RUN pip install -r ./function/Buffers/requirements.txt
ENV fprocess="python index.py"
EXPOSE 8080
HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1
CMD ["fwatchdog"]
