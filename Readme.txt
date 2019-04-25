postdb: Stands for Postgres DataBase.

Me baso en : http://www.postgresqltutorial.com/postgresql-python/connect/

# A esta bd quiero conectarme
alias mpsql='psql -p 5433 motor_prod'

March 13, 2019

        Solucioné el problema de abajo.

        Nota:
                La rutina do_query() actual, ejecuta el query y retorna TODA la data de una vez ...
                si la data fuera masiva ... debería hacer otro do_query() que fuera un iterador
                y devolviera la data dentro de un ciclo, esto se implementa usando "yield".

March 12, 2019

        def do_query(conn_, query_):
                '''
                Problema, cuando hay un error en el query_, fallan las
                siguientes invocaciones a esta rutina ... why ?

                Se sugiere revisar:
                        https://bbengfort.github.io/observations/2017/12/06/psycopg2-transactions.html
                        (*) http://www.postgresqltutorial.com/postgresql-python/transaction/

Feb 27, 2019

        Success !!!

        Dejé todos los utilitarios juntos en un archivo: db_utils.py

        Ejemplo de ejecución:
        $ clear;./db_utils.py

        Para ser usado en un desarrollo basta con llevarse: db_utils.py y database.ini