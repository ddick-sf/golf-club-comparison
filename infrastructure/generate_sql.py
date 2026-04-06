import csv
import json

tables = {
    'Drivers': 'Data/Golf Comparison - Drivers.csv',
    'Fairways': 'Data/Golf Comparison - Fairway.csv',
    'Irons': 'Data/Golf Comparison - Irons.csv',
    'Wedges': 'Data/Golf Comparison - Wedges.csv'
}

sql_statements = []

for table_name, file_path in tables.items():
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        if not reader:
            continue
        
        headers = list(reader[0].keys())
        
        # Create Table statement
        create_stmt = f'CREATE TABLE IF NOT EXISTS "{table_name}" (\n'
        create_stmt += '    id SERIAL PRIMARY KEY,\n'
        
        for header in headers:
            safe_header = header.replace('"', '""')
            create_stmt += f'    "{safe_header}" TEXT,\n'
            
        create_stmt = create_stmt.rstrip(',\n') + '\n);\n'
        sql_statements.append(create_stmt)
        
        # Disable RLS for easy reading, or enable setting a basic 'anon' select policy
        sql_statements.append(f'ALTER TABLE "{table_name}" ENABLE ROW LEVEL SECURITY;')
        sql_statements.append(f'DROP POLICY IF EXISTS "Public Select" ON "{table_name}";')
        sql_statements.append(f'CREATE POLICY "Public Select" ON "{table_name}" FOR SELECT USING (true);\n')
        
        # Clear existing data before inserting new ones
        sql_statements.append(f'TRUNCATE TABLE "{table_name}";\n')
        
        # Insert statements
        for row in reader:
            cols = []
            vals = []
            for k, v in row.items():
                safe_k = k.replace('"', '""')
                safe_v = v.replace("'", "''") if v else ""
                cols.append(f'"{safe_k}"')
                vals.append(f"'{safe_v}'")
            
            insert_stmt = f'INSERT INTO "{table_name}" ({", ".join(cols)}) VALUES ({", ".join(vals)});'
            sql_statements.append(insert_stmt)
        
        sql_statements.append('\n')

with open('setup_supabase.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_statements))

print("SQL generated successfully.")
