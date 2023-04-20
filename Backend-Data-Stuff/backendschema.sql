CREATE TABLE phyrexian_word (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  phyrexian VARCHAR(255),
  phonetic VARCHAR(255),
  translation VARCHAR(255)
);
CREATE TABLE composite_bridge (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  child_id INT NOT NULL,
  parent_id INT NOT NULL,
  FOREIGN KEY (child_id) REFERENCES phyrexian_word(id),
  FOREIGN KEY (parent_id) REFERENCES phyrexian_word(id)
);
CREATE TABLE phyrexian_word_notes (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  phyrexian_word_id INT NOT NULL,
  notes VARCHAR(255),
  FOREIGN KEY (phyrexian_word_id) REFERENCES phyrexian_word(id)
);
CREATE TABLE card (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  card_name VARCHAR(255) NOT NULL
);
CREATE TABLE example_text (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  card_id INT NOT NULL,
  text_field VARCHAR(255),
  phyrexian_text VARCHAR(255),
  english_text VARCHAR(255),
  FOREIGN KEY (card_id) REFERENCES card(id)
);
CREATE TABLE example_bridge (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  phyrexian_word_id INT NOT NULL,
  example_text_id INT NOT NULL,
  FOREIGN KEY (phyrexian_word_id) REFERENCES phyrexian_word(id),
  FOREIGN KEY (example_text_id) REFERENCES example_text(id)
);