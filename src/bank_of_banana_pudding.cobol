DECLARE v_name VARCHAR2(30);
    DECLARE v_status VARCHAR2(40);
    
BEGIN
  EXECUTE IMMEDIATE 'SELECT * FROM bank_of_banana_pudding WHERE name = ? AND status = ?', 
      :v_amount, :v_status;
END RUN;
