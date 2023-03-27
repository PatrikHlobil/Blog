---
draft: true
date: 2023-03-13
categories: pytest
            pyspark
            testing
---

# Unit to System Testing of Pyspark Applications with Pytest
**Testing data-centric applications** is always a challenge due to the added complexity of state in the corresponding date interchange systems (files, databases, REST Services, ...). In the following, I will consider as an example simple batch data pipelines with IO and data transformation in `Pyspark` with **Spark Warehouse/Hive**, the main ideas however can be easily transfered and used for testing data-workflows involving other Frameworks or databases.

## Testing pyramide

For `Pyspark`, there is the additional complexity with the main **Spark Java process** running the workload, while the Python-wrapper is driving the execution. However, this will turn out not be be a hard problem. 

A testing pyramide for **Spark Applications** can look like the one below, with:

- unit tests covering internal data transformations (on dataframes)
- integration tests adding IO from local filesystems and databases (Spark Warehouse, JDBC)
- system tests running similar tests on a Release system. Preferably, these tests should also be executed on the production system, because you can never be sure about configuration drifts or other subtile differences between the systems that affect your application.

![Testing pyramide](images/testing-pyramide.svg)

Each stage normaly comes with an increase test complexity and also potential security implications (running automated tests on production systems has to be handler with care). On top of the pyramide one could add additional stages like an **end-2-end test**, where you use real-world data on the Cluster for your tests, however this is often involved with a manuel reviewing process and I am not going to discuss this topic in the following. 



- https://github.com/malexer/pytest-spark
