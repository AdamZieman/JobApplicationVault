import sqlite3
# Function to create tables if they don't exist
def create_tables(connection):
    cursor = connection.cursor()

    # Create job_applications table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_applications (
            job_application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            work_style TEXT,
            employment_status TEXT,
            city TEXT,
            state TEXT,
            job_description TEXT
        );
    ''')

    # Create application_statuses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS application_statuses (
            application_status_id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            julian_date REAL NOT NULL,
            job_application_id INTEGER NOT NULL,
            FOREIGN KEY(job_application_id) REFERENCES job_applications(job_application_id) ON DELETE CASCADE
        );
    ''')

    # Create contacts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            position TEXT,
            email TEXT,
            phone TEXT,
            job_application_id INTEGER NOT NULL,
            FOREIGN KEY(job_application_id) REFERENCES job_applications(job_application_id) ON DELETE CASCADE
        );
    ''')

    # Create technical_skills table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS technical_skills (
            technical_skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL UNIQUE,
            occurrences INTEGER NOT NULL DEFAULT 1
        );
    ''')

    # Create job_application_technical_skills table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_application_technical_skills (
            job_application_id INTEGER NOT NULL,
            technical_skill_id INTEGER NOT NULL,
            PRIMARY KEY(job_application_id, technical_skill_id),
            FOREIGN KEY(job_application_id) REFERENCES job_applications(job_application_id) ON DELETE CASCADE,
            FOREIGN KEY(technical_skill_id) REFERENCES technical_skills(technical_skill_id) ON DELETE CASCADE
        );
    ''')

    connection.commit()
