class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "LAPTOP-ET544B99"
        database_name = "Project_final"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str