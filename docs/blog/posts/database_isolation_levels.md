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
    --8<-- "docs/code/database_isolation_levels/database_setup.py"
    ```

This script starts a postgres Docker container, which is automatically stopped when the user aborts the process. It also creates a table `inventory` with the columns:

| Column | Type | Description |
| --- | --- | --- |
| `id` | `uuid` | Uniquely identifies an inventory item. PostgreSQL generates a random UUID by default, and the column is the table's primary key. |
| `product` | `text` | Stores the name of the product. A value is required for every inventory item. |
| `buyer` | `text` | Stores the name of the person who bought the item. A `NULL` value means the item is still available. |

Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your machine, then you can start the Database process via:

    uv run database_setup.py

## Isolation Levels

### Read Committed

The weakest isolation level is called **Read-Committed** and is the default in Postgres and most other SQL Databases.

In **Read-Committed**, a transaction will only see changes that have been successfully committed by other transactions. Thus, any changes that are **not yet committed** are hidden for other transactions.

```mermaid
    --8<-- "docs/code/database_isolation_levels/read-committed.mmd"
```


## Conclusion

...

If you are interested in more details, I can highly recommend the book [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) by **Martin Kleppmann, Chris Riccomini**.