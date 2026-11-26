# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: main-backend-pytest

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:tikiaihub-harbor-bundle-base-image-20261125@sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f

ARG REPO_URL="https://github.com/claffin/cloudproxy"
ARG BASE_COMMIT="06f8a9d8f6f14867125b813a098243794f85d218"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="python" \
      io.envpipe.project.runtime.version="3.11.16" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       gcc \
       git \
       python3-dev \
    && rm -rf /var/lib/apt/lists/*

ARG ENVPIPE_RUNTIME_SPEC=python@3.11.16

RUN runuser -u agent -- env HOME=/home/agent MISE_PYTHON_COMPILE=1 mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=python \
    ENVPIPE_RUNTIME_VERSION="3.11.16"

RUN python --version 2>&1 \
    | grep -F 3.11.16

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
RUN cd /workspace/repo && python -m pip install --upgrade pip && pip install pytest pytest-mock pytest-cov && pip install -r requirements.txt

# cache warmup
RUN cd /workspace/repo && pip install -r requirements.txt

# workspace cleanup
RUN cd /workspace/repo && rm -rf .pytest_cache junit.xml coverage.xml htmlcov .coverage

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
