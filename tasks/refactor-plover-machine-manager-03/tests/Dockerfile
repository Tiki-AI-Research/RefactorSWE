# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: ci-test-linux

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:tikiaihub-harbor-bundle-base-image-20261125@sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f

ARG REPO_URL="https://github.com/opensteno/plover"
ARG BASE_COMMIT="e87c4ef2982fcdeea587d2e612dff829fd331386"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="python" \
      io.envpipe.project.runtime.version="3.13.3" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
       libxkbcommon-dev \
       sudo \
    && rm -rf /var/lib/apt/lists/*

ARG ENVPIPE_RUNTIME_SPEC=python@3.13.3

RUN runuser -u agent -- env HOME=/home/agent MISE_PYTHON_COMPILE=1 mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=python \
    ENVPIPE_RUNTIME_VERSION="3.13.3"

RUN python --version 2>&1 \
    | grep -F 3.13.3

RUN git init /workspace/repo \
    && git -C /workspace/repo remote add origin "$REPO_URL" \
    && git -C /workspace/repo fetch --depth=1 origin "$BASE_COMMIT" \
    && git -C /workspace/repo checkout --detach FETCH_HEAD \
    && test "$(git -C /workspace/repo rev-parse HEAD)" = "$BASE_COMMIT" \
    && git -C /workspace/repo remote remove origin \
    && git -C /workspace/repo config core.hooksPath /dev/null \
    && git -C /workspace/repo reflog expire --expire=now --all \
    && git -C /workspace/repo gc --prune=now

# toolchain setup
RUN cd /workspace/repo && mkdir -p /usr/local/bin && printf '#!/bin/bash\nset -e\n_args=("$@")\nset --\ncd /workspace/repo\n. .github/workflows/ci/helpers.sh\nset -- "${_args[@]}"\n%s "$@"\n' apt_get_install > /usr/local/bin/apt_get_install && printf '#!/bin/bash\nset -e\n_args=("$@")\nset --\ncd /workspace/repo\n. .github/workflows/ci/helpers.sh\nset -- "${_args[@]}"\n%s "$@"\n' setup_python_env > /usr/local/bin/setup_python_env && printf '#!/bin/bash\nset -e\nif [ "$(id -u)" -eq 0 ]; then exec runuser -u agent -- /usr/local/bin/run_tests "$@"; fi\n_args=("$@")\nset --\ncd /workspace/repo\n. .github/workflows/ci/helpers.sh\nset -- "${_args[@]}"\n%s "$@"\n' run_tests > /usr/local/bin/run_tests && chmod 0755 /usr/local/bin/apt_get_install /usr/local/bin/setup_python_env /usr/local/bin/run_tests

# dependency installation
RUN cd /workspace/repo && python3 -m pip install -c reqs/constraints.txt -r reqs/dist.txt -r reqs/test.txt

# cache warmup
RUN cd /workspace/repo && python3 -m plover_build_utils.install_wheels --no-install -c reqs/constraints.txt -r reqs/dist.txt -r reqs/test.txt

# workspace cleanup
RUN cd /workspace/repo && rm -rf /root/.cache/pip

ENV \
    ENVPIPE_BASE_COMMIT="$BASE_COMMIT" \
    ENVPIPE_REPO_PATH="/workspace/repo" \
    GITHUB_ENV="/tmp/github_env" \
    SWEBENCH_REPO_PATH="/workspace/repo"

WORKDIR /workspace/repo

RUN cd /workspace/repo \
    && test "$(git rev-parse HEAD)" = "$BASE_COMMIT" \
    && test -z "$(git status --porcelain)"

RUN chown -R agent:agent /workspace/repo \
    && git config --system --add safe.directory /workspace/repo

CMD ["/bin/bash"]

COPY . /tests
