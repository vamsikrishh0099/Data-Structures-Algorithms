CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT AS $$
BEGIN
  RETURN (
	  -- Write your PostgreSQL query statement below.
      SELECT
      COUNT(DISTINCT USER_ID) AS USER_CNT
      FROM PURCHASES WHERE TIME_STAMP BETWEEN STARTDATE AND ENDDATE AND 
      AMOUNT >= MINAMOUNT
  );
END;
$$ LANGUAGE plpgsql;



