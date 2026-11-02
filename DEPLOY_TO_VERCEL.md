# 🚀 Deploying to Vercel Guide

This application is fully pre-configured for one-click or command-line deployment to **Vercel** as a serverless Python Flask application.

---

## 📁 Key Files Configured for Vercel

1. **`api/index.py`**: The serverless entry point that exposes the Flask `app` callable to Vercel's Python runtime.
2. **`vercel.json`**: Configures URL rewrites to route all traffic to `/api/index.py` and bundles `templates/`, `static/`, `data/`, and database assets into the Lambda bundle.
3. **`.vercelignore`**: Excludes local cache, bytecode, uploads, and `.env` files from being deployed.
4. **`requirements.txt`**: Optimized list of runtime dependencies for fast serverless builds.
5. **`config.py` & `database.py`**: Automatically detect serverless environments, write dynamic uploads/charts to `/tmp`, and support cloud databases (`DATABASE_URL`, `MYSQL_URL`) as well as SQLite fallback in `/tmp/sales_data.db`.

---

## Method 1: Deploy via GitHub (Recommended)

1. **Initialize Git & Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Configure Flask app for Vercel deployment"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

2. **Import to Vercel**:
   - Log in to your [Vercel Dashboard](https://vercel.com).
   - Click **Add New...** -> **Project**.
   - Select your GitHub repository and click **Import**.
   - Under **Framework Preset**, leave it as **Other**.
   - Under **Root Directory**, keep `./`.

3. **(Optional) Configure Environment Variables**:
   In the **Environment Variables** section on Vercel:
   - `SECRET_KEY`: Set a secure random string (e.g. `your-production-secret-key-2026`).
   - If using a cloud MySQL database (e.g. PlanetScale, Railway, Aiven, TiDB Cloud, Supabase):
     - `DATABASE_URL`: `mysql://user:password@host:port/dbname`
     - `DB_SSL`: `true` (if required by your cloud provider)
     - `DB_TYPE`: `mysql`
   - *If no environment variables are set*, the app automatically runs in **SQLite demo mode** using the pre-seeded SQLite database copied to `/tmp/sales_data.db`.

4. **Click Deploy**:
   - Vercel will install dependencies from `requirements.txt` and launch your project.
   - Your live URL will be generated (e.g., `https://your-project.vercel.app`).

---

## Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from project folder**:
   ```bash
   cd newwwwwwwwwww
   vercel
   ```
   Follow the interactive prompts (accept defaults).

4. **Deploy to Production**:
   ```bash
   vercel --prod
   ```

---

## 🗄️ Database Options on Vercel

- **Zero-Config SQLite (Default / Demo)**:
  - If no database credentials are provided, the app automatically copies the bundled `sales_data.db` to `/tmp/sales_data.db`.
  - Perfect for immediate demos, presentations, or testing.
  - *Note: In serverless environments, `/tmp` is ephemeral and resets during cold starts.*

- **Production Cloud MySQL (Recommended for Persistent Data)**:
  - Free cloud MySQL instances are available on:
    - [Railway](https://railway.app)
    - [Aiven for MySQL](https://aiven.io)
    - [TiDB Cloud Serverless](https://tidbcloud.com)
    - [Clever Cloud](https://clever-cloud.com)
  - Copy the MySQL connection URI and paste it as `DATABASE_URL` in your Vercel Project Settings -> **Environment Variables**.
  - All users, sales records, and uploaded CSV datasets will persist permanently across serverless function instances!
