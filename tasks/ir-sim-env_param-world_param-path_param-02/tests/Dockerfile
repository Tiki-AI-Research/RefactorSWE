# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: ci-ubuntu-pytest

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:blacktt94-harbor-bundle-base-image-20261125@sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3

ARG REPO_URL="https://github.com/hanruihua/ir-sim"
ARG BASE_COMMIT="7c086d9902694c3c56f0e4259cc01c7fe7af6693"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="python" \
      io.envpipe.project.runtime.version="3.12.14" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
       xauth \
       xvfb \
    && rm -rf /var/lib/apt/lists/*

ARG ENVPIPE_RUNTIME_SPEC=python@3.12.14

RUN runuser -u agent -- env HOME=/home/agent MISE_PYTHON_COMPILE=1 mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=python \
    ENVPIPE_RUNTIME_VERSION="3.12.14"

RUN python --version 2>&1 \
    | grep -F 3.12.14

RUN git init /workspace/repo \
    && git -C /workspace/repo remote add origin "$REPO_URL" \
    && git -C /workspace/repo fetch --depth=1 origin "$BASE_COMMIT" \
    && git -C /workspace/repo checkout -B main FETCH_HEAD \
    && test "$(git -C /workspace/repo rev-parse HEAD)" = "$BASE_COMMIT" \
    && test "$(git -C /workspace/repo rev-parse refs/heads/main)" = "$BASE_COMMIT" \
    && git -C /workspace/repo remote remove origin \
    && git -C /workspace/repo config core.hooksPath /dev/null \
    && git -C /workspace/repo reflog expire --expire=now --all \
    && git -C /workspace/repo gc --prune=now

# dependency installation
RUN cd /workspace/repo && uv sync --locked --all-extras --dev

ENV \
    ENVPIPE_BASE_COMMIT="$BASE_COMMIT" \
    ENVPIPE_REPO_PATH="/workspace/repo" \
    SWEBENCH_REPO_PATH="/workspace/repo"

WORKDIR /workspace/repo

RUN cd /workspace/repo \
    && test "$(git rev-parse HEAD)" = "$BASE_COMMIT" \
    && test "$(git symbolic-ref --short HEAD)" = main \
    && test "$(git rev-parse refs/heads/main)" = "$BASE_COMMIT" \
    && test -z "$(git status --porcelain)"

RUN chown -R agent:agent /workspace/repo \
    && git config --system --add safe.directory /workspace/repo \
    && git config --system --add safe.directory /workspace/repo/.git

CMD ["/bin/bash"]

COPY . /tests
