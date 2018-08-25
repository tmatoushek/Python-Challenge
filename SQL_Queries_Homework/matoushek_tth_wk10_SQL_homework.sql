
USE sakila;


-- 1a. Display the first and last names of all actors from the table `actor`.
SELECT first_name, last_name 
FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. 
-- Name the column `Actor Name`.
SELECT CONCAT(first_name, '   ', last_name) AS Actor_Name
FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you 
-- know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';

-- 2b. Find all actors whose last name contain the letters `GEN`:
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE '%gen%';

-- 2c. Find all actors whose last names contain the letters `LI`. 
-- This time, order the rows by last name and first name, in that order:
SELECT last_name, first_name
FROM actor
WHERE last_name LIKE '%li%';

-- 2d. Using `IN`, display the `country_id` and `country` columns 
-- of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a. You want to keep a description of each actor. You don't think you 
-- will be performing queries on a description, so create a column in the table 
-- `actor` named `description` and use the data type `BLOB` (Make sure to research 
-- the type `BLOB`, as the difference between it and `VARCHAR` are significant).
ALTER TABLE actor ADD actor_description BLOB;

-- 3b. Very quickly you realize that entering descriptions for 
-- each actor is too much effort. Delete the `description` column.
ALTER TABLE actor DROP COLUMN actor_description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;

-- 4b. List last names of actors and the number of actors who have that 
-- last name, but only for names that are shared by at least two actors
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) >= 2;

-- 4c. The actor `HARPO WILLIAMS` was accidentally entered in the 
-- `actor` table as `GROUCHO WILLIAMS`. Write a query to fix the record.
UPDATE actor
SET first_name = 'harpo'
WHERE last_name = 'williams' AND first_name = 'groucho';

-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns 
-- out that `GROUCHO` was the correct name after all! In a single query, if 
-- the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
UPDATE actor
SET first_name = 'groucho'
WHERE last_name = 'williams' AND first_name = 'harpo';

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to 
-- re-create it? * Hint: <https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html>
SHOW CREATE TABLE address;

--  
-- ```
-- CREATE TABLE `address` (
--    `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
--    `address` varchar(50) NOT NULL,
--    `address2` varchar(50) DEFAULT NULL,
--    `district` varchar(20) NOT NULL,
-- 	`city_id` smallint(5) unsigned NOT NULL,
-- `postal_code` varchar(10) DEFAULT NULL,
--    `phone` varchar(20) NOT NULL,
--    `location` geometry NOT NULL,
--    `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--    PRIMARY KEY (`address_id`),
--    KEY `idx_fk_city_id` (`city_id`),
--    SPATIAL KEY `idx_location` (`location`),
--    CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
--  ) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8
-- ```

-- 6a. Use `JOIN` to display the first and last names, as well as the 
--  address, of each staff member. Use the tables `staff` and `address`:
SELECT first_name, last_name, address
FROM  staff st
INNER JOIN address ad 
ON st.address_id = ad.address_id;

-- 6b. Use `JOIN` to display the total amount rung up by each staff 
-- member in August of 2005. Use tables `staff` and `payment`.
SELECT st.first_name, st.last_name, SUM(amount)
FROM staff st
INNER JOIN payment py
ON st.staff_id = py.staff_id
WHERE DATE(payment_date) BETWEEN '2005-08-01' AND '2005-08-31'
GROUP BY st.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. 
-- Use tables `film_actor` and `film`. Use inner join.
SELECT title, COUNT(actor_id)
FROM film f
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
GROUP BY title;

-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT title, COUNT(inventory_id)
FROM film f
INNER JOIN inventory inv 
ON f.film_id = inv.film_id
WHERE title = 'Hunchback Impossible';

-- 6e. Using the tables `payment` and `customer` and the `JOIN` command, list 
-- the total paid by each customer. List the customers alphabetically by last name:
-- SELECT cs.last_name, cs.first_name, py.amount
SELECT cs.last_name, cs.first_name, py.amount 
FROM customer cs
INNER JOIN payment py
ON cs.customer_id = py.customer_id
GROUP BY py.customer_id
ORDER BY last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely 
-- resurgence. As an unintended consequence, films starting with the 
-- letters `K` and `Q` have also soared in popularity. Use subqueries to 
-- display the titles of movies starting with the letters `K` and `Q` 
-- whose language is English.
SELECT title
    FROM film
    WHERE language_id
    IN (
      SELECT language_id
        FROM language
        WHERE name = 'English'
              )
            AND title LIKE 'K%'
            OR title LIKE 'Q%';


-- 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
(
  SELECT actor_id
  FROM film_actor
  WHERE film_id IN
  (
   SELECT film_id
   FROM film
   WHERE title = 'ALONE TRIP'
  )
);

-- 7c. You want to run an email marketing campaign in Canada, for which you 
-- will need the names and email addresses of all Canadian customers. Use 
-- joins to retrieve this information.
SELECT first_name, last_name, email
	FROM customer
	WHERE address_id 
    IN (
      SELECT address_id
        FROM address
        WHERE city_id
        IN (
          SELECT city_id
            FROM city
            WHERE country_id
			IN (
              SELECT country_id
			  FROM country
              WHERE country = 'Canada'
	)
		)
			);

-- 7d. Sales have been lagging among young families, and you wish to target all 
-- family movies for a promotion. Identify all movies categorized as family films.
SELECT category, title
FROM film_list
WHERE category = 'Family';

-- 7e. Display the most frequently rented movies in descending order.
SELECT f.title AS 'Film Title', COUNT(rnt.rental_date) AS 'Times Rented'
FROM film f
JOIN inventory inv 
ON inv.film_id = f.film_id
JOIN rental rnt 
ON rnt.inventory_id = inv.inventory_id
GROUP BY f.title
ORDER BY COUNT(rnt.rental_date) DESC;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT st.store_id, ci.city, co.country
FROM store st
INNER JOIN customer cu
ON st.store_id = cu.store_id
INNER JOIN address ad
ON cu.address_id = ad.address_id
INNER JOIN city ci
ON ad.city_id = ci.city_id
INNER JOIN country co
ON ci.country_id = co.country_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (**Hint**: you may need to use the following tables: category, 
-- film_category, inventory, payment, and rental.)
SELECT category_id, category.name , sum(amount) as rev
From payment
Join rental
using(rental_id)
JOIN inventory
using(inventory_id)
JOIN film_category
USING(film_id)
JOIN category
USING (category_id)
GROUP BY category_id
ORDER BY rev DESC
LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of 
-- viewing the Top five genres by gross revenue. Use the solution from the 
-- problem above to create a view. If you haven't solved 7h, you can substitute 
-- another query to create a view.
CREATE VIEW genre_top5_sales AS
SELECT name, SUM(py.amount) AS 'Total Sales'
FROM category ct
JOIN film_category fc
ON ct.category_id = fc.category_id
JOIN inventory inv
ON fc.film_id = inv.film_id
JOIN rental rnt
ON inv.inventory_id = rnt.inventory_id
JOIN payment py 
ON rnt.rental_id = py.rental_id
-- GROUP BY name
-- GROUP BY name;
GROUP BY name LIMIT 5;

-- 8b. How would you display the view that you created in 8a?
SELECT * FROM genre_top5_sales;

-- 8c. You find that you no longer need the view `top_five_genres`. 
-- Write a query to delete it.
DROP VIEW genre_top5_sales;


