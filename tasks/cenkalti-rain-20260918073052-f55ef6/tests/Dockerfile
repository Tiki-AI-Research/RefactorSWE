# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: ci-test-job

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:blacktt94-harbor-bundle-base-image-20261125@sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3

ARG REPO_URL="https://github.com/cenkalti/rain"
ARG BASE_COMMIT="697380ffec04290679230d8d04636eb41c99e0a8"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="go" \
      io.envpipe.project.runtime.version="1.25.14" \
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

ARG ENVPIPE_RUNTIME_SPEC=go@1.25.14

RUN runuser -u agent -- env HOME=/home/agent mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=go \
    ENVPIPE_RUNTIME_VERSION="1.25.14"

ENV GOROOT="/opt/envpipe/runtime"

RUN go version 2>&1 \
    | grep -F 1.25.14

RUN git init /workspace/repo \
    && git -C /workspace/repo remote add origin "$REPO_URL" \
    && git -C /workspace/repo fetch --depth=1 origin "$BASE_COMMIT" \
    && git -C /workspace/repo checkout --detach FETCH_HEAD \
    && test "$(git -C /workspace/repo rev-parse HEAD)" = "$BASE_COMMIT" \
    && git -C /workspace/repo remote remove origin \
    && git -C /workspace/repo config core.hooksPath /dev/null \
    && git -C /workspace/repo reflog expire --expire=now --all \
    && git -C /workspace/repo gc --prune=now

ENV GOMODCACHE="/home/agent/go/pkg/mod" \
    GOCACHE="/home/agent/.cache/go-build"

RUN mkdir -p /home/agent/go/pkg/mod /home/agent/.cache/go-build /opt/go-cache/pkg \
    && ln -snf /home/agent/go/pkg/mod /opt/go-cache/pkg/mod \
    && chown -R agent:agent /home/agent /opt/go-cache /workspace/repo \
    && git config --system --add safe.directory /workspace/repo

# Download dependencies as the actual task user.
RUN runuser -u agent -- env \
    HOME=/home/agent \
    GOMODCACHE=/home/agent/go/pkg/mod \
    GOCACHE=/home/agent/.cache/go-build \
    /bin/bash -c 'cd /workspace/repo && go mod download'

# Compile production code and tests to warm up all dependencies.
RUN runuser -u agent -- env \
    HOME=/home/agent \
    GOMODCACHE=/home/agent/go/pkg/mod \
    GOCACHE=/home/agent/.cache/go-build \
    /bin/bash -c 'cd /workspace/repo && go build ./... && go test -run="^$" ./...'

# Verify compilation and go vet offline without network access.
RUN runuser -u agent -- env \
    HOME=/home/agent \
    GOMODCACHE=/home/agent/go/pkg/mod \
    GOCACHE=/home/agent/.cache/go-build \
    GOPROXY=off \
    GOTOOLCHAIN=local \
    /bin/bash -c 'cd /workspace/repo && go build ./... && go test -run="^$" ./... && go vet ./...'

ENV \
    ENVPIPE_BASE_COMMIT="$BASE_COMMIT" \
    ENVPIPE_REPO_PATH="/workspace/repo" \
    SWEBENCH_REPO_PATH="/workspace/repo"

WORKDIR /workspace/repo

RUN cd /workspace/repo \
    && test "$(git rev-parse HEAD)" = "$BASE_COMMIT" \
    && test -z "$(git status --porcelain)"

RUN chown -R agent:agent /home/agent /workspace/repo \
    && git config --system --add safe.directory /workspace/repo

CMD ["/bin/bash"]

COPY . /tests
RUN chmod +x /tests/test.sh /tests/grader.py \
    /tests/verifier/verifier.py /tests/verifier/hardgate.py
