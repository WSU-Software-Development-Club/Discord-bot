# ---------- Stage 1: build the virtual environment ----------
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Create an isolated Python virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ---------- Stage 2: slim runtime image ----------
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Run as a non-root user
RUN useradd --create-home --shell /usr/sbin/nologin botuser

# Copy only the finished venv from the builder stage
COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
COPY --chown=botuser:botuser . .

USER botuser

CMD ["python", "bot.py"]
