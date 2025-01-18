```mermaid

erDiagram

CUSTOMERS ||--o{ Orders : bought

Users{
    uuid user_id
    }

Customers{
    uuid customer_id
    }

Orders{
    uuid customer_id
    }

Logs{}


```