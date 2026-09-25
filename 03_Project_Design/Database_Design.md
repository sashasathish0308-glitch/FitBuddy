# Database Design

## Database

SQLite

## Main Tables

### Users

- user_id
- name
- age
- weight
- goal
- intensity
- created_at

### Plans

- id
- user_id
- original_plan
- updated_plan
- nutrition_tip
- updated_nutrition_tip
- created_at
- updated_at

## Relationship

One user can have one or more generated plan records.