# Student Attendance Application - Agile Lab

A very small Python app used to demo five topics: **JIRA, Git/GitHub, Pytest, Docker, Selenium, GitHub Actions (CI/CD)**.

Login for the demo: `admin` / `admin123`

## Files

| File | What it does |
|------|--------------|
| `attendance.py` | `attendance(present, total)` gives the percentage. `attendance_report(percent)` gives Good / Average / Poor (this is the change made on the feature branch). |
| `app.py` | Tiny Flask web app: login page, then a dashboard showing attendance. |
| `templates/` | `login.html` and `dashboard.html`. Elements have ids (`username`, `password`, `login-btn`, `welcome`, `error`) used as Selenium locators. |
| `test_attendance.py` | 4 Pytest test cases for `attendance()`. |
| `test_login.py` | 2 Selenium tests (valid login, invalid login) with explicit waits. |
| `Dockerfile` | Builds the app image. |
| `.github/workflows/ci.yml` | GitHub Actions pipeline. |
| `requirements.txt` | flask, pytest, selenium. |

---

## 1. Git setup (run in the project folder)

The local repo already has the branch `feature/attendance-report` with the report function committed. Just connect it to GitHub:

```bash
git remote add origin https://github.com/thatindiangeek81/Student-Attendance-application.git
git branch
```

Local main branch is called `master`. Push it first, then the feature branch:

```bash
git push -u origin master
git add .
git commit -m "add flask app, tests, dockerfile and CI pipeline"
git push -u origin feature/attendance-report
```

If the push of `master` is rejected because the GitHub repo already has files, run `git pull origin master --allow-unrelated-histories` and push again.

Then on GitHub: **Compare & pull request** -> create PR (`feature/attendance-report` into `master`) -> merge.
Creating the branch from scratch would be: `git checkout -b feature/attendance-report`.

## 2. Pytest (attendance percentage)

```bash
pip install -r requirements.txt
pytest test_attendance.py -v
```

4 cases: 50% (5/10), 0% (0/10), 100% (10/10), and total = 0 (must return 0 and not crash).

## 3. Docker

```bash
docker build -t attendance-app .
docker run -d -p 5000:5000 --name attendance attendance-app
```

`-p 5000:5000` means **host port 5000 -> container port 5000**. Open http://localhost:5000

Useful: `docker ps` (see it running), `docker logs attendance`, `docker stop attendance`, `docker rm attendance`.
To use another host port, e.g. `-p 8080:5000`, then open http://localhost:8080 (the Selenium test uses 5000).

## 4. Selenium (login page)

Needs Google Chrome installed (Selenium 4 downloads the driver itself). Start the app first (via Docker above, or `python app.py`), then in another terminal:

```bash
pytest test_login.py -v
```

- Locators: `By.ID` for username, password, login button, welcome text and error text.
- Explicit wait: `WebDriverWait` with `expected_conditions` (waits up to 10 s for the element instead of fixed `sleep`).
- Test 1: valid login -> "Welcome" appears. Test 2: wrong login -> "Invalid credentials" appears.

## 5. CI/CD - GitHub Actions

File: `.github/workflows/ci.yml`. Runs on every push and pull request:
1. checkout code
2. set up Python 3.11
3. `pip install -r requirements.txt`
4. `pytest test_attendance.py`

After pushing, open the **Actions** tab of the repo to see the green tick. (Selenium test is not in the pipeline because it needs a running app and browser.)

## 6. JIRA (for the demo, done in the browser)

1. Create a free Jira site -> create a **Scrum** project, e.g. "Student Attendance".
2. Create an **Epic**: *Attendance Management*.
3. Create stories under it, for example:
   - SA-1: As a student, I can log in to the system
   - SA-2: As a teacher, I can see attendance percentage
   - SA-3: As a teacher, I can see an attendance report (Good/Average/Poor)  <- feature branch
   - SA-4: Write tests, Dockerize and add CI pipeline
4. Create a **Sprint**, drag the stories into it, click **Start sprint**.
5. Move cards To Do -> In Progress -> Done as you work.
6. Tip: name commits/branches with the issue key (e.g. `SA-3`) to show Jira + Git linking.

## 7. How to explain it to faculty (quick flow)

1. **JIRA** - planned work as epic/stories in a sprint (Agile).
2. **Git/GitHub** - made a feature branch, changed the code a little, raised PR, merged.
3. **Pytest** - automated unit tests for the percentage function.
4. **GitHub Actions** - on each push, tests run automatically (CI).
5. **Docker** - app packaged in a container, run with port mapping.
6. **Selenium** - automated UI test of the login page.

Likely questions:
- *Why Docker?* Same environment everywhere, no "works on my machine".
- *What is CI?* Automatically building/testing code on every change.
- *Why explicit wait?* Waits only as long as needed for an element, more reliable than `time.sleep`.
- *Why test `total = 0`?* Edge case; avoids division by zero.
