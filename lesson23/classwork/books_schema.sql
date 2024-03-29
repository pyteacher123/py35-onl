CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE);
CREATE TABLE new_authors (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, surname TEXT NOT NULL, country_id INTEGER, FOREIGN KEY (country_id) REFERENCES countries(id));
CREATE TABLE genres (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE);
CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT NOT NULL, genre_id INTEGER, author_id INTEGER, FOREIGN KEY (genre_id) REFERENCES genres(id), FOREIGN KEY (author_id) REFERENCES "new_authors"(id));
CREATE TABLE profiles (id INTEGER PRIMARY KEY AUTOINCREMENT, phone TEXT, birth_date NUMERIC);
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, profile_id INTEGER UNIQUE, FOREIGN KEY (profile_id) REFERENCES profiles(id));
CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT);
CREATE TABLE courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, hours INTEGER);
CREATE TABLE students_courses (student_id INTEGER, course_id INTEGER, PRIMARY KEY (student_id, course_id), FOREIGN KEY (student_id) REFERENCES students(id), FOREIGN KEY (course_id) REFERENCES courses(id));
