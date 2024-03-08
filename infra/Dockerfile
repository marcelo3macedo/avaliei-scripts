FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        libssl-dev

RUN curl https://pyenv.run | bash

ENV PATH="/root/.pyenv/bin:/root/.pyenv/shims:${PATH}"

RUN pyenv install 3.9.0 && \
    pyenv global 3.9.0

ENV PYENV_VIRTUALENV_SKIP_EXISTING 1

RUN pyenv virtualenv 3.9.0 myenv

RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc && \
    echo 'pyenv activate myenv' >> ~/.bashrc

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "src/main.py"]
#CMD tail -f /dev/null
