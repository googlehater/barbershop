-- 1. create enum for master status type
CREATE TYPE master_status AS ENUM ('fired', 'works', 'on_vacation');

-- 2. table services
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    services_name VARCHAR(100) NOT NULL,
    duration_minutes INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT
);

-- 3. table masters
CREATE TABLE masters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    average_score DECIMAL(3,2),  -- средний рейтинг от 1 до 5
    works_since DATE,
    status master_status DEFAULT 'works'
);

-- 4. table clients
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    client_since DATE DEFAULT CURRENT_DATE
);

-- 5. table appointments for services
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    master_id INT NOT NULL,
    service_id INT NOT NULL,
    client_wish TEXT,
    date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'confirmed',   -- добавил статус записи (полезно)
    CONSTRAINT fk_appointments_client FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE RESTRICT,
    CONSTRAINT fk_appointments_master FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE RESTRICT,
    CONSTRAINT fk_appointments_service FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE RESTRICT
);

-- 6. tablw scores of masters
CREATE TABLE scores (
    id SERIAL PRIMARY KEY,
    score_of_master_id INT NOT NULL,
    score_by_client_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    feedback_text TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_scores_master FOREIGN KEY (score_of_master_id) REFERENCES masters(id) ON DELETE CASCADE,
    CONSTRAINT fk_scores_client FOREIGN KEY (score_by_client_id) REFERENCES clients(id) ON DELETE CASCADE,
    CONSTRAINT unique_master_client UNIQUE (score_of_master_id, score_by_client_id)
);