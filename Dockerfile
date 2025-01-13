FROM python:3.10
RUN pip install streamlit numpy
WORKDIR /app
# COPY src/* /app/
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py" ]