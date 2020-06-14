DECLARE
  CURSOR c_foreigns IS
     SELECT cons.r_constraint_name PrimaryKey,
            cons.constraint_name   ForeignKey,
            cons.table_name        TableName,
            cons.status
       FROM all_constraints  cons
      WHERE cons.owner             = USER --NVL(UPPER(:P_USUARIO_DUENIO),USER)
        AND cons.constraint_type   = 'R'
        AND cons.r_constraint_name = 'GM_PK_BAL_CUE';

BEGIN
  FOR i IN c_foreigns LOOP
    BEGIN
      EXECUTE IMMEDIATE 'ALTER TABLE '||i.TableName||' ENABLE CONSTRAINT '||i.ForeignKey;
    EXCEPTION
      WHEN OTHERS THEN
        NULL;
    END;
  END LOOP;
END;
/