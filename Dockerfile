# Base Image
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        git \
        python3-pip \
        python3-dev \
        libglib2.0-0 \
        iputils-ping \
        cron \
        curl \
        nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /model_automation

# Copy requirements and install Python dependencies
COPY ./requirements.txt /model_automation/requirements.txt
RUN pip install --no-cache-dir -r /model_automation/requirements.txt

# Copy application code
COPY ./app /model_automation/app

# Expose port
EXPOSE 5000

# Start the cron service and the application
CMD uvicorn app.main:app --host 0.0.0.0 --port 5000