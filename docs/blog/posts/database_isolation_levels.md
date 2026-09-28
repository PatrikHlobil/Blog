---
date: 2026-09-23
categories: 
  - databases
  - concurrency
draft: true
---


# Isolation Levels in Databases

**Databases** are one of the key pillars in application development and serve as a consistent & scalable persistent storage. However, when using a database with shared access pattern, where multiple users can concurrently write data, inconcistencies can occur when using the wrong **Isolation Levels**.

Here, we will discuss the different isolation levels from `Read-Committed` to `Serializable` and show with code examples problems like *write skews* and *phantom reads* that can occur.

<!-- more -->


## Setup

For easy setup, you can use the prepared script:

??? "Postgres Setup Script"

    ```python title="database_setup.py"
    --8 < --"docs/code/database_isolation_levels/database_setup.py"
    ```

This script starts a postgres Docker container, which is automatically stopped when the user aborts the process. It also creates a table `inventory` with the columns:

| Column | Type | Description |
| --- | --- | --- |
| `id` | `uuid` | Uniquely identifies an inventory item. PostgreSQL generates a random UUID by default, and the column is the table's primary key. |
| `product` | `text` | Stores the name of the product. A value is required for every inventory item. |
| `buyer` | `text` | Stores the name of the peson who bought the item. A `NULL` value means the item is still available. |
| `delivery_address` | `text` | Stores the address where the delivery will be send to. |

Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your machine, then you can start the Database process via:

    uv run database_setup.py

## Isolation Levels

### Read Committed

The weakest isolation level is called **Read-Committed** and is the default in Postgres and most other SQL Databases.

In **Read-Committed**, a transaction will only see changes that have been successfully committed by other transactions. Thus, any changes that are **not yet committed** are hidden for other transactions. This level of seperations ensures that we do not have:

- Dirty Reads: Transactions only see changes of other transactions that where successfully committed
- Dirty Writes: A second transaction cannot change data of a row, which has already been changes in another uncommitted transaction. In this case, the database makes sure that the first transaction first successfully commits (or rolls back), and then the changes of the second transaction will be applied. This is typically be implemented by using row-level locks.


#### Demo: No Dirty Reads

Consider an example where two users concurrently access the same item in the `inventory` table.


=== "Diagram"

    ```mermaid
    --8<-- "docs/code/database_isolation_levels/read-committed-dirty-reads.mmd"
    ```

=== "Code"

    ```python title="read-committed.py"
    --8 < --"docs/code/database_isolation_levels/read-committed-dirty-reads.py"
    ```

Here, we have the following interactions with the database:

① User 1 adds a **Laptop** to the inventory without a buyer and commits the change.

② User 2 reads the item's buyer. The query returns `NULL`, which means the laptop is still available.

③ User 1 starts a transaction and sets the item's buyer to **Alice**.

④ Concurrently, User 2 reads the buyer again. The query still returns `NULL` because User 1's update has not been committed. This prevents a dirty read.

⑤ User 1 commits the transaction, making the purchase visible to other transactions.

⑥ User 2 reads the buyer again and now gets **Alice**.


You can test this out in action using the provided Python script. Just make sure that you have the database running as described in the [Setup](#setup) section and then run the script via:

    > uv run read_committed.py

    ②: Buyer is None
    ④: Buyer is None (no dirty read)
    ⑥: Buyer is Alice (read committed)

#### Demo 2: No Dirty Writes

=== "Diagram"

    ```mermaid
    --8<-- "docs/code/database_isolation_levels/read-committed-dirty-writes.mmd"
    ```

=== "Code"

    ```python title="read-committed.py"
    --8 < --"docs/code/database_isolation_levels/read-committed-dirty-writes.py"
    ```

Executing the provided Python script gives us:

    > uv run docs/code/database_isolation_levels/read-committed-dirty-writes.py
    0.05 Seconds | User 1: UPDATE inventory SET buyer='Alice' WHERE product='Laptop'
    2.08 Seconds | User 1: UPDATE inventory SET delivery_address='Los Angeles' WHERE product='Laptop'
    2.08 Seconds | User 2: UPDATE inventory SET buyer='Robin' WHERE product='Laptop'
    2.09 Seconds | User 2: UPDATE inventory SET delivery_address='New York' WHERE product='Laptop'
    Final buyer is Robin, delivery address is New York


## Conclusion

...

If you are interested in more details, I can highly recommend the book [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) by **Martin Kleppmann, Chris Riccomini**.
