# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: platform-tests

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:tikiaihub-harbor-bundle-base-image-20261125@sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f

ARG REPO_URL="https://github.com/FyshOS/fynedesk"
ARG BASE_COMMIT="7bc2c75eda3aeff73b18450fe32a656bc4af27c4"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="go" \
      io.envpipe.project.runtime.version="1.21.13" \
      io.envpipe.project.runtime.provisioner="mise" \
      io.envpipe.harbor-bundle.digest="sha256:a2eec5fcbf6931070109e8783280d36f097060d5f5f91628385e008ab990979f"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       bc \
       ca-certificates \
       curl \
       dbus \
       dbus-x11 \
       gcc \
       git \
       libegl1-mesa-dev \
       libgl1-mesa-dev \
       libgles2-mesa-dev \
       libx11-dev \
       xorg-dev \
    && rm -rf /var/lib/apt/lists/*

ARG ENVPIPE_RUNTIME_SPEC=go@1.21.13

RUN runuser -u agent -- env HOME=/home/agent mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=go \
    ENVPIPE_RUNTIME_VERSION="1.21.13"

ENV GOROOT="/opt/envpipe/runtime"

RUN go version 2>&1 \
    | grep -F 1.21.13

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
RUN cd /workspace/repo && GOPATH_DIR="$(go env GOPATH)" && rm -rf "$GOPATH_DIR/src" && mkdir -p "$GOPATH_DIR/src/golang.org/x" "$GOPATH_DIR/src/github.com/mattn" && git clone --quiet --depth 1 --branch v0.15.0 https://github.com/golang/mod "$GOPATH_DIR/src/golang.org/x/mod" && git clone --quiet --depth 1 --branch v0.17.0 https://github.com/golang/tools "$GOPATH_DIR/src/golang.org/x/tools" && git init --quiet "$GOPATH_DIR/src/github.com/mattn/goveralls" && git -C "$GOPATH_DIR/src/github.com/mattn/goveralls" remote add origin https://github.com/mattn/goveralls && git -C "$GOPATH_DIR/src/github.com/mattn/goveralls" fetch --quiet --depth 1 origin 3c566820b1872aae28023f455893c0fd4f15198b && git -C "$GOPATH_DIR/src/github.com/mattn/goveralls" checkout --quiet --detach FETCH_HEAD && GO111MODULE=off go get github.com/mattn/goveralls

# cache warmup
RUN cd /workspace/repo && go mod download

# workspace cleanup
RUN cd /workspace/repo && rm -f coverage.out

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

COPY . /tests
