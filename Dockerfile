FROM python:alpine
RUN pip install uv
WORKDIR /app
COPY logging.yml \
	pyproject.toml \
	testserver.py \
	./
RUN uv pip install --system .
EXPOSE 8888
CMD ["python", "testserver.py"]
