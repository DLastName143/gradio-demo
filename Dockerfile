FROM python:3.10-slim

# Set working directory
WORKDIR /app

ENV MPLCONFIGDIR=/tmp/matplotlib
ENV GRADIO_FLAGGING_DIR=/tmp/flagged
# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set environment variable for Gradio temp directory
ENV GRADIO_TEMP_DIR=/tmp

# Ensure OpenShift-compatible non-root user
RUN adduser --disabled-password --gecos '' --uid 1001 appuser
USER 1001

# Expose Gradio port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]