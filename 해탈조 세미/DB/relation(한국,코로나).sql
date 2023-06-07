SELECT 국가명, 링크, 기사제목, 내용1, 내용2, 내용3 
FROM new_schema.relation 
WHERE (내용1 LIKE '%한국%' OR 내용1 LIKE '%대한민국%') AND 내용1 LIKE '%코로나%'
   OR (내용2 LIKE '%한국%' OR 내용2 LIKE '%대한민국%') AND 내용2 LIKE '%코로나%'
   OR (내용3 LIKE '%한국%' OR 내용3 LIKE '%대한민국%') AND 내용3 LIKE '%코로나%';
   