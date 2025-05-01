FROM python:3.9-slim
WORKDIR /app
COPY pyproject.toml setup.cfg ./
RUN pip install .
COPY sdk/ sdk/
CMD ["pytest"]
