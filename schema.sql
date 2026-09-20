CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    role VARCHAR(50) -- User, Technician, Refurbisher, Recycler, Admin
);

CREATE TABLE devices (
    device_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    model VARCHAR(100),
    status VARCHAR(50),
    recommended_pathway VARCHAR(50)
);

CREATE TABLE lifecycle_records (
    record_id SERIAL PRIMARY KEY,
    device_id INT REFERENCES devices(device_id),
    event_type VARCHAR(100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);