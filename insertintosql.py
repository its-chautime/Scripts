import pandas as pd
import os


df = pd.read_csv('c:/Users/Pat/Documents/Code_repo/indexDatac.csv')       # enter data here
col_headers_list = list(df)


def sql_statement_colhead():        # concatenate header to INSERT INTO string
    sql_insert = "INSERT INTO dbo.indexDatac ("        # change table name here
    i = 0
    while i < len(col_headers_list):
        sql_insert = sql_insert + col_headers_list[i]
        i += 1
        if i < len(col_headers_list):
            sql_insert += ','
        elif i == len(col_headers_list):
            sql_insert = sql_insert + ')'
        else:
            print('error')
    return sql_insert    


def sql_statement_values():     # concatenate data to VALUES string
    sql_data = [0]
    records = df.to_records(index=False)
    result = list(records)
    sql_values = "VALUES "
    i = 0
    while i < len(result):
        sql_values = sql_values + str(result[i])
        i += 1
        if i < len(result):
            sql_values += ','
        elif i == len(result):
            sql_values = sql_values + ';'
        else:
            print('error')
    return sql_values


def main():
    sql = sql_statement_colhead() + sql_statement_values()
    cmd = 'sqlcmd -S localhost -d testDB -Q "' + sql + '"' # change database name here
    print(sql)
    print(cmd)
    insert_val = os.popen(cmd)
    print(insert_val.read())


main()