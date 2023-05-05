## Assignment Tracker CRUD App

This web application is designed to help students keep track of their assignment deadlines. It allows them to input their assignments, including their due dates and any other relevant details. The app is intended to help students stay organized and on top of their workload, ensuring that they don't miss any important deadlines. Overall, this app serves as a useful tool for students to manage their assignments and stay on track with their academic responsibilities.

To run this app, follow the steps below:
```
flask --app base.py db init
flask --app base.py db migrate -m "Done"
flask --app base.py db upgrade
python cat.py
flask --app base.py run
```

Deployed App: https://assignment-tracker-pccx.onrender.com
