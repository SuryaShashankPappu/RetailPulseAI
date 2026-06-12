# RetailPulse AI - Source to Target Mapping

## Sales Transactions (CSV → Warehouse)

| Source Column | Target Column    | Target Table      | Transformation Rule                |
| ------------- | ---------------- | ----------------- | ---------------------------------- |
| Invoice       | invoice_id       | fact_transactions | Trim whitespace                    |
| StockCode     | product_id       | fact_transactions | Convert to string                  |
| Description   | product_name     | dim_product       | Remove nulls where possible        |
| Quantity      | quantity         | fact_transactions | Preserve negative values (returns) |
| InvoiceDate   | transaction_date | fact_transactions | Convert to datetime                |
| Price         | unit_price       | fact_transactions | Validate numeric values            |
| Customer ID   | customer_id      | dim_customer      | Convert to string                  |
| Country       | country          | dim_customer      | Standardize country names          |

---

## Inventory System (PostgreSQL → Warehouse)

| Source Column | Target Column | Target Table   | Transformation Rule |
| ------------- | ------------- | -------------- | ------------------- |
| product_id    | product_id    | fact_inventory | No change           |
| stock_level   | stock_level   | fact_inventory | Validate >= 0       |
| reorder_point | reorder_point | fact_inventory | Validate >= 0       |
| warehouse_id  | warehouse_id  | fact_inventory | No change           |
| last_updated  | snapshot_date | fact_inventory | Convert to datetime |

---

## Supplier API (REST API → Warehouse)

| Source Field   | Target Column   | Target Table | Transformation Rule |
| -------------- | --------------- | ------------ | ------------------- |
| supplier_id    | supplier_id     | dim_supplier | No change           |
| supplier_name  | supplier_name   | dim_supplier | Trim whitespace     |
| lead_time_days | lead_time_days  | dim_supplier | Validate numeric    |
| country        | country         | dim_supplier | Standardize         |
| rating         | supplier_rating | dim_supplier | Validate range 1-5  |

---

## Customer Reviews (JSON → Warehouse)

| Source Field | Target Column | Target Table | Transformation Rule |
| ------------ | ------------- | ------------ | ------------------- |
| review_id    | review_id     | fact_reviews | No change           |
| product_id   | product_id    | fact_reviews | No change           |
| rating       | rating        | fact_reviews | Validate range 1-5  |
| review_text  | review_text   | fact_reviews | Clean text          |
| review_date  | review_date   | fact_reviews | Convert to datetime |

---

## Weather API (API → Warehouse)

| Source Field | Target Column | Target Table | Transformation Rule |
| ------------ | ------------- | ------------ | ------------------- |
| temperature  | temperature   | dim_weather  | Numeric validation  |
| rainfall     | rainfall      | dim_weather  | Numeric validation  |
| humidity     | humidity      | dim_weather  | Numeric validation  |
| date         | weather_date  | dim_weather  | Convert to date     |

---

## Holiday API (API → Warehouse)

| Source Field | Target Column | Target Table | Transformation Rule |
| ------------ | ------------- | ------------ | ------------------- |
| holiday_name | holiday_name  | dim_holiday  | No change           |
| holiday_date | holiday_date  | dim_holiday  | Convert to date     |
| country      | country       | dim_holiday  | Standardize         |
