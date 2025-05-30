FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY main.py ./

# Expose the port your app runs on
EXPOSE 8001

# Run the application
CMD ["uv", "run", "python", "main.py"]
