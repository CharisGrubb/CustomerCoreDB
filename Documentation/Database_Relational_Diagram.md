```mermaid

erDiagram

CUSTOMERS ||--o{ Orders : bought

Users{user_id}

Customers{customer_id}

Orders{customer_id}

Logs{}


```