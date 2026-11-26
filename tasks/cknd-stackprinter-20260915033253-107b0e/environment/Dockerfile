# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: build-python-3-13

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:blacktt94-harbor-bundle-base-image-20261125@sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3

ARG REPO_URL="https://github.com/cknd/stackprinter"
ARG BASE_COMMIT="7a07a51a806e70c273a96071c87d19289bc0c69e"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="python" \
      io.envpipe.project.runtime.version="3.13.15" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
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
RUN cd /workspace/repo && python -m pip install --upgrade pip

RUN cd /workspace/repo && python -m pip install flake8 pytest

RUN cd /workspace/repo && python -m pip install numpy

RUN cd /workspace/repo && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# build
RUN cd /workspace/repo && python -m pip install -e .

ENV \
    ENVPIPE_BASE_COMMIT="$BASE_COMMIT" \
    ENVPIPE_REPO_PATH="/workspace/repo" \
    SWEBENCH_REPO_PATH="/workspace/repo"

WORKDIR /workspace/repo

RUN cd /workspace/repo \
    && test "$(git rev-parse HEAD)" = "$BASE_COMMIT" \
    && test -z "$(git status --porcelain)"

RUN chown -R agent:agent /workspace/repo \
    && git config --system --add safe.directory /workspace/repo

CMD ["/bin/bash"]
