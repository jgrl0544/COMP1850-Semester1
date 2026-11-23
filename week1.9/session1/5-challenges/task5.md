# Task 5: Leeds Eats task sheet

Open the database with `sqlite3 leeds_eats.db`, write your queries in `task.sql`, and run them with `.read task.sql`.

Most of these are requests from real people at Leeds Eats. For each one, work out which table and columns you need, then write the query. Some questions also ask you to explain or justify: write your answer as a comment in task.sql, starting with `--`.

Start wherever suits you, and come back to finish off anything you missed in your independent study time.


## Bronze: warm-up

1. List every column for every driver.
SELECT * FROM drivers;

2. List the name and price of every dish sold by Bangkok Garden (restaurant 3).
SELECT menu_items.name, menu_items.price from menu_items INNER JOIN restaurants ON restaurants.restaurant_id == menu_items.restaurant_id;

3. List the names of all the Indian restaurants.


4. How many customers does Leeds Eats have?


## Silver: requests from customers and staff

5. **A student:** "I'm vegetarian and I've only got £8. What could I order? Cheapest first, please."

SELECT name, price FROM menu_items WHERE price <= 8 AND is_vegetarian == 1 ORDER BY price;

6. **A food safety officer from Leeds City Council:** "Which restaurants have a hygiene rating below 4? Show the worst first."

SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 ORDER BY hygiene_rating;

7. **A student who lives in LS6:** "Which restaurants are near me, best rated first?" Does a matching postcode really mean a restaurant is near? What could go wrong?

8. **The marketing team:** "We want to email everyone who signed up with a University of Leeds email address, newest members first." Write the query, then say whether Leeds Eats should actually send this email.

9. **The operations manager:** "Show me the 10 most recent cancelled orders."

10. **The owner of Pasta Pronto (restaurant 4):** "Which of my dishes are vegetarian? And what's my most expensive dish?" (Two queries.)


## Gold: think it through

11. **The operations manager:** "Some orders from October look stuck: they still say 'placed'. Find them for the support team." Choose only the columns a support agent would need, and justify each one.

SELECT order_id, customer_id, restaurant_id,  delivery_fee FROM orders WHERE status == 'placed' AND order_time < '2026-11-01' AND order_time > '2026-09-30';

order id to know what the order is.
customer id to inform them.
restaurant id to inform them.
delivery_fee in case of any refunds.

12. **A colleague:** "I want the 5 cheapest vegetarian dishes. My first query gives an error and my second gives the wrong answer. Why?"
   
       SELECT name, price FROM menu_items ORDER BY price LIMIT 5 WHERE is_vegetarian = 1; the ordering is wrong. ORDER BY should be right before LIMIT. 
       all conditionals should happen before both. 
       SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5; you need to order by price ascending. 


       Correction: SELECT name, price FROM menu_items WHERE is_vegetarian = 1 ORDER BY price ASC LIMIT 5;

   
   Explain what's wrong with each, then write a correct version.

13. **A customer:** "What's the cheapest thing I can get on Leeds Eats?" Write the query. Then run it again with LIMIT 5 instead of LIMIT 1. What do you notice, and how should Leeds Eats answer this customer fairly?

SELECT name, price FROM menu_items ORDER BY price LIMIT 5;
We realize that they all have the same price, so there is no cheapest thing. 
In my opinion, run another query where price == 3.5 and give the customer all these options and let them decide for themselves.
╞════════════════════╪═══════╡
│ Egg fried rice     │   3.5 │
│ Hot and sour soup  │   3.5 │
│ Baba ganoush       │   3.5 │
│ Edamame            │   3.5 │
│ Callaloo           │   3.5 │
│ Tzatziki and pitta │   3.5 │
│ Onion rings        │   3.5 │
│ Garlic bread       │   3.5 │
│ Rice and peas      │   3.5 │
│ Festival dumplings │   3.5 │
│ Tzatziki and pitta │   3.5 │
╰────────────────────┴────────
14. **The product team:** "We're thinking of launching a 'late-night favourites' menu. How many orders are placed at 21:00 or later, out of all orders?" Is that enough evidence to launch the feature? What else would you want to know?

check if its less than, say, 3am and greater than 9pm. how do we filter out? wed want to know if theres specific restaurants that have a disproportionately high number of late-night orders. we want to know the cardinality of late night orders compared to the cardinality of ALL orders. also, if the same item is being ordered at night, it would be a lame late night menu of just one item.

SELECT COUNT(*) FROM orders WHERE time(order_time) > '21:00:00'; 173.
this seems to be the best method. cast it to a time and compare it to the needed time. 

SELECT COUNT(*) FROM orders; 1300.
173/1300 is just over 13% of all orders being late night ones. 
maybe use joins and whatever to see which restaurants specifically have the most orders late at night?

15. **You:** Think of a question a Leeds Eats customer, restaurant owner or manager might ask. Write it as a request in their words, then write the query. Swap with a neighbour: answer theirs, and check each other's.

