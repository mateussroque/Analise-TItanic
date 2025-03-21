FROM python:3.10-slim


WORKDIR /app

# Copy the application code
COPY app/ /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

# Start the application with Streamlit
CMD ["streamlit", "run", "graficos.py"]
