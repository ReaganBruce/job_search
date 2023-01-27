
create_table = """
    CREATE TABLE IF NOT EXISTS applied_jobs (
        Company CHARACTER(20) NOT NULL,
        Position VARCHAR(50) NOT NULL,
        Location VARCHAR(40) NOT NULL,
        Software Stack VARCHAR(60) NOT NULL,
        Date_Submitted TIMESTAMP
    );
"""

insert_into_applied_jobs = """
INSERT INTO applied_jobs
VALUES (?, ?, ?, ?, ?);
"""

select_applied_to_jobs = """
SELECT * FROM applied_jobs
"""