# syntax=docker/dockerfile:1.7
# Generated environment definition
# Generator: dockerfile-generator.v1
# Candidate: pr-release-check-library-gate

FROM --platform=linux/amd64 docker.io/tikiaiteam/refactor:blacktt94-harbor-bundle-base-image-20261125@sha256:c3b4c5a85cc1b8b1602e72d70bf655483735dd1ad5591f51b1ccb23781127ef3

ARG REPO_URL="https://github.com/amll-dev/applemusic-like-lyrics"
ARG BASE_COMMIT="5c0959686d18ca185b81811added3cd31299569f"

LABEL org.opencontainers.image.source="$REPO_URL" \
      org.opencontainers.image.revision="$BASE_COMMIT" \
      io.envpipe.image.generator="dockerfile-generator.v1" \
      org.opencontainers.image.title="Repository runtime environment" \
      io.envpipe.project.runtime.family="node" \
      io.envpipe.project.runtime.version="24.21.0" \
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

ARG ENVPIPE_RUNTIME_SPEC=node@24.21.0

RUN runuser -u agent -- env HOME=/home/agent mise install --yes "$ENVPIPE_RUNTIME_SPEC" \
    && runtime_dir="$(runuser -u agent -- env HOME=/home/agent mise where "$ENVPIPE_RUNTIME_SPEC")" \
    && test -d "$runtime_dir" \
    && ln -s "$runtime_dir" /opt/envpipe/runtime \
    && basename "$runtime_dir" > /opt/envpipe/runtime-install-version \
    && chown root:root /opt/envpipe/runtime-install-version

ENV PATH="/opt/envpipe/runtime/bin:${PATH}" \
    ENVPIPE_RUNTIME_FAMILY=node \
    ENVPIPE_RUNTIME_VERSION="24.21.0"

RUN node --version 2>&1 \
    | grep -F 24.21.0

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
RUN cd /workspace/repo && corepack enable pnpm && corepack install --global pnpm@11.21.0 && pnpm --version

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

# Pinned tools for the repository's complete unit-test suite.
RUN mkdir -p /opt/amll-test-deps \
    && cd /opt/amll-test-deps \
    && npm init -y >/dev/null \
    && npm install --no-audit --no-fund vitest@4.1.10 @xmldom/xmldom@0.9.10 pako@3.0.1 @ungap/structured-clone@1.3.3 bezier-easing@3.0.1 deep-freeze@0.0.1 gl-matrix@4.0.0-beta.2
ENV PATH="/opt/amll-test-deps/node_modules/.bin:${PATH}"
RUN ln -s /opt/amll-test-deps/node_modules /workspace/repo/node_modules

RUN git config --system --add safe.directory /workspace/repo/.git

RUN printf '\n/node_modules\n' >> /workspace/repo/.git/info/exclude

# Preinstall the agent runtime to avoid network downloads during trial setup.
RUN uv python install 3.12 \
    && uv tool install --python 3.12 mini-swe-agent==2.4.6 --with litellm --with orjson --with fastapi

RUN git -C /workspace/repo branch -f main "$BASE_COMMIT"
