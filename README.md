# yuna-e2e

A test repository for [Yuna](https://github.com/corya0687/yuna) security checks.

**Every problem in this repository is planted on purpose.** Do not copy this
code, and do not deploy it. Nothing here runs in production.

| Check | Planted problem |
|---|---|
| Secrets | `.env` holds a value that looks like an API key (random; never a real credential) |
| Code scan (SAST) | SQL injection and command injection in `app.py`, `server.js`, `main.go`, `app/controllers/users_controller.rb`, and `src/main/java/app/Vuln.java` |
| Dependencies (SCA) | old `lodash` in `package-lock.json`, old `PyYAML` and others in `requirements.txt` |
| Container image | `Dockerfile` uses an old base image and runs as root |
| Infrastructure config (IaC) | `main.tf` opens SSH to the internet and makes a bucket public |
| CI/CD pipeline | `.github/workflows/planted-ci.yml` (it can only be started by hand) |
| Threat model | routes without authentication in `server.js` and `app.py` |

Yuna must report each of these and block. A release of Yuna is tested here
before founders use it.
