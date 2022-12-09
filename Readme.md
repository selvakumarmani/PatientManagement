1.Create the virtual environment for python3.8 using below command.

    virtualenv patient_env

2.To activate the virtual environment

    source patient_env/bin/activate

3. After activating the virtual environment To install dependencies use below command

    pip install -r requirement.txt

4. After activating the virtual environment run the django project, daphne and celery

    1.Execute django project using daphne

        daphne PatientManagement.asgi:application -p 8002

    2.Enable the celery worker

        python -m celery -A PatientManagement worker

    3.For run the django project

        python manage.py migrate

        python manage.py runserver

