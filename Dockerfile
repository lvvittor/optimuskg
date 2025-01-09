FROM quay.io/astronomer/ap-airflow:2.4.3-onbuild

RUN pip install --user ./dist/optimuskg-0.1-py3-none-any.whl
