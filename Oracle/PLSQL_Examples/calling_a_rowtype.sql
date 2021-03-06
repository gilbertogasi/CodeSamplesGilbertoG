DECLARE
  PN_CODIGOCLIENTE NUMBER;
  PN_TIPO_CLIENTE VARCHAR2(200);
  PC_DATOS BE_K_DATOS_PERSONALES.CONSULTADATOSCURSOR;
  LR_DATOS MG_CLIENTES%ROWTYPE;
  PI_CODIGOMENSAJE NUMBER;
  PV_DESCRIPCIONMENSAJE VARCHAR2(200);

  /*TYPE R_CLIENTES IS RECORD
  (NOMBRES           MG_CLIENTES.NOMBRES         %TYPE:= NULL,
   PRIMER_APELLIDO   MG_CLIENTES.PRIMER_APELLIDO %TYPE:= NULL
  );*/

BEGIN
  PN_CODIGOCLIENTE := 187;

  BE_K_DATOS_PERSONALES.BE_P_CONSULTAR_DATOS_CLIENTE(
    PN_CODIGOCLIENTE => PN_CODIGOCLIENTE,
    PN_TIPO_CLIENTE => PN_TIPO_CLIENTE,
    PC_DATOS => PC_DATOS,
    PI_CODIGOMENSAJE => PI_CODIGOMENSAJE,
    PV_DESCRIPCIONMENSAJE => PV_DESCRIPCIONMENSAJE
  );
  DBMS_OUTPUT.PUT_LINE('PN_TIPO_CLIENTE = ' || PN_TIPO_CLIENTE);
  -- Modify the code to output the variable
  -- DBMS_OUTPUT.PUT_LINE('PC_DATOS = ' || PC_DATOS);

--  OPEN PC_DATOS;

  LOOP
    FETCH PC_DATOS INTO LR_DATOS;
    DBMS_OUTPUT.PUT_LINE(LR_DATOS.NOMBRES);
    EXIT WHEN PC_DATOS%NOTFOUND;
  END LOOP;

  CLOSE PC_DATOS;
  /*FOR I IN PC_DATOS LOOP
    DBMS_OUTPUT.PUT_LINE(I.NOMBRES);
  END LOOP;*/

  DBMS_OUTPUT.PUT_LINE('PI_CODIGOMENSAJE = ' || PI_CODIGOMENSAJE);
  DBMS_OUTPUT.PUT_LINE('PV_DESCRIPCIONMENSAJE = ' || PV_DESCRIPCIONMENSAJE);
END;