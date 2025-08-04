# NXTech REST API


## Database 
### nxtech

## Table Setup (NXTech)

- users
- user_roles
- titles
- nationalities
- departments
- professions
- professional_groups
- agents
- biz_introducers
- clients


## Execution
docker-compose up --build


# Execute into docker container
docker exec -ti nxtech-be sh
# Create a migration for a table
masonite-orm migration insurance_companies_table

# Create a model (mostly mapped to a table in DB)
masonite-orm model InsuranceCompany --directory=models

# Create a seeder file
masonite-orm seed insurance_companies

# Run migration
masonite-orm migrate -m 2025_06_07_090752_roles_table.py

# DB Migration & Seeding
masonite-orm migration user_roles_table<br>
masonite-orm migrate -m 2025_06_07_090752_roles_table.py
# masonite-orm migrate:rollback -m 2025_06_07_090752_roles_table

masonite-orm seed user_roles<br>
masonite-orm seed:run user_roles

masonite-orm model UserRole --directory=models


