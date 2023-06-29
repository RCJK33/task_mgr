CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0,
    archived BOOLEAN DEFAULT 0
);

-- Dummy data (for testing)

INSERT INTO task (summary, description) VALUES 
(
    "Test task 1",
    "This is a test task"
),
(
    "Test task 1",
    "This is a test task"
);