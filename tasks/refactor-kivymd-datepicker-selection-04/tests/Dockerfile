# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: ci-test-ubuntu-pytest

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:tikiaihub-harbor-bundle-base-image-20261125@sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f

ARG REPO_URL="https://github.com/kivymd/KivyMD"
ARG BASE_COMMIT="4a2617ea24e13ef2540c37edb95a54ef02e78707"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="python" \
      io.envpipe.project.runtime.version="3.13.15" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       ca-certificates \
       curl \
       git \
       gstreamer1.0-alsa \
       gstreamer1.0-plugins-base \
       libavcodec-dev \
       libavformat-dev \
       libcairo2-dev \
       libgl1-mesa-dev \
       libgles2-mesa-dev \
       libgstreamer1.0-dev \
       libjpeg-dev \
       libmtdev-dev \
       libsdl2-dev \
       libsdl2-image-dev \
       libsdl2-mixer-dev \
       libsdl2-ttf-dev \
       libsmpeg-dev \
       libswscale-dev \
       libtiff5-dev \
       libx11-dev \
       pkg-config \
       pulseaudio \
       sudo \
       xsel \
       xvfb \
    && rm -rf /var/lib/apt/lists/*

ARG ENVPIPE_RUNTIME_SPEC=python@3.13.15

RUN runuser -u agent -- env HOME=/home/agent MISE_PYTHON_COMPILE=1 mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=python \
    ENVPIPE_RUNTIME_VERSION="3.13.15"

RUN python --version 2>&1 \
    | grep -F 3.13.15

RUN git init /workspace/repo \
    && git -C /workspace/repo remote add origin "$REPO_URL" \
    && git -C /workspace/repo fetch --depth=1 origin "$BASE_COMMIT" \
    && git -C /workspace/repo checkout --detach FETCH_HEAD \
    && test "$(git -C /workspace/repo rev-parse HEAD)" = "$BASE_COMMIT" \
    && git -C /workspace/repo remote remove origin \
    && git -C /workspace/repo config core.hooksPath /dev/null \
    && git -C /workspace/repo reflog expire --expire=now --all \
    && git -C /workspace/repo gc --prune=now

# dependency installation
RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && python -m pip install --upgrade pip setuptools wheel

RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && python -m pip install --upgrade cython pytest pytest-cov pytest_asyncio pytest-timeout coveralls pillow docutils pygments "pyinstaller[hook_testing]" sphinx sphinxcontrib-blockdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-nwdiag

RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && python -m pip install --upgrade "kivy==${KIVY_VERSION}"

RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && python -m pip install -e .

# cache warmup
RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && python -m pip download --dest /tmp/pip-warmup cython pytest pytest-cov pytest_asyncio pytest-timeout coveralls pillow docutils pygments "pyinstaller[hook_testing]" "kivy==${KIVY_VERSION}" setuptools wheel pip sphinx sphinxcontrib-blockdiag sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-nwdiag

# workspace cleanup
RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && git checkout -- kivymd/_version.py

RUN cd /workspace/repo && export KIVY_VERSION="2.3.1" && rm -rf /tmp/pip-warmup

ENV \
    DISPLAY=":99.0" \
    ENVPIPE_BASE_COMMIT="$BASE_COMMIT" \
    ENVPIPE_REPO_PATH="/workspace/repo" \
    KIVY_VERSION="2.3.1" \
    SWEBENCH_REPO_PATH="/workspace/repo"

WORKDIR /workspace/repo

RUN cd /workspace/repo \
    && test "$(git rev-parse HEAD)" = "$BASE_COMMIT" \
    && test -z "$(git status --porcelain)"

RUN chown -R agent:agent /workspace/repo \
    && git config --system --add safe.directory /workspace/repo

CMD ["/bin/bash"]

COPY . /tests
