-- write your SQL here
SELECT
	o.locationId,
	EXTRACT(YEAR_MONTH FROM t.datetime) as Month_Year,
	SUM(refund.amount) as Refund_Amount
	from transactions t, 
		 JSON_TABLE(details, '$.items[*]' COLUMNS(
		id INT PATH '$.id',
		amount INT PATH '$.amount')) refund
		inner join orderItems o on o.id=refund.id
		group by o.locationId, Month_Year
		order by o.locationId;
