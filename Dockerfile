FROM continuumio/miniconda3:latest
ENV PATH /opt/conda/bin:$PATH
ENV PYTHONPATH=/nuscenes-dev/python-sdk

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsm6 \
        libxext6 \
        libxrender-dev \
        libgl1-mesa-glx \
        libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /nuscenes-dev
COPY requirements.txt /nuscenes-dev
# Install Python dependencies inside of the Docker image via Conda.
RUN bash -c "conda create -y -n nuenv python=3.7; source activate nuenv && \
    pip install -r /nuscenes-dev/requirements.txt \
    && conda clean --yes --all"

COPY . /nuscenes-dev
